import frappe
from frappe.utils import nowdate
from datetime import datetime, timedelta
from frappe import _


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


# AddBook form button
@frappe.whitelist()
def add_book(**kwargs):
    # Optional: required field check
    required_fields = [
        "title",
        "author",
        "category",
        "location",
        "total_copies",
        "status",
    ]
    for field in required_fields:
        if not kwargs.get(field):
            frappe.throw(_(f"{field.capitalize()} is required"))

    try:
        book = frappe.get_doc({"doctype": "Book", **kwargs})
        book.insert()
        frappe.db.commit()

        return {"message": "Book added successfully", "name": book.name}

    except Exception as e:
        frappe.log_error(str(e), "Add Book Error")
        raise
