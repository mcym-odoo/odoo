# -*- coding: utf-8 -*-
{
    'name' : "Ahorasoft customizaciones MYCM",
    'version' : "1.1.5",
    'author'  : "Ahorasoft",
    'description': """
Customizaciones para MCYM
===========================

Custom module for MYCM
    """,
    "depends": [
        "web",
        "sale",'base','report_xlsx',
    ],
    'website': 'http://www.ahorasoft.com',
    'data' : [
        'views/as_report_format.xml',
        'views/report/as_mcym_report_templates.xml',
        'views/report/as_mcym_report_invoice_templates.xml',
        # 'wizard/as_aprobe_utility.xml',
        # 'security/ir.model.access.csv',
     
             ],
    'demo' : [],
    'qweb': [],
    'installable': True,
    'auto_install': False
}
