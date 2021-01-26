from . import amount_to_text_es
from odoo import api, models, fields,_

class as_sales_invoice(models.Model):

    _inherit = 'account.move'
    _description = 'Heredando Modelo Ventas'

    def get_literal_amount_two(self,amount):
        return amount_to_text_es.amount_to_text(amount,'pesos') 


class as_get_lote(models.Model):

    _inherit = 'account.move.line'
    _description = 'Heredando Modelo Ventas'

    def get_lote_two(self):
        for line in self: 
            origin = line.move_id.invoice_origin 
            sale = self.env['sale.order'].search([('name','=',origin)]).picking_ids 
            for pick in sale: 
                for pick_l in pick.move_line_ids_without_package: 
                    if line.product_id == pick_l.product_id: 
                        return pick_l.lot_id.name   