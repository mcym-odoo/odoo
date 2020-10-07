# -*- coding: utf-8 -*-

from odoo import tools
from odoo import models, fields, api, _
from odoo.exceptions import UserError

import logging
_logger = logging.getLogger(__name__)

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    def _get_product_supplier_price(self):
        for product in self:
            if  product.as_last_price_purchase <= 0.0:
                product.as_last_price_purchase = product.standard_price
                product.as_last_price_purchase_condicionado = product.standard_price
                product.as_compute = True
            else:
                product.as_compute = False


    as_last_price_purchase = fields.Float(string='Last purchase cost',store=True)
    as_last_price_purchase_condicionado = fields.Float(string='Last purchase cost condicionado',store=True)
    as_profit = fields.Float(string='Profit %')
    as_compute = fields.Boolean(string='Computar costo en cero',compute='_get_product_supplier_price')
   
