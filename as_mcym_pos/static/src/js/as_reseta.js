odoo.define('as_mcym_pos.as_reseta', function (require) {
    "use strict";
    var exports = {};

    var core = require('web.core');
    var screens = require('point_of_sale.screens');
    var discount = require('pos_discount.pos_discount');
	var gui = require('point_of_sale.gui');
    var PopupWidget = require('point_of_sale.popups');
    var _t = core._t;
    var Backbone = window.Backbone;
    var rpc = require('web.rpc');
    console.log('cargo para reseta')
    window.descuento = discount;
    var PosBaseWidget = require('point_of_sale.BaseWidget');
    var gui = require('point_of_sale.gui');
    var _t  = require('web.core')._t;

    var ResetaLinePopupWidget = PopupWidget.extend({
        template: 'ResetaLinePopupWidget',
        events: _.extend({}, PopupWidget.prototype.events, {
            'click .confirm': 'click_confirm',
            'keydown': 'add_lot',
            'blur .packlot-line-input': 'lose_input_focus'
        }),
    
        show: function(options){
            this._super(options);
            this.focus();
            var product_id = options.order_line.product.id;
            this.$('#retener').click(function() {
                rpc.query({
                    model: 'pos.order',
                    method: 'get_correlativo',
                    args: [product_id],
                }).then(function(output) {
                    window.lot = output;
                    $('#folio_receta_correlativo').val(output);
                               
                })

            });
            this.$('.search').click(function() {
                var nombres = $('#as_clientes_medicos');
                console.log('entro al recetario')
                var buscando = $('#search_receta').val();
                $('#as_clientes_medicos > tbody > tr').remove();
                var cantidad = 0;
                console.log(buscando)
                rpc.query({
                    model: 'pos.order',
                    method: 'get_client_with_search',
                    args: [buscando],
                }).then(function(output) {
                    window.lot = output;
                    // $('.item_'+output[row][0]).click(function() {$('#name_med').val(output[row][2]);});
                    $('.selecter_id').show();
                    var res_html = '';
                    for (var row = 0; row < output.length; row++) {
                        var selector = "$('#name_med').val('"+output[row][2]+"');"+"$('#cedula').val('"+output[row][1]+"');"+"$('.selecter_id').hide();"+"$('#name_med_id').val('"+output[row][0]+"');"
                        name_med_id
                        window.lect =selector;
                    res_html += '<tr class="item_'+output[row][0]+'" onclick="'+selector+'"><td width="65%" class="nombres">'+output[row][1]+'</td><td width="20%">'+output[row][2]+'</td></tr>';
                }
                console.log(res_html);
    
                $('#as_clientes_medicos > tbody').append(res_html);
                cantidad = $('.item').length;
              
                })
				});









            
        },
        
        click_confirm: function(){
            var order_line = this.options.order_line;
            order_line.name_partner = $('#name_med').val();
            order_line.vat = $('#cedula').val();
            order_line.partner_id = $('#name_med_id').val();
            order_line.street = $('#domicilio').val();
            order_line.localidad =  $('#localidad').val();
            order_line.municipio = $('#municipio').val();
            order_line.estado =  $('#state').val();
            order_line.pais = $('#country').val();
            order_line.folio = $('#folio_receta').val();
            order_line.folio_receta = $('#folio_receta_correlativo').val();
            window.confirmate = this.options;
            this.options.order.save_to_db();
            this.options.order_line.trigger('change', this.options.order_line);
            this.gui.close_popup();
        },
    
        add_lot: function(ev) {
            if (ev.keyCode === $.ui.keyCode.ENTER && this.options.order_line.product.tracking == 'serial'){
                var pack_lot_lines = this.options.pack_lot_lines,
                    $input = $(ev.target),
                    cid = $input.attr('cid'),
                    lot_name = $input.val();
    
                var lot_model = pack_lot_lines.get({cid: cid});
                lot_model.set_lot_name(lot_name);  // First set current model then add new one
                if(!pack_lot_lines.get_empty_model()){
                    var new_lot_model = lot_model.add();
                    this.focus_model = new_lot_model;
                }
                pack_lot_lines.set_quantity_by_lot();
                this.renderElement();
                this.focus();
            }
        },
    
        remove_lot: function(ev){
            var pack_lot_lines = this.options.pack_lot_lines,
                $input = $(ev.target).prev(),
                cid = $input.attr('cid');
            var lot_model = pack_lot_lines.get({cid: cid});
            lot_model.remove();
            pack_lot_lines.set_quantity_by_lot();
            this.renderElement();
        },
    
        lose_input_focus: function(ev){
            var $input = $(ev.target),
                cid = $input.attr('cid');
            var lot_model = this.options.pack_lot_lines.get({cid: cid});
            lot_model.set_lot_name($input.val());
        },
    
        focus: function(){
            this.$("input[autofocus]").focus();
            this.focus_model = false;   // after focus clear focus_model on widget
        }
    });
    gui.define_popup({name:'Resetaline', widget:ResetaLinePopupWidget});

    
    });
    