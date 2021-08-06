#Скрипт для клієнта чату Tkinter GUI.
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import tkinter


def receive():
    """Обробляє отримання повідомлень."""
    while True:
        try:
            msg = client_socket.recv(BUFSIZ).decode("utf8")
            msg_list.insert(tkinter.END, msg)
        except OSError:  # Можливо, клієнт залишив чат. 
            break


def send(event=None):  # подія передається зв'язуючим.
    """Ручна передача повідмлень."""
    msg = my_msg.get()
    my_msg.set("")  # Очищає поле введення.
    client_socket.send(bytes(msg, "utf8"))
    if msg == "{quit}":
        client_socket.close()
        top.quit()


def on_closing(event=None):
    """Цю функцію потрібно викликати, коли вікно закрите."""
    my_msg.set("{quit}")
    send()

top = tkinter.Tk()
top.title("Чат")

messages_frame = tkinter.Frame(top)
my_msg = tkinter.StringVar()  # Для надсилання повідомлень. Слідкування за змінною змінних у tkinter
my_msg.set("Ваш нік")
scrollbar = tkinter.Scrollbar(messages_frame)  # Для переміщення по минулих повідомленнях. 
# Нижче наведено повідомлення.
msg_list = tkinter.Listbox(messages_frame, height=15, width=50, yscrollcommand=scrollbar.set) # Ліст повідомлень
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y) # Прикріплюємо області
msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
msg_list.pack()
messages_frame.pack()

entry_field = tkinter.Entry(top, textvariable=my_msg) # встановлює прив'язку до елементу StringVar
entry_field.bind("<Return>", send)
entry_field.pack()
send_button = tkinter.Button(top, text="Надіслати", command=send)
send_button.pack()

top.protocol("WM_DELETE_WINDOW", on_closing) # події та функцію. обробник закриття вікна

#----Тепер приходить частина sockets----
HOST = input('Введіть адрес: ')
PORT = input('Введіть порт: ')
if not PORT:
    PORT = 27015
else:
    PORT = int(PORT)

BUFSIZ = 1024
ADDR = (HOST, PORT)

client_socket = socket(AF_INET, SOCK_STREAM) # для сетевого протокола IPv4. надійна потоків орієнтована служба (сервіс) або потоковий сокет
client_socket.connect(ADDR) # Підключення по адресу

receive_thread = Thread(target=receive)
receive_thread.start()
tkinter.mainloop()  # Починає виконання графічного інтерфейсу.
