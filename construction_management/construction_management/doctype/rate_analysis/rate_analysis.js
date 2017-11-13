// Copyright (c) 2017, Frappé and contributors
// For license information, please see license.txt

frappe.ui.form.on('Rate Analysis', {
	setup: function(frm) {
		frm.set_query('asset', "items", function(doc, cdt, cdn){
			return {
				filters: {
					"sub_head": locals[cdt][cdn].type
				}
			}
		});
	},

	total_cost: function(frm) {
		if(frm.doc.items){
			var total = 0;
			frm.doc.items.forEach(r => {
				total += r.cost;
			});
			frm.set_value('total_cost', total);
		}
	},

	cost_for: function(frm) {
		frm.set_value('cost_per_unit', (frm.doc.tax_calculated_cost / frm.doc.cost_for));
	},

	final_unit: function(frm){
		var name = frm.doc.unit + " to " + frm.doc.final_unit;		
		frappe.model.with_doc('Unit Conversion', name, function() {
			var uc = frappe.model.get_doc('Unit Conversion', name);
			console.log(uc.rate);
				var cost = uc.rate * frm.doc.cost_per_unit;
				frm.set_value('final_cost_per_unit', cost);
		})
	},

	refresh: function(frm) {
		frm.trigger('total_cost');
	}
});

frappe.ui.form.on('Rate Analysis Item', {
	quantity: function(frm, cdt, cdn){
		var child = locals[cdt][cdn];
		child.cost = child.rate * child.quantity;
		frm.refresh_field('items');
		frm.trigger('total_cost');
	},
	asset: function(frm, cdt, cdn) {
		var child = locals[cdt][cdn];
		if(child.asset) {
			frappe.model.with_doc('Basic Rates', child.asset, function(){
				var br = frappe.model.get_doc('Basic Rates', child.asset);
					child.unit = br.unit;
					child.rate = br.rate;
					frm.refresh_field('items');
			})
		}
		else {
			child.unit = "";
			child.rate = "";
			frm.refresh_field('items');
		}
	}
});

cur_frm.cscript.calculate_charges_cost = function(doc, cdt, cdn){
	var me = this;
	if(doc.charges.length >= 1){
		var total_percent = 0;
		doc.charges.forEach(r => {
			total_percent += r.percentage;
		});
		var cost = (total_percent / 100) * doc.total_cost; 
		me.frm.set_value('charges_cost', cost + doc.total_cost);
	} else { me.frm.set_value('charges_cost', ""); }
}

cur_frm.cscript.calculate_tax_cost = function(doc, cdt, cdn){
	var me = this;
	if(doc.taxes.length >= 1){
		var total = doc.charges_cost || doc.total_cost;
		var total_percent = 0;
		doc.taxes.forEach(r => {
			total_percent += r.percentage;
		});
		var cost = (total_percent / 100) * total; 
		this.frm.set_value('tax_cost', cost + total);
		this.frm.set_value('tax_calculated_cost', cost + total);
	}
}