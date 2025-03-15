# Copyright (c) 2025, ahsan and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import getdate


class Transaction(Document):
	def before_submit(self):
		book = frappe.get_doc("Book", self.book)
		member = frappe.get_doc("Member", self.member)
		payment = frappe.get_doc("Payment", self.payment)
		if member.payment_status == "Unpaid" or not member.membership_id:
			frappe.throw("Please pay the membership fee to issue a book")
		else:
			if book.status == "Borrowed" and book.available_copies == 0:
				frappe.throw(f"The book {book.title} is not available for borrowing")
			if getdate(self.return_date) > getdate(self.due_date):
				frappe.throw("Return Date cannot be greater than Due Date")
			if getdate(self.return_date) < getdate(self.issue_date):
				frappe.throw("Issue Date cannot be greater than Return Date")

		book.available_copies -= 1
		book.save()
	def on_cancel(self):
		book = frappe.get_doc("Book", self.book)
		book.available_copies += 1
		book.save()
		

		
		
		
		
		
