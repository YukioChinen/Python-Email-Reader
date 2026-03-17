# Python Email Reader
## Descrição
Uma aplicação Python para ler e processar emails de servidores IMAP e classificar baseado no domínio do email do remetente.

## Funcionalidades
- Conectar a contas de email via IMAP
- Separar o domínio do remetente
- Criar um marcador baseado no domínio
- Salvar o email correspondente ao domínio

## Versão 2
### O que foi mudado
- Adicionado um bot do Telegram.
- O bot envia para o seu usuário o total de emails categorizados.
- O bot também envia os marcadores que foram criados durante a categorização.

### Exemplo de mensagem que chega
```text
📬 Emails organizados:

blizzard: 2
google: 9
instagram: 5

Total: 16
```

## Requisitos
- Python 3.7+
- python-dotenv
- imbox

## Instalação
```bash
git clone https://github.com/seu-usuario/Python-Email-Reader.git
cd Python-Email-Reader
pip install -r requirements.txt
```

## Uso
```bash
python main.py
```

Ou importar a função diretamente:
```python
from src.email_reader import read_emails

read_emails()
```

## Configuração
Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:

```env
EMAIL_USER=seu_email@gmail.com
EMAIL_PASSWORD=sua_senha_ou_app_password
HOST=imap.gmail.com
TELEGRAM_TOKEN=seu_token_do_bot
CHAT_ID=seu_chat_id
```

### Como conseguir TELEGRAM_TOKEN
1. No Telegram, procure por `@BotFather`.
2. Envie o comando `/newbot` e siga as instruções para criar o bot.
3. Ao final, o BotFather vai retornar um token no formato `123456789:ABC...`.
4. Copie esse valor e use em `TELEGRAM_TOKEN`.

### Como conseguir CHAT_ID
1. Envie uma mensagem para o seu bot (por exemplo: `oi`).
2. No navegador, abra:
	`https://api.telegram.org/botSEU_TELEGRAM_TOKEN/getUpdates`
3. No JSON retornado, procure por `chat` e depois por `id`.
4. Use esse número em `CHAT_ID`.

**Nota:** Para Gmail, recomenda-se usar [App Passwords](https://support.google.com/accounts/answer/185833) ao invés da senha principal.

## Autor
Enzo Yukio Chinen
