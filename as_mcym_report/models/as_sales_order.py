from . import amount_to_text_es
from odoo import api, models, fields,_

class as_sales_order(models.Model):

    _inherit = 'sale.order'
    _description = 'Heredando Modelo Ventas'

    def get_literal_amount(self,amount):
        return amount_to_text_es.amount_to_text(amount,'pesos')


    def get_lote(self, product):
        for i in self.picking_ids:
            for linea in i.move_line_ids_without_package:
                if linea.product_id == product:
                    return linea.lot_id.name

