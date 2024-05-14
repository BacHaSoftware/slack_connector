import slack, html
import odoo
from odoo import _
import logging
from htmlslacker import HTMLSlacker
from odoo import models, fields, api
from datetime import date

_logger = logging.getLogger(__name__)


class SlackConnector(models.Model):
    _name = 'slack.connector'
    _description = 'Slack connector settings'

    name = fields.Char(string='Name')
    namespace = fields.Selection([('slack','Slack')], string='Namespace')
    workspace_id = fields.Char(string='Workspace ID')
    workspace_name = fields.Char(string='Workspace Name')
    access_token = fields.Char(string='Access Token')
    active = fields.Boolean(string='Active', default=True)

    _sql_constraints = [
        ('namespace_workspace_uniq', 'unique (namespace, workspace_id)', "Workspace ID phải là duy nhất!"),
    ]


class MailThread(models.AbstractModel):
    _inherit = 'mail.thread'

    def _notify_thread(self, message, msg_vals=False, **kwargs):
        recipients_data = super(MailThread, self)._notify_thread(message, msg_vals=msg_vals, **kwargs)
        self._notify_record_by_slack(message, recipients_data, msg_vals=msg_vals, **kwargs)
        return recipients_data

    def _notify_record_by_slack(self, message, recipients_data, msg_vals=False, **kwargs):
        _logger.info("_notify_record_by_slack")

        """ Notification method: by SLACK.

        :param message: mail.message record to notify;
        :param recipients_data: see ``_notify_thread``;
        :param msg_vals: see ``_notify_thread``;
        """
        # notify from computed recipients_data (followers, specific recipients)
        partners_data = [r for r in recipients_data if r['notif'] == 'slack']
        partner_ids = [r['id'] for r in partners_data]
        if partner_ids:
            for partner in self.env['res.partner'].sudo().browse(partner_ids):
                user_data = self.env['res.users'].sudo().search([('partner_id','=',partner.id)])
                slack_user_configs = user_data.slack_user_config.filtered(lambda rec: rec.active is True)

                _logger.info("User: %s" % user_data.name)
                _logger.info("Slack_user_configs: %s" % slack_user_configs)
                _logger.info("Message: %s" % message)

                notif = False  # sql constraints on message and partner => create only one notification
                for slack_user_config in slack_user_configs:
                    try:
                        if message.message_type == 'user_notification' or (not message.subtype_id and message.model == 'hr.leave'):
                            text = message.subject
                        else:
                            text = message.body

                        text = HTMLSlacker(text).get_output()
                        # link_record = message.action_open_document()

                        web_base_url = self.env['ir.config_parameter'].sudo().get_param(
                            'web.base.url')  # must be https if not localhost

                        link = web_base_url + '/web#id=%s&model=%s&view_type=form' % (message.res_id, message.model)
                        if message.model == 'mail.channel':
                            act_mail_channel = self.env['ir.model.data'].sudo().search([('module','=','mail'),('name','=','action_discuss')],limit=1)
                            link = web_base_url + '/web#default_active_id=mail.box_inbox&action=%s&active_id=mail.channel_%s' % (act_mail_channel.res_id, message.res_id)

                        text_slack = _(':speech_balloon: *Thông báo từ Odoo*:')
                        # text_slack += _('\n*Loại*:') + dict(message._fields['message_type'].selection).get(message.message_type)
                        model_description = self.env['ir.model'].sudo().search([('model','=',message.model)],limit=1)
                        if model_description:
                            text_slack += _('\n*%s:*') % model_description.name
                        if not text:
                            text = _('*Thông báo hệ thống (%s)*') % (message.subtype_id.name)
                        text_slack += _('\n*Nội dung*: ') + html.unescape(text)

                        if message.author_id:
                            text_slack += _('\n*Người gửi*: ') + message.author_id.name
                        if message.subtype_id:
                            text_slack += _('\n*Kiểu*: ') + message.subtype_id.name

                        text_slack += _('\n*Link*: ') + link

                        client = slack.WebClient(token=slack_user_config.slack_connector.access_token)
                        # tin nhắn hệ thống để tracking các trường thay đổi nên không gửi
                        if message.message_type == 'notification':
                            pass
                        # elif message.model == 'hr.leave' and not message.subtype_id:
                        #     pass
                        else:
                            client.chat_postMessage(channel=slack_user_config.member_id, blocks=[
                                {
                                    "type": "section",
                                    "text": {
                                        "type": "mrkdwn",
                                        "text": text_slack
                                    }
                                }
                            ])
                    except Exception as e:
                        _logger.exception(e)
                        if not notif:
                            notif = self.env['mail.notification'].sudo().create({
                                'mail_message_id': message.id,
                                'res_partner_id': partner.id,
                                'notification_type': 'slack',
                                'slack_user_config': slack_user_config.id,
                                'is_read': True,  # discard Inbox notification
                                'notification_status': 'sent',
                                'failure_type': 'slack_server',
                                'failure_reason': e
                            })

                    if not notif:
                        notif = self.env['mail.notification'].sudo().create({
                            'mail_message_id': message.id,
                            'res_partner_id': partner.id,
                            'notification_type': 'slack',
                            'slack_user_config': slack_user_config.id,
                            'is_read': True,  # discard Inbox notification
                            'notification_status': 'sent'
                        })
