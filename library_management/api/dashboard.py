import frappe
from frappe.utils import nowdate

@frappe.whitelist()
def get_dashboard_data():
    total_books= frappe.db.count("Book")
    return {
        "total_books":total_books,
    }