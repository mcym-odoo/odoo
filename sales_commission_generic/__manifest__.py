# -*- coding: utf-8 -*-
# Part of Ahorasoft. See LICENSE file for full copyright and licensing details.

{
    "name" : "Sales Commission from Sales/Invoice/Payment in Odoo ",
    "version" : "13.0.1.5",
    'category' : "Sales",
    "summary" : "Sale Commission for sales order invoice based commission payment based commission margin based commission for product margin commissions for sales person commission for partner Sales Agent commission Sales Commission for Users commission based on margin",
    "description": """
       """,
    "author" : "Ahorasoft",
    "website" : "https://www.ahorasoft.com",
    "price": 69,
    "currency": 'EUR',
    "depends" : ['base' , 'sale', 'sale_management', 'sale_stock', 'sale_margin'],
    "data" :[
        'security/sales_commission_security.xml',
        'security/ir.model.access.csv',
        'account/account_invoice_view.xml',
        'commission_view.xml',
        'base/res/res_partner_view.xml',
        'sale/sale_config_settings.xml',
        'sale/sale_view.xml',
        'report/commission_report.xml',
        'report/sale_inv_comm_template.xml'
    ],
    "auto_install": False,
    "installable": True,
    "live_test_url":'https://youtu.be/4BlRGFqPiO8',
    "images":['static/description/Banner.png'],
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
