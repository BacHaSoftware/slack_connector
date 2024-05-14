# -*- coding: utf-8 -*-
{
    'name': 'Slack Connector',
    'version': '1.0',
    'author': 'Bac Ha Software',
    'website': 'https://bachasoftware.com',
    'maintainer': 'Bac Ha Software',
    'category': 'Extra Tools',
    'summary': "You can send to Slack email messages generated in odoo.",
    'description': "You can send to Slack email messages generated in odoo.",
    'depends': ['base_setup','mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/slack_connector.xml',
        'views/slack_user_config.xml',
        'views/res_config_settings_views.xml',
    ],
    'external_dependencies': {
        'python': ['slackclient','html-slacker'],
    },
    'images': ['static/description/banner.gif'],
    'installable': True,
    'application': True,
    'license': 'LGPL-3'
}