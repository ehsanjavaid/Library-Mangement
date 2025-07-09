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
# Books Allocation by Locations (Donut Chart
@frappe.whitelist()
def get_books_by_location():
    locations = frappe.get_all("Book", fields=["location"], pluck="location")
    from collections import Counter
    location_counts = Counter(locations)
    result = [{"name": loc, "count": count} for loc, count in location_counts.items()]
    return result

# Books Availability
@frappe.whitelist()
def get_books_availability():
    books = frappe.db.sql(""" 
                          SELECT status AS name, COUNT(*) AS count
                          FROM `tabBook`
                          GROUP BY status
                          """, as_dict=True)
    return books