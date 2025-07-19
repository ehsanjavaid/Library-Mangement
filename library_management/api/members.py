import frappe


@frappe.whitelist()
def get_members(page=1, page_length=20, filters=None, search_text=None):
    start = (int(page) - 1) * int(page_length)
    filters = frappe.parse_json(filters) if filters else []

    if search_text:
        filters += [
            ["Member", "name", "like", f"%{search_text}%"],
            ["Member", "first_name", "like", f"%{search_text}%"],
            ["Member", "last_name", "like", f"%{search_text}%"],
        ]

    members = frappe.get_all(
        "Member",
        fields=[
            "membership_id",
            "full_name",
            "phone",
            "email",
            "membership_type",
            "payment_status",
        ],
        filters=filters,
        order_by="creation desc",
        limit_start=start,
        limit_page_length=int(page_length),
    )

    members_count = frappe.db.count("Member", filters=filters)

    return {
        "members": members,
        "total_count": members_count,
        "page": int(page),
        "page_size": int(page_length),
    }
