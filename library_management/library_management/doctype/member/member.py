# Copyright (c) 2025, Ahsan and contributors
# For license information, please see license.txt

import frappe
import random
from frappe.model.document import Document


class Member(Document):
    def before_save(self):
        self.full_name = f"{self.first_name} {self.last_name}".strip()
        if self.payment_status == "Paid" and not self.membership_id:
            self.generate_membership_id()
        self.fee_validate()
        self.fee_update()
        self.insert_payment()

    def generate_membership_id(self):
        prefix_map = {"Regular": "REG", "Student": "STD", "Premium": "PRE"}
        prefix = prefix_map.get(self.membership_type, "GEN")

        if self.is_new() or self.has_value_changed("membership_type"):
            self.membership_id = f"{prefix}-{random.randint(1000, 9999)}"

    def fee_update(self):
        if float(self.amount) > 0:
            self.payment_status = "Paid"
        else:
            self.payment_status = "Unpaid"

    def fee_validate(self):
        try:
            fee_val = float(self.amount)
        except (TypeError, ValueError):
            fee_val = 0

        if fee_val <= 0:
            self.payment_status = "Unpaid"
            frappe.throw("Fee must be greater than 0")

    def insert_payment(self):
        # frappe.msgprint(f"Debug: id = {self.name}")
        membership = frappe.db.exists("Payment", {"membership_id": self.membership_id})
        # frappe.msgprint(f"Debug: membership = {self.membership_id}")
        if membership:
            payment_doc = frappe.get_doc("Payment", membership)
            payment_doc.amount = self.amount
            payment_doc.payment_date = self.payment_date
            payment_doc.payment_type = "Membership Fee"
            payment_doc.status = "Paid"
            payment_doc.save()
        else:
            payment_doc = frappe.get_doc(
                {
                    "doctype": "Payment",
                    "member": self.name,
                    "amount": self.amount,
                    "membership_id": self.membership_id,
                    "membership_type": "Membership Fee",
                    "payment_date": self.payment_date,
                    "status": "Paid",
                }
            )
            payment_doc.insert(ignore_permissions=True)
            frappe.msgprint(f"Payment inserted successfully {self.name}")
