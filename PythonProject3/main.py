import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Настройки
smtp_server = 'smtp.example.com'
smtp_port = 587
username = 'your_email@example.com'
password = 'your_password'
from_email = 'your_email@example.com'
to_email = 'recipient@example.com'
subject = 'Тема письма'
body = 'Это тело письма'

# Создание сообщения
msg = MIMEMultipart()
msg['From'] = from_email
msg['To'] = to_email
msg['Subject'] = subject
msg.attach(MIMEText(body, 'plain'))
server = None

# Подключение к SMTP-серверу и отправка письма
try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  # Установим соединение TLS
    server.login(username, password)
    server.sendmail(from_email, to_email, msg.as_string())
    print("Письмо успешно отправлено")
except Exception as e:
    print(f"Ошибка при отправке письма: {e}")
finally:
    if server:
        server.quit()