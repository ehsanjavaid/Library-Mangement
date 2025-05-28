# whatsapp.py
import frappe
from twilio.rest import Client

@frappe.whitelist()
def send_whatsapp_message(template_id, member_name, recipient_number):
    doc = frappe.get_doc("Whatsapp Saved Template", template_id)

    # Replace placeholder
    message_body = doc.message_body.replace("{{member_name}}", member_name)

    # Optional file link (like Google Drive)
    attachment_link = f"\n\nAttachment: {doc.attachment}" if doc.attachment else ""

    final_message = f"{message_body}{attachment_link}"

    # Twilio credentials
    account_sid = frappe.conf.twilio_account_sid
    auth_token = frappe.conf.twilio_auth_token
    from_whatsapp_number = 'whatsapp:+14155238886'

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_=from_whatsapp_number,
        body=final_message,
        to=recipient_number
    )

    return message.sid
