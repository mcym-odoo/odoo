# -*- coding: utf-8 -*-

from odoo import tools
from odoo import models, fields, api, _
from odoo.exceptions import UserError

import logging
_logger = logging.getLogger(__name__)

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    as_last_price_purchase = fields.Float(string='Last purchase cost', compute="get_product_supplier_price",store=True)
    as_profit = fields.Float(string='Profit %')
   
