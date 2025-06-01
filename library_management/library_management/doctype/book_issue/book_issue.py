# Copyright (c) 2025, ahsan and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import getdate, nowdate


class BookIssue(Document):
    def validate(self):
        if self.membership_expiry and getdate(self.membership_expiry) < getdate(nowdate()):
            self.membership_validity = "expired"
            frappe.throw("Member has expired membership, cannot issue book.")
