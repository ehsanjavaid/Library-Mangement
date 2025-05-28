// // Copyright (c) 2025, ahsan and contributors
// // For license information, please see license.txt

frappe.ui.form.on("Member", {
    refresh(frm) {
        frm.add_custom_button(__('Contact Us'), function () {
            frappe.call({
                method: "frappe.client.get_list",
                args: {
                    doctype: "Whatsapp Saved Template",
                    fields: ["message_body", "attachment"],
                    limit_page_length: 100,
                },
                callback: function (response) {
                    if (!response.message || response.message.length == 0) {
                        frappe.msgprint(__('No saved templates found.'));
                        return;
                    }

                    let admin_number = "923138619329";
                    let member_name = frm.doc.name || frm.doc.member_name;

                    const messageMap = {};
                    const options = response.message.map(row => {
                        let message = row.message_body.replace("{{member_name}}", member_name);
                        messageMap[message] = row.attachment || null;
                        return message;
                    });

                    let d = new frappe.ui.Dialog({
                        title: __('Choose message to send'),
                        fields: [
                            {
                                label: 'Message Options',
                                fieldname: 'message',
                                fieldtype: 'Select',
                                options: options,
                                reqd: 1
                            }
                        ],
                        primary_action_label: __('Send On WhatsApp'),
                        primary_action(values) {
                            const message = values.message;
                            const attachment = messageMap[message];
                            let final_message = message;

                            if (attachment) {
                                final_message += `\n ${window.location.origin}${attachment}`;
                            }

                            let whatsapp_url = `https://wa.me/${admin_number}?text=${encodeURIComponent(final_message)}`;
                            window.open(whatsapp_url, '_blank');
                            d.hide();
                        }
                    });

                    d.show();
                }
            });
        });
    }
});

