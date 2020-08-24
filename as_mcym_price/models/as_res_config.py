from odoo import fields,models,api, _

class res_config(models.TransientModel): 
    _inherit='res.config.settings'
        

    as_password_ventas1 = fields.Char(string='Contraseña para aprobar Ventas fuera de margen admitido')
    
    @api.model
    def get_values(self):
        res = super(res_config, self).get_values()
        params = self.env['ir.config_parameter'].sudo()
        res.update(as_password_ventas1 = str(params.get_param('as_sale_pricelist.as_password_ventas1')))
        return res
    
    def set_values(self):
        super(res_config,self).set_values()
        ir_parameter = self.env['ir.config_parameter'].sudo()        
        ir_parameter.set_param('as_sale_pricelist.as_password_ventas1', self.as_password_ventas1)
        
