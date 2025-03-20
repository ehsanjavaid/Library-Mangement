// Copyright (c) 2025, ahsan and contributors
// For license information, please see license.txt

frappe.ui.form.on("Payment", {
    refresh(frm) {
        if (!frm.is_new()) {
            frm.set_df_property("member", "read_only", 1);
            frm.set_df_property("amount", "read_only", 1);
            frm.set_df_property("payment_type", "read_only", 1);
            frm.set_df_property("payment_date", "read_only", 1);
            frm.set_df_property("status", "read_only", 1);
        }

	},
});
