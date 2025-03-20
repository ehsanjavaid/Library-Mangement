# Copyright (c) 2025, Ahsan and contributors
# For license information, please see license.txt

import frappe
from frappe.utils import nowdate, getdate
from frappe.model.document import Document

class Payment(Document):
    def validate(self):
        #skipp validation when value is updated
        if not self.get("__islocal"):  
            member = frappe.get_doc("Member", self.member)
            if member.membership_expiry < frappe.utils.getdate(nowdate()):
                frappe.throw("Membership has expired. Please renew your membership.")
            if self.amount > 0:
                self.status = "Paid"

