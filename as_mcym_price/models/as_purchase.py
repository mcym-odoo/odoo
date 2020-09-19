# -*- coding: utf-8 -*-

from odoo import tools
from odoo import models, fields, api, _
from odoo.exceptions import UserError

import logging
_logger = logging.getLogger(__name__)


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    def button_confirm(self):
        res = super(PurchaseOrder, self).button_confirm()
        for po in self:
            for line in po.order_line:
                #comprobamos si existe variacion del precio anterior con el actual antes de actualizar el costo
                price = 0.0
                costo_mayor = self.get_costo_mayor(line.product_id,line.price_unit)
                if line.product_id.as_last_price_purchase_condicionado > costo_mayor:
                    price = line.product_id.as_last_price_purchase_condicionado
                else:
                    price = costo_mayor
                proporcion = line.price_unit - price
                if proporcion > 0:
                    precio_new = line.product_id.list_price+proporcion
                    line.product_id.list_price = precio_new
                    line.product_id.product_tmpl_id.list_price = precio_new
                    #se actualiza los p;recio en las listas de precios 
                    items = self.env['product.pricelist.item'].search(['|',('product_tmpl_id','=',line.product_id.product_tmpl_id.id),('product_id','=',line.product_id.id)])
                    if items:
                        for value in items:
                            precio_new_list = value.fixed_price+proporcion
                            value.update({'fixed_price':precio_new_list})
                line.product_id.as_last_price_purchase = line.price_unit
                if line.price_unit > line.product_id.as_last_price_purchase_condicionado:
                    line.product_id.as_last_price_purchase_condicionado = line.price_unit
        return res

    def get_costo_mayor(self,product_id,price):
        prices = []
        id_last = product_id.purchase_price_history_line_ids[0].id
        for line in product_id.purchase_price_history_line_ids:
            if id_last != line.id:
                prices.append(line.purchase_price)
        if prices != []:
            precio = max(prices)
        else:
            precio = 0.0
        return precio