# -*- coding: utf-8 -*-

from odoo import tools
from odoo import models, fields, api, _
from odoo.exceptions import UserError

import logging
_logger = logging.getLogger(__name__)
      

class SaleOrder(models.Model):
    _inherit = "sale.order"

    as_aprobe = fields.Boolean(string='Aporbar Venta',default=False)

    def action_confirm(self):
        if self.as_aprobe == False:
            access = False
            no_access = False
            for line in self.order_line:
                margin_minimo = line.product_id.as_profit
                if (line.as_margin_porcentaje  < float(margin_minimo)):
                    access= True
            if access:
                action = self.env.ref('as_mcym_price.action_aprobe_sales_mcym_qweb').read()[0]
                action.update({
                    'context': {
                        'default_as_sale': self.id,
                    
                    },
                })
                return action  
        res = super(SaleOrder, self).action_confirm()
        return res

class SaleOrderLine(models.Model):
    _inherit="sale.order.line"
    
    as_margin_porcentaje = fields.Float('Margen Porcentaje',compute='get_margin_porcentaje',store=True)

    @api.depends('price_unit','product_uom_qty')
    def get_margin_porcentaje(self):
        for sale_line in self:
            if sale_line.price_unit:
                costo = sale_line.product_id.as_last_price_purchase
                price = sale_line.price_unit
                price_total_unit = price*sale_line.product_uom_qty
                price_total_cost = costo*sale_line.product_uom_qty
                if price_total_unit > 0:
                    sale_line.as_margin_porcentaje = ((price_total_unit-price_total_cost)/price_total_unit)*100
        