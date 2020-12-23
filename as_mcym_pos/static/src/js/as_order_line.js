odoo.define('as_mcym_pos.as_order_line', function (require) {
    "use strict";
    
    var models = require('point_of_sale.models');
    var screens = require('point_of_sale.screens');
    var core = require('web.core');
    
    var QWeb = core.qweb;
    var _t   = core._t;
    
    var _super_orderline = models.Orderline.prototype;
    models.load_fields("pos.order.line",['partner_id','street','localidad','municipio','estado','pais','folio','name_partner','folio_receta']);

    models.Orderline = models.Orderline.extend({
        initialize: function(attr, options) {
            _super_orderline.initialize.call(this,attr,options);
            this.partner_id = this.partner_id || "";
            this.street = this.street || "";
            this.localidad = this.localidad || "";
            this.municipio = this.municipio || "";
            this.estado = this.estado || "";
            this.pais = this.pais || "";
            this.folio = this.folio || "";
            this.folio_receta = this.folio_receta || "";
            this.name_partner = this.name_partner || "";
            this.vat = this.vat || "";
        },
        export_as_JSON: function(){
            var json = _super_orderline.export_as_JSON.call(this);
            json.partner_id = this.partner_id;
            json.street = this.street;
            json.localidad = this.localidad;
            json.municipio = this.municipio;
            json.estado = this.estado;
            json.pais = this.pais;
            json.folio = this.folio;
            json.folio_receta = this.folio_receta;
            json.name_partner = this.name_partner;
            return json;
        },
        init_from_JSON: function(json){
            _super_orderline.init_from_JSON.apply(this,arguments);
            this.partner_id = json.partner_id;
            this.street = json.street;
            this.localidad = json.localidad;
            this.municipio = json.municipio;
            this.estado = json.estado;
            this.pais = json.pais;
            this.folio = json.folio;
            this.folio_receta = json.folio_receta;
            this.name_partner = json.name_partner;
        },
    });
    
    });
    