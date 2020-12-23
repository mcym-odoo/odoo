# -*- coding: utf-8 -*-

from odoo import tools
from odoo import models, fields, api, _
from odoo.exceptions import UserError

import logging
_logger = logging.getLogger(__name__)

class SaleOrderLine(models.Model):
    _inherit="res.partner"

    as_medico = fields.Boolean(string='Es médico',default=False)
    # localidad = fields.Char(string='Localidad')
    # municipio = fields.Char(string='Municipio')
    # estado = fields.Char(string='Estado')
    # pais = fields.Char(string='Pais')