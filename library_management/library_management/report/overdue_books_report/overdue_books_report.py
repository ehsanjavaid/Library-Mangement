import frappe
from frappe.utils import nowdate

def execute(filters=None):
    columns = [
        {"label": "Book Title", "fieldname": "book_title", "fieldtype": "Data", "width": 200},
        {"label": "Member", "fieldname": "library_member", "fieldtype": "Link", "options": "Library Member", "width": 200},
        {"label": "Return Date", "fieldname": "due_date", "fieldtype": "Date", "width": 120},
        {"label": "Overdue Days", "fieldname": "overdue_days", "fieldtype": "Int", "width": 100},
    ]

    today = nowdate()

    data = frappe.db.sql("""
        SELECT
            child.book AS book_title,
            parent.library_member,
            child.due_date,
            DATEDIFF(%s, child.due_date) AS overdue_days
        FROM `tabBook Issued Items` AS child
        JOIN `tabBook Issue` AS parent ON child.parent = parent.name
        WHERE child.due_date < %s
        AND parent.status = 'Issued'
    """, (today, today), as_dict=True)

    return columns, data
