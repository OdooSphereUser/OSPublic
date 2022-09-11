/** @odoo-module **/
import SystrayMenu from 'web.SystrayMenu';
import Widget from 'web.Widget';
var ExampleWidget = Widget.extend({
   template: 'PopUpSystray',
   events: {
       'click #create_pu': '_onClick',
   },
   _onClick: function(){
       this.do_action({
            type: 'ir.actions.act_window',
            name: 'PopUp',
            res_model: 'popup.wizardz',
            view_mode: 'form',
            views: [[false, 'form']],
            target: 'new'
       });
   },
});
SystrayMenu.Items.push(ExampleWidget);
export default ExampleWidget;