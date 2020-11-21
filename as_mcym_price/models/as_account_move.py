# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError
import time
import datetime
from time import mktime
from dateutil import parser
from datetime import datetime, timedelta, date

import logging
_logger = logging.getLogger(__name__)

class SaleOrder(models.Model):
    _inherit = "account.move"

    @api.depends('partner_id')
    @api.onchange('partner_id')
    def get_usage_paymentway(self):
        self.l10n_mx_edi_payment_method_id = self.partner_id.l10n_mx_edi_payment_method_id
        self.l10n_mx_edi_usage = self.partner_id.l10n_mx_edi_usage

