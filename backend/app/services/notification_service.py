# app/services/notification_service.py

import os
from twilio.rest import Client

# Load credentials from .env file
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
twilio_number = os.getenv("TWILIO_PHONE_NUMBER")
my_number = os.getenv("MY_PHONE_NUMBER")

# Initialize the Twilio client
client = Client(account_sid, auth_token)

def send_whatsapp_message(body: str):
    """Sends a WhatsApp message using Twilio."""
    if not all([account_sid, auth_token, twilio_number, my_number]):
        print("❌ Twilio credentials are not fully configured. Cannot send message.")
        return

    try:
        message = client.messages.create(
            from_=twilio_number,
            body=body,
            to=my_number
        )
        print(f"✅ WhatsApp message sent successfully! SID: {message.sid}")
    except Exception as e:
        print(f"❌ Failed to send WhatsApp message. Error: {e}")