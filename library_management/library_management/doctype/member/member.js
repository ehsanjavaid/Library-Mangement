// Copyright (c) 2025, ahsan and contributors
// For license information, please see license.txt

frappe.ui.form.on("Member", {
    refresh(frm) {
        frm.add_custom_button(__('Contact Us'), function () {
            let admin_number = "923138619329";
            let member_name = frm.doc.name || frappe.doc.member_name;
            let message = `Hello, I am ${member_name}. I would like to inquire about the library membership.`;
            let whatsapp_url = `https://wa.me/${admin_number}?text=${encodeURIComponent(message)}`;
            window.open(whatsapp_url, '_blank');
        });
	},
});
