#Сервер для багатопотокового (асинхронного) додатку чату.
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread


def accept_incoming_connections():
    #Встановлює обробку для вхідних клієнтів.
    while True:
        client, client_address = SERVER.accept()# повертає новий сокет та адрес клієнта
        print("%s:%s підключився." % client_address)  # Виводим його
        client.send(bytes("Ви підєдналися до чату", "utf8")) # відправляєм повідомлення
        addresses[client] = client_address # зберігаєм адрес нового клієнта
        Thread(target=handle_client, args=(client,)).start() # додаємо новий потік для клієнта


def handle_client(client):  # Приймає сокет клієнта як аргумент.
    #Обробляєм з'єднання одного клієнта.
    name = client.recv(BUFSIZ).decode("utf8")
    welcome = 'Ласкаво просимо %s!' % name
    client.send(bytes(welcome, "utf8"))
    msg = "%s приєднався до чату!" % name
    broadcast(bytes(msg, "utf8"))
    clients[client] = name

    while True:
        msg = client.recv(BUFSIZ)
        broadcast(msg, name+": ")


def broadcast(msg, prefix=""):  # префікс для ідентифікації імені.
    #Передає повідомлення всім клієнтам.

    for sock in clients:
        sock.send(bytes(prefix, "utf8")+msg)

        
clients = {}
addresses = {}

HOST = ''
PORT = 27015
BUFSIZ = 1024 # для декодування
ADDR = (HOST, PORT) # адрес

SERVER = socket(AF_INET, SOCK_STREAM) # для сетевого протокола IPv4. надійна потоків орієнтована служба (сервіс) або потоковий сокет
SERVER.bind(ADDR) # Додаєм наш адрес

SERVER.listen(5) # коли підєднується клієнт ?
print("Очікування з'єднання...")
ACCEPT_THREAD = Thread(target=accept_incoming_connections) # паралельність
ACCEPT_THREAD.start()
