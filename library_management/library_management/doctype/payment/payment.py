# Copyright (c) 2025, ahsan and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Payment(Document):
    pass
    # def before_submit(self):
    #     member = frappe.get_doc("Member", self.member)
    #     transaction = frappe.get_doc("Transaction", self.transaction)
    #     if member.payment_status == "Paid" and member.membership_id:
    #         transaction.payment_type = "Membership Fee"
    #         transaction.status = "Paid"
    #         transaction.currency = member.fee
    #         transaction.save()
