from src.email_reader import read_emails
from src.send_telegram import send_telegram, build_summary_message

def main():
    print("Iniciando leitura de emails...")
    category_count, total = read_emails()

    message = build_summary_message(category_count, total)
    send_telegram(message)

    print("Processo finalizado.")


if __name__ == "__main__":
    main()