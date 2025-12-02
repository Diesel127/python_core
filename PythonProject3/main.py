import socket

def main():
    # Параметры сервера
    server_host = '127.0.0.1'  # Адрес сервера (localhost)
    server_port = 12345        # Порт сервера

    # Создание сокета-клиента
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Подключение к серверу
        client_socket.connect((server_host, server_port))
        print(f'Подключен к серверу {server_host}:{server_port}')

        # Сообщение для отправки серверу
        message = 'Привет, сервер!'
        client_socket.sendall(message.encode('utf-8'))
        print(f'Сообщение отправлено: {message}')

        # Получение ответа от сервера
        response = client_socket.recv(1024).decode('utf-8')
        print(f'Ответ от сервера: {response}')

    except socket.error as e:
        print(f'Ошибка сокета: {e}')

    finally:
        # Закрытие сокета
        client_socket.close()
        print('Соединение закрыто')

main()