# -*- coding: utf-8 -*-
{
    'name': 'Systray Search View',
    'version': '15.0.1.0',
    'summary': 'Systray Search View software',
    'sequence': -24000,
    'description': "Systray Search View software using odoo",
    'category': 'Productivity',
    'website': 'https://www.apollohospitals.com/',
    'depends': [ 'web', 'website','stock','base','product'
        # 'base','point_of_sale','contacts'
    ],
    'data': [
        # 'security/ir.model.access.csv',
        # 'wizard/qr_code_wiz.xml',
        # 'views/systray.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'systray_search/static/src/js/qr_generator.js',
            'systray_search/static/src/css/style.css',
        ],
        'web.assets_qweb': [
            # 'qr_code/static/src/xml/systray.xml',
            'systray_search/static/src/xml/qr_generator.xml'
        ],
    },
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
