odoo.define('as_mcym_pos.as_product', function (require) {

	var exports = {};

    var session = require('web.session');
    var Backbone = window.Backbone;
    var core = require('web.core');
    var screens = require('point_of_sale.screens');
    var models = require('point_of_sale.models');
    var rpc = require('web.rpc');

    var _t = core._t;
    
    var QWeb = core.qweb;

    var pedido_actual = 0;

    console.log("Se cargado stock");
    window.cathh = models
 
    models.load_fields("product.product", "as_product_reseta");
    
    var OrderlineSuper = models.Orderline;
    models.Orderline = models.Orderline.extend({
    
      get_as_availity_reset: function() {
        console.log('valor -----> '+this);
        window.jota = this;

          return this.product.as_product_reseta;
      },

    });
    
screens.OrderWidget.include({
  render_orderline: function(orderline) {
    console.log('entro a al funcion de mostrar lotes');
    var node = this._super(orderline);
    var el_reseta_icon = node.querySelector('#botton_reseta');
    if(el_reseta_icon){
      el_reseta_icon.addEventListener('click', (function() {
        this.show_resetas_product(orderline);
      }.bind(this)));
    }
    return node;
  },
  show_resetas_product: function(orderline){
    this.pos.get_order().select_orderline(orderline);
    var order = this.pos.get_order();
    order.display_reseta_popup();
  },
});


var _super_Order = models.Order.prototype;
models.Order = models.Order.extend({
  initialize: function(attr,options){
      _super_Order.initialize.apply(this,arguments);
  },
  display_reseta_popup: function() {
    var order_line = this.get_selected_orderline();
    if (order_line){
        this.pos.gui.show_popup('Resetaline', {
            'title': _t('Agregar Receta Medica'),
            'order_line': order_line,
            'order': this,
            'name_partner': order_line.name_partner,
            'folio' : order_line.folio,
            'folio_receta' : order_line.folio_receta,
            'vat' : order_line.vat,
            'street' : order_line.street,
            'localidad' : order_line.localidad,
            'municipio' : order_line.municipio,
            'estado' : order_line.estado,
            'pais' : order_line.pais,
            
        });
    }
  },        
//   display_lot_popup: function() {
    
//     var self  = this;
//     var order_line = this.get_selected_orderline();
//     var product = order_line.get_product();
//     var picking_type_id = this.pos.config.picking_type_id[0];
//     var order = order_line.pos.get_order();
//     if (order_line){
//       if(order_line.product.as_product_reseta){
//         if (order.get("habilitar_lote")){
//           var pack_lot_lines =  order_line.compute_lot_lines();
//           rpc.query({
//             model: 'stock.quant',
//             method: 'get_pos_quants',
//             args: [[product.id, picking_type_id]],
//         }).then(function(backend_result) {
//             if (backend_result) {
//                 if (order_line) {
//                     product.lot_result = backend_result;
//                     // order_line.compute_lot_lines();
//                     self.pos.gui.show_popup('PackLotLinePopupWidgetNew', {
//                         'title': 'Lot/Serial Number(s)',
//                         'pack_lot_lines': backend_result,
//                         'order_line': order_line,
//                         'order': this,
//                     });
//                 }
//             }
    
//         });
  
//         }
//       }else{
//         var pack_lot_lines =  order_line.compute_lot_lines();
//         rpc.query({
//           model: 'stock.quant',
//           method: 'get_pos_quants',
//           args: [[product.id, picking_type_id]],
//       }).then(function(backend_result) {
//           if (backend_result) {
//               if (order_line) {
//                   product.lot_result = backend_result;
//                   // order_line.compute_lot_lines();
//                   self.pos.gui.show_popup('PackLotLinePopupWidgetNew', {
//                       'title': 'Lot/Serial Number(s)',
//                       'pack_lot_lines': backend_result,
//                       'order_line': order_line,
//                       'order': this,
//                   });
//               }
//           }
  
//       });
//       }
//     }
// },

});

});