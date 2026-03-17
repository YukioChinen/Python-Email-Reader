import requests
import os

def send_telegram(message):
    token = os.getenv("TELEGRAM_TOKEN")
    chat_id = os.getenv("CHAT_ID")

    url = f"https://api.telegram.org/bot{token}/sendMessage"

    requests.post(url, data={
        "chat_id": chat_id,
        "text": message
    })

def build_summary_message(category_count, total):

    message = "📬 Emails organizados:\n\n"

    for category, count in category_count.items():
        message += f"{category}: {count}\n"

    message += f"\nTotal: {total}"

    return message