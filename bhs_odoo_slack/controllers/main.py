# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import requests
import logging
from odoo import http, _
from odoo.http import request
from odoo.exceptions import UserError

_logger = logging.getLogger(__name__)

#----------------------------------------------------------
# Controller
#----------------------------------------------------------

class SlackAuthentication(http.Controller):
    @http.route('/slack', type='http', auth='public', website=True, sitemap=False)
    def get_authentication(self, **kw):
        """Get token for workspace when click install app in slack"""
        code = kw.get('code')
        client_id = request.env['ir.config_parameter'].sudo().get_param('slack_client_id')
        client_secret = request.env['ir.config_parameter'].sudo().get_param('slack_client_secret')
        headers = {'content-type': "application/x-www-form-urlencoded"}
        body = {'code': code,
                'client_id': client_id,
                'client_secret': client_secret}

        r = requests.post("https://slack.com/api/oauth.v2.access", headers=headers, data=body)
        result_data = r.json()

        if result_data.get('ok'):
            access_token = result_data.get('access_token')
            workspace_id = result_data.get('team').get('id')
            workspace_name = result_data.get('team').get('name')
            check_connection = request.env['slack.connector'].sudo().search(
                               [('namespace', '=', 'slack'), ('workspace_id', '=', workspace_id)])

            if len(check_connection) == 0:
                request.env['slack.connector'].sudo().create({
                    'name': 'Slack: %s' % workspace_name,
                    'namespace':'slack',
                    'workspace_id': workspace_id,
                    'workspace_name': workspace_name,
                    'access_token': access_token,
                    'active': True
                })
            else:
                check_connection.write({'name': 'Slack: %s' % workspace_name,
                                        'access_token': access_token,
                                        'active': True})

        _logger.info("Access_token: %s" % access_token)
        _logger.info("Workspace_id: %s" % workspace_id)
        _logger.info("Workspace_name: %s" % workspace_name)


