from openerp import api, fields, models

class ProductProduct(models.Model):
    _inherit = "product.category"

    as_secuencia_categ =  fields.Many2one('ir.sequence', string="Secuencia Para Productos", help=u'Secuencia Para Productos')