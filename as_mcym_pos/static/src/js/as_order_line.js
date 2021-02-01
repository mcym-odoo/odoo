odoo.define('as_mcym_pos.as_order_line', function (require) {
    "use strict";

    var models = require('point_of_sale.models');
    var screens = require('point_of_sale.screens');
    var core = require('web.core');
    var PopupWidget = require('point_of_sale.popups');
    var gui = require('point_of_sale.gui');
    var QWeb = core.qweb;
    var _t = core._t;
    var _super_order = models.Order.prototype;
    models.load_fields("pos.order.line", ['partner_id', 'street', 'localidad', 'municipio', 'estado', 'pais', 'folio', 'name_partner', 'folio_receta']);

        // new widget, so fine if we dont check it in details for v13
        var PackLotLinePopupWidgetNew1 = PopupWidget.extend({
            template: 'PackLotLinePopupWidgetNew',
            events: _.extend({}, PopupWidget.prototype.events, {}),
            show: function(options) {
                this._super(options);
                this.update_qty();
    
                this.$('.lot_qty_autocheckbox').click(function(event){
                    var ev_target = $(event.target);
                    var checked = ev_target[0].checked;
                    if(checked){
                        $('.'+ev_target.attr('id')).val(parseInt(ev_target.attr('data-lot_qty')));
                    }
                    if(!checked){
                        $('.'+ev_target.attr('id')).val("");
                    }
                });
    
            },
            update_qty: function(){
                var order_line = this.pos.get_order().get_selected_orderline();
                var get_lot_ids = order_line.get_lot_ids();
                if (get_lot_ids != 'undefined' && get_lot_ids.length > 0) {
                    $('.popup').find('.lot_inputs').each(function(index, el) {
                        var cid = $(el).attr('data-lot-index');
                        $.each(get_lot_ids, function(index, dict) {
                            if (dict['lot_id'] == cid) {
                                $(el).val(dict['qty_done']);
                            }
                         });
                    });
                }
            },
            click_cancel: function(){
                this._super();
                var order = this.pos.get_order();
                var order_line = this.options.order_line;
                if (order_line.product.as_product_reseta){

                    order.display_reseta_popup();
                }
                // this.pos.get_order().get_selected_orderline().set_quantity(0);
            },
            click_confirm: function() {
                console.log('entro al heredado CATHA')
                var self = this;
                var order_line = this.options.order_line;
                var pack_lot_lines = this.options.pack_lot_lines;
                var lot_inputs = self.$('.lot_inputs');
                var lot_ids = [];
                var has_error = false;
                var has_blank_inputs = false;
                var has_atleast_onefilled = false;
                if (lot_inputs) {
                    var sum = 0;
                    _.each(lot_inputs, function(lotinput) {
                        var lotinput_val = $(lotinput).val(); 
                        var lot_qty = parseInt(lotinput_val);
                        if(lotinput_val == ""){
                            lot_qty = 0;
                        }
                        var datalotqty = $(lotinput).parent().parent().children('td.lot_qty').data('lotqty');
                        if(lot_qty > datalotqty || lot_qty <= 0){
                            $(lotinput).css('border','2px solid red');
                            has_blank_inputs = true;
                        }
                        else if (lot_qty) {
                            sum += lot_qty;
                            var lot_id = lotinput.getAttribute('data-lot-index');
                            var package_id = lotinput.getAttribute('data-package_id');
                            lot_ids.push({
                                'lot_id': parseInt(lot_id),
                                'qty_done': lot_qty,
                                'package_id': package_id,
                            });
                            order_line.has_product_customlot = true;
                            has_atleast_onefilled = true;
                        }
                    });
                    if(has_blank_inputs && !has_atleast_onefilled)
                        return;
                    order_line.set_quantity(sum);
                    order_line.set_lot_ids(lot_ids);
                    this.gui.close_popup();
                    var order = this.pos.get_order();
                    if (order_line.product.as_product_reseta){

                        order.display_reseta_popup();
                    }
                }
            },
        });
        gui.define_popup({
            name: 'PackLotLinePopupWidgetNew',
            widget: PackLotLinePopupWidgetNew1
        });
    

    // models.Order = models.Order.extend({
    // add_product : function (product, options) {
    //     var result = _super_order.add_product.apply(this, arguments);
    //     var order    = this.pos.get_order();
    //     if(product.as_product_reseta !== false){
    //         console.log('ENTRO A MOSTRAR RESETA');
    //         var order = this.pos.get_order();
    //         window.mostrat_line = order;
    //         order.display_reseta_popup();
    //         console.log('debio generar el POPUP');
    //         order.set("habilitar_lote",true)
    //     }
    //     return result;

    // }
    // });

    var _super_orderline = models.Orderline.prototype;
    models.Orderline = models.Orderline.extend({
        initialize: function (attr, options) {
            _super_orderline.initialize.call(this, attr, options);
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
        export_as_JSON: function () {
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
            json.vat = this.vat;
            return json;
        },
        init_from_JSON: function (json) {
            _super_orderline.init_from_JSON.apply(this, arguments);
            this.partner_id = json.partner_id;
            this.street = json.street;
            this.localidad = json.localidad;
            this.municipio = json.municipio;
            this.estado = json.estado;
            this.pais = json.pais;
            this.folio = json.folio;
            this.folio_receta = json.folio_receta;
            this.name_partner = json.name_partner;
            this.vat = json.vat;
        },
        
    });

});