# -*- coding: utf-8 -*-
#################################################################################
# Author      : Webkul Software Pvt. Ltd. (<https://webkul.com/>)
# Copyright(c): 2015-Present Webkul Software Pvt. Ltd.
# All Rights Reserved.
#
#
#
# This program is copyright property of the author mentioned above.
# You can`t redistribute it and/or modify it.
#
#
# You should have received a copy of the License along with this program.
# If not, see <https://store.webkul.com/license.html/>
#################################################################################
{
  "name"                 :  "POS Home Delivery",
  "summary"              :  """Create Sales Order/Quotation, without leaving POS, which can be processed later.""",
  "category"             :  "Point Of Sale",
  "version"              :  "1.0",
  "author"               :  "Webkul Software Pvt. Ltd.",
  "license"              :  "Other proprietary",
  "website"              :  "https://store.webkul.com/Odoo-POS-Home-Delivery.html",
  "description"          :  """http://webkul.com/blog/odoo-pos-home-delivery/""",
  "live_test_url"        :  "http://odoodemo.webkul.com/?module=pos_to_sales_order&custom_url=/pos/auto",
  "depends"              :  [
                             'point_of_sale',
                             'sale',
                            ],
  "data"                 :  [
                             'views/pos_to_sales_order_view.xml',
                             'views/templates.xml',
                             'data/pos_to_sale_order_demo.xml',
                             'security/ir.model.access.csv',
                            ],
  "qweb"                 :  ['static/src/xml/pos_to_sale_order.xml'],
  "images"               :  ['static/description/Banner.png'],
  "application"          :  True,
  "installable"          :  True,
  "auto_install"         :  False,
  "price"                :  35,
  "currency"             :  "USD",
  "pre_init_hook"        :  "pre_init_check",
}