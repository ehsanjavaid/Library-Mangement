import frappe
from frappe.utils import nowdate

@frappe.whitelist(allow_guest= True)
def get_dashboard_data():
    user = frappe.session.user
    roles = frappe.get_roles(user)

    if "Librarian" in roles:
        return get_librarian_dashboard()
    elif "Library Member" in roles:
        return get_member_dashboard(user)
    else:
        return {"error": "Unauthorized"}

def get_librarian_dashboard():
    return {
        "role": "Librarian",
        "chart_data": {
            "labels": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
            "visitors": [70, 45, 60, 30, 80, 70, 55],
            "borrowers": [40, 15, 35, 20, 60, 30, 35]
        },
        "overdue_books": [
            {
                "id": "88934231",
                "member": "Daniel",
                "title": "The Midnight Line",
                "author": "Lee Child",
                "overdue": "2 days",
                "return_date": "2023-06-14"
            }
        ]
    }

def get_member_dashboard(user):
    member = frappe.get_value("Library Member", {"email": user}, "name")
    issued_books = frappe.get_all("Book Issue", filters={"library_member": member}, fields=["name", "book", "return_date", "status"])

    return {
        "role": "Library Member",
        "issued_books": issued_books
    }
