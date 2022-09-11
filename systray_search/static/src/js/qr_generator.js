
/** @odoo-module **/



import SystrayMenu from 'web.SystrayMenu';
import Widget from 'web.Widget';
var ExampleWidget = Widget.extend({
    template: 'SearchBarSystray',




   events: {
       'click #button': '_onClick',
   },
   _onClick: function(){



       var input = document.getElementById("input").value
       console.log(input,'input')

       if ((input).length > 10) {
                try {
                alert("NO product for  " + input);
            }
            catch(err) {
                document.getElementById("input").innerHTML
                        = err.message;
            }
            }

       this.do_action({
            type: 'ir.actions.act_window',
            name: 'products',
            res_model: 'product.template',
            view_mode: 'list',
            views: [[false, 'list']],
            domain: ['|',['default_code', 'ilike', document.getElementById("input").value],['name', 'ilike', document.getElementById("input").value]],
            target: 'new'
       });
   },
});
SystrayMenu.Items.push(ExampleWidget);
export default ExampleWidget;