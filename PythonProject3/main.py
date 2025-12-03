import poplib
from email.parser import BytesParser
from email.policy import default

# Учётные данные для входа
username = 'yahoo.com'
password = 'password'

# Подключение к почтовому серверу Gmail
pop3_server = 'pop.mail.yahoo.com'
mailbox = poplib.POP3_SSL(pop3_server, 995)

# Вход в почтовый ящик
mailbox.user(username)
mailbox.pass_(password)  # Используем pass_ для предотвращения конфликта с ключевым словом pass в Python

num_messages = len(mailbox.list()[1])

# Если есть письма, получаем содержимое последнего
if num_messages > 0:
    response, lines, octets = mailbox.retr(num_messages)
    message_content = b'\r\n'.join(lines)

    # Парсинг письма
    message = BytesParser(policy=default).parsebytes(message_content)

    # Отображение содержимого последнего письма
    print(f"Subject: {message['subject']}")
    print(f"From: {message['from']}")
    print(f"To: {message['to']}")
    print(f"Date: {message['date']}")
    print("\nBody:\n")
    if message.is_multipart():
        for part in message.iter_parts():
            if part.get_content_type() == "text/plain":
                print(part.get_payload(decode=True).decode(part.get_content_charset()))
    else:
        print(message.get_payload(decode=True).decode(message.get_content_charset()))

# Закрытие соединения
mailbox.quit()