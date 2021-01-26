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
    var el_str  = QWeb.render('Orderline',{widget:this, line:orderline}); 
    var el_node = document.createElement('div');
        el_node.innerHTML = _.str.trim(el_str);
        el_node = el_node.childNodes[0];
        el_node.orderline = orderline;
        el_node.addEventListener('click',this.line_click_handler);
    var el_lot_icon = el_node.querySelector('.line-lot-icon');
    var el_reseta_icon = el_node.querySelector('#botton_reseta');
    if(el_lot_icon){
        el_lot_icon.addEventListener('click', (function() {
            this.show_product_lot(orderline);
        }.bind(this)));
    }
    if(el_reseta_icon){
      el_reseta_icon.addEventListener('click', (function() {
          this.show_resetas_product(orderline);
      }.bind(this)));
  }

    orderline.node = el_node;
    return el_node;
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
        });
    }
  },
  display_lot_popup: function() {
    console.log('entro a al funcion de mostrar lotes');
    var order_line = this.get_selected_orderline();
    var order = order_line.pos.get_order();
    if (order_line){
      if(order_line.product.as_product_reseta){
        if (order.get("habilitar_lote")){
          var pack_lot_lines =  order_line.compute_lot_lines();
          this.pos.gui.show_popup('packlotline', {
              'title': _t('Lot/Serial Number(s) Required'),
              'pack_lot_lines': pack_lot_lines,
              'order_line': order_line,
              'order': this,
          });
  
        }
      }else{
        var pack_lot_lines =  order_line.compute_lot_lines();
        this.pos.gui.show_popup('packlotline', {
            'title': _t('Lot/Serial Number(s) Required'),
            'pack_lot_lines': pack_lot_lines,
            'order_line': order_line,
            'order': this,
        });
      }
    }
},
});

});