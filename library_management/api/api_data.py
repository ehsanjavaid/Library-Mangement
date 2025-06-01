import frappe
# get details from members
@frappe.whitelist(allow_guest=True)
def get_members():
    return frappe.get_all("Member")

@frappe.whitelist(allow_guest=True)
def get_member(id: str):
    return frappe.get_doc("Member", id) 
# get details for books
@frappe.whitelist(allow_guest=True)
def get_books():
    return frappe.get_all("Book")

@frappe.whitelist(allow_guest=True)
def get_book(id: str):
    return frappe.get_doc("Book", id)

    