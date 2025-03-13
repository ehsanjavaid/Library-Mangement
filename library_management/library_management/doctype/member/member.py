# Copyright (c) 2025, ahsan and contributors
# For license information, please see license.txt

import frappe
import random 
from frappe.model.document import Document


class Member(Document):
	def generate_membership_id(self):
			prefix_map = {
				"Student": "STD",
				"Regular": "REG",
				"Premium": "PRE"
			}
			prefix = prefix_map.get(self.membership_type, "GEN")
			random_number = random.randint(1000, 9999)
			return f"{prefix}-{random_number}" 
	
	def before_save(self):
		self.full_name = f"{self.first_name} {self.last_name}"
		if self.payment_status == "Paid" and not self.membership_id:
			self.membership_id = self.generate_membership_id()
		
		