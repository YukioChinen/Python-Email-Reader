# Python Email Reader
## Descrição
Uma aplicação Python para ler e processar emails de servidores IMAP.

## Funcionalidades
- Conectar a contas de email via IMAP
- Ler emails da caixa de entrada
- Analisar conteúdo de emails e anexos
- Interface de linha de comando simples

## Requisitos
- Python 3.7+
- imaplib
- email
- ssl

## Instalação
```bash
git clone https://github.com/seunome/Python-Email-Reader.git
cd Python-Email-Reader
pip install -r requirements.txt
```

## Uso
```python
from email_reader import EmailReader

reader = EmailReader(email, password, imap_server)
emails = reader.fetch_emails()
```

## Configuração
Atualize suas credenciais de email em `config.py` ou passe-as como argumentos.

## Autor
Enzo Yukio Chinen
