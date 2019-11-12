import sys
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import tkinter
from tkinter import font


def receive():
    while True:
        try:
            msg = client_socket.recv(BUFSIZ).decode("utf8")
            message_lists.insert(tkinter.END, msg)
            message_lists.see(tkinter.END)
        except OSError:
            break


def send(event=None):
    try:
        msg = my_message.get()
        my_message.set("")
        client_socket.send(bytes(msg, "utf8"))
        if msg == "{quit}":
            client_socket.close()
            top.quit()

    except ConnectionResetError:
        msg = "Server has been shut down. You may close this window."
        message_lists.insert(tkinter.END, msg)
        message_lists.see(tkinter.END)


def on_closing(event=None):
    my_message.set("{quit}")
    send()
    top.quit()


HOST = input("Enter Server IP Address = ")
print("Enter PORT number. Leave blank if you dont know the port number.")
try:
    PORT = input("-> ")
    if not PORT:
        PORT = 33000
    else:
        PORT = int(PORT)
except ValueError:
    print("Port should be a number.")
    sys.exit()

BUFSIZ = 1024
ADDR = (HOST, PORT)

client_socket = socket(AF_INET, SOCK_STREAM)
try:
    client_socket.connect(ADDR)
except ConnectionRefusedError:
    print("Cant connect to server.")
    sys.exit()
except TimeoutError:
    print("A connection attempt failed because the connected party did not properly respond after a period of time.")
    sys.exit()
except Exception as e:
    print(e)
    sys.exit()

top = tkinter.Tk()
top.title("Chat Room")

framee = tkinter.Frame(top)
my_message = tkinter.StringVar()
my_message.set("")
scrollbar = tkinter.Scrollbar(framee)
small_font = font.Font(size=10)
message_lists = tkinter.Listbox(framee, height=20, width=70, yscrollcommand=scrollbar.set, font=small_font)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
message_lists.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
message_lists.pack()
framee.pack()

fields = tkinter.Entry(top, textvariable=my_message)
fields.bind("<Return>", send)
fields.pack()
send_button = tkinter.Button(top, text="Send", command=send)
send_button.pack()

top.protocol("WM_DELETE_WINDOW", on_closing)

receive_thread = Thread(target=receive)
receive_thread.start()
tkinter.mainloop()
