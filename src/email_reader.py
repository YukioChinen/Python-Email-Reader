from dotenv import load_dotenv
import os
from imbox import Imbox

load_dotenv()

email_user = os.getenv('EMAIL_USER')
email_password = os.getenv('EMAIL_PASSWORD')
host = os.getenv('HOST')

def read_emails():
    with Imbox(host, username=email_user, password=email_password) as imbox:
        unread_messages = imbox.messages(unread=True)

        for uid, message in unread_messages:
            sender = message.sent_from[0]['email']
            subject = message.subject

            body = ""
            if message.body['plain']:
                body = message.body['plain'][0]

            category = classify_email_by_domain(sender)

            print(f"From: {sender}")
            print(f"Subject: {subject}")
            print(f"Category: {category}")
            print("-" * 50)

            ensure_folder_exists(imbox, category)

            imbox.move(uid, category)
            imbox.mark_seen(uid)

def ensure_folder_exists(imbox, folder_name):
    status, folders = imbox.connection.list()

    folder_names = []

    for folder in folders:
        decoded = folder.decode()
        name = decoded.split(' "/" ')[-1]
        folder_names.append(name)

    if folder_name not in folder_names:
        imbox.connection.create(folder_name)
        print(f"Pasta criada: {folder_name}")

def classify_email_by_domain(sender_email):
    domain = sender_email.split("@")[-1].lower()
    parts = domain.split(".")

    if len(parts) >= 2:
        return parts[-2]

    return parts[0]