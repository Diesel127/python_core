import poplib

# Учётные данные для входа
username = 'bykdenis@yahoo.com'
password = 'password'

# Подключение к почтовому серверу Gmail
pop3_server = 'pop.mail.yahoo.com'
mailbox = poplib.POP3_SSL(pop3_server, 995)

# Вход в почтовый ящик
mailbox.user(username)
mailbox.pass_(password)  # Используем pass_ для предотвращения конфликта с ключевым словом pass в Python

# Получение информации о почтовом ящике
num_messages = len(mailbox.list()[1])
print(f"Количество писем: {num_messages}")

# Пример: Чтение последнего письма
if num_messages > 0:
    response, lines, octets = mailbox.retr(num_messages)
    message = '\n'.join(line.decode('utf-8') for line in lines)
    print("Содержимое последнего письма:")
    print(message)

# Закрытие соединения
mailbox.quit()