# -*- coding: utf-8 -*-
{
    'name' : "Ahorasoft customizaciones MYCM",
    'version' : "1.0.1",
    'author'  : "Ahorasoft",
    'description': """
Customizaciones para MCYM
===========================

Custom module for MYCM
    """,
    'category' : "Sale",
    'depends' : [ "base",
        "sale_management",
        'product',"purchase",'sale','sales_commission_generic','l10n_mx_edi'],
    'website': 'http://www.ahorasoft.com',
    'data' : [
        'views/as_product_template.xml',
        'views/as_res_config.xml',
        'views/as_res_partner.xml',
        'views/sale_order_inherit_view.xml',
        'wizard/as_aprobe_utility.xml',
        'security/ir.model.access.csv',
     
             ],
    'demo' : [],
    'qweb': [],
    'installable': True,
    'auto_install': False
}
