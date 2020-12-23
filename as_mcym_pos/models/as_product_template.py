# -*- coding: utf-8 -*-

from odoo import tools
from odoo import models, fields, api, _
from odoo.exceptions import UserError

import logging
_logger = logging.getLogger(__name__)

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    as_product_reseta = fields.Boolean(string='Venta con receta médica',store=True)

  
class ProductProduct(models.Model):
    _inherit = "product.product"

    as_product_reseta = fields.Boolean(related='product_tmpl_id.as_product_reseta')