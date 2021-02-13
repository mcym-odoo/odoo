from . import amount_to_text_es
from odoo import api, models, fields,_

class as_sales_invoice(models.Model):

    _inherit = 'account.move'
    _description = 'Heredando Modelo Ventas'

    def get_literal_amount_two(self,amount,moneda):
        return amount_to_text_es.amount_to_text(amount,moneda)

    def enteros_y_centavos(self,amount):
        cantidad = str(amount).split('.')
        valor_entero = cantidad[0]
        valor_cemtavos = cantidad[1]
        pesos = self.get_literal_amount_two(int(valor_entero),'pesos')
        centavos = self.get_literal_amount_two(int(valor_cemtavos),'centavos')

        valor_total = str(pesos + " PESOS Y " +centavos + " CENTAVOS")

        return valor_total

    def lxn_usage(self, value):
        
        dicionario = {
        'G01': 'Adquisición de mercancías',
        'G02': 'Devoluciones, descuentos o bonificaciones',
        'G03': 'Gastos en general',
        'I01': 'Construcciones',
        'I02': 'Mobilario y equipo de oficina por inversiones',
        'I03': 'Equipo de transporte',
        'I04': 'Equipo de cómputo y accesorios',
        'I05': 'Dados, troqueles, moldes, matrices y herramental',
        'I06': 'Comunicaciones telefónicas',
        'I07': 'Comunicaciones satelitales',
        'I08': 'Other machinery and equipment',
        'D01': 'Otra maquinaria y equipo.',
        'D02': 'Gastos médicos por incapacidad o discapacidad',
        'D03': 'Gastos funerales',
        'D04': 'Donaciones',
        'D05': 'Intereses reales efectivamente pagados por créditos hipotecarios casa habitación.',
        'D06': 'Aportaciones voluntarias al SAR.',
        'D07': 'Primas por seguros de gastos médicos',
        'D08': 'Gastos de transportación escolar obligatoria.',
        'D09': 'Depósitos en cuentas para el ahorro, primas que tengan como base planes de pensiones.',
        'D10': 'Pagos por servicios educativos colegiaturas',
        'P01': 'Por definir',
        }
        return dicionario[value]



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


