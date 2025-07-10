import frappe
from frappe.utils import nowdate
from datetime import datetime, timedelta


@frappe.whitelist()
def get_books_list(page=1, page_length=20, filters=None, search_text=None):
    start = (int(page) - 1) * int(page_length)

    # Initialize filters if not passed
    filters = frappe.parse_json(filters) if filters else []

    # Apply search filter using OR conditions
    if search_text:
        filters += [
            ["Book", "name", "like", f"%{search_text}%"],
            ["Book", "title", "like", f"%{search_text}%"],
            ["Book", "author", "like", f"%{search_text}%"],
        ]

    books = frappe.get_all(
        "Book",
        fields=[
            "name",
            "title",
            "author",
            "category",
            "status",
            "location",
            "total_copies",
        ],
        filters=filters,
        order_by="creation desc",
        limit_start=start,
        limit_page_length=int(page_length),
    )

    total_count = frappe.db.count("Book", filters=filters)

    return {
        "books": books,
        "total_count": total_count,
        "page": int(page),
        "page_size": int(page_length),
    }
