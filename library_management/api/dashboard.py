import frappe
from frappe.utils import nowdate
from datetime import datetime, timedelta


@frappe.whitelist(allow_guest=True)
def get_dashboard_data():
    total_books = frappe.db.count("Book")
    issued_books_item = frappe.db.count(
        "Book Issued Items",
        filters={
            "status": "Issued",
        },
    )
    book_issue = frappe.db.count("Book Issue")
    available_books = total_books - issued_books_item
    return {
        "total_books": total_books,
        "members": frappe.db.count("Member"),
        "book_issue": book_issue,
        "available_books": available_books,
    }


#  Visiters log insert graph
def insert_visitor(ip=None, page=None):
    frappe.get_doc(
        {
            "doctype": "Visitor Log",
            "visitor_ip": ip,
            "visited_on": nowdate(),
            "visited_page": page
        }
    ).insert(ignore_permissions=True)
    return {"message": "Visitor log inserted successfully"}


def get_visitor_stats():
    labels, data = [], []
    for i in range(7):
        day = (datetime.today() - timedelta(days=i)).date()
        count = frappe.db.count("Visitor Log", {"visited_on": day})
    labels.insert(0, day.strftime("%a"))  # e.g. 'Mon'
    data.insert(0, count)

    return {"labels": labels, "data": data}
