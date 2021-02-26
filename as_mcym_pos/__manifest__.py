# -*- coding: utf-8 -*-
{
    'name' : "Ahorasoft POS customizaciones MYCM",
    'version' : "1.0.6",
    'author'  : "Ahorasoft",
    'description': """
Customizaciones para MCYM
===========================

Custom module for MYCM
    """,
    'category' : "Sale",
    'depends' : [ "base",
        "point_of_sale","pos_lots_selection","ks_pos_low_stock_alert","pos_to_sales_order"],
    'website': 'http://www.ahorasoft.com',
    'data' : [
        'views/as_product_template.xml',
        'views/templates.xml',
        'views/as_sequence.xml',
        'views/as_product_category.xml',
        'views/por_order.xml',
        'views/as_res_partner.xml',
        'report/as_pos_order_report.xml',
        # 'wizard/as_aprobe_utility.xml',
        # 'security/ir.model.access.csv',
     
             ],
    'qweb': ['static/src/xml/*.xml'],
    'demo' : [],
    'installable': True,
    'auto_install': False
}
