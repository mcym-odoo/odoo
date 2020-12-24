# -*- coding: utf-8 -*-

from odoo import tools
from odoo import models, fields, api, _
from odoo.exceptions import UserError

import logging
_logger = logging.getLogger(__name__)

class SaleOrder(models.Model):
    _inherit="pos.order"

    lines_recetas_ids = fields.One2many("pos.order.line",'order_id', string='Recetas')

    @api.model
    def get_correlativo(self,product):    
        products = self.env['product.product'].search([('id','=',product)])
        correlativo= products.categ_id.as_secuencia_categ.next_by_id()
        return correlativo
        
    @api.model
    def get_client_with_search(self,criterio):
        vals=[]
        consulta_pos = ("""
            select id,vat,name,street,localidad,municipio,estado,pais from res_partner where (name ilike '%"""+str(criterio)+"""%' or vat ilike '%"""+str(criterio)+"""%')
            and as_medico = true
            """)    

        self.env.cr.execute(consulta_pos)

        for array in self.env.cr.fetchall():
            vals.append(array)
        return vals

class SaleOrderLine(models.Model):
    _inherit="pos.order.line"

    partner_id = fields.Many2one("res.partner", string='Medico')
    street = fields.Text(string='Dirección')
    localidad = fields.Char(string='Localidad')
    municipio = fields.Char(string='Municipio')
    estado = fields.Char(string='Estado')
    pais = fields.Char(string='Pais')
    folio = fields.Char(string='Folio Interno')
    vat = fields.Char(string='ci')
    name_partner = fields.Char(string='name partner')
    folio_receta = fields.Char(string='Folio Receta')

    @api.model
    def create(self, vals):
        result = super(SaleOrderLine, self).create(vals)
        if result.name_partner:
            partner_id = self.env['res.partner'].search([('name','=',result.name_partner),('as_medico','=',True)])
            if partner_id:
                result.partner_id = partner_id.id
            else:
                partner_id = self.env['res.partner'].create(
                    {'name': result.name_partner, 
                    'vat': result.vat,
                    'localidad': result.localidad,
                    'municipio': result.municipio,
                    'estado': result.estado,
                    'pais': result.pais,
                    'as_medico': True,
                    'street': result.street+' '+result.localidad+' '+result.estado+' '+result.pais,
                    })
                result.partner_id = partner_id.id

        return result

