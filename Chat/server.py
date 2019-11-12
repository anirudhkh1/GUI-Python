from socket import AF_INET, SOCK_STREAM
from threading import Thread
import sys
import socket


def accept():
    while True:
        client, client_address = SERVER.accept()
        print("%s:%s has connected." % client_address)
        client.send(bytes("Welcome to %s! Now type your name and press enter!" % (server_name), "utf8"))
        addresses[client] = client_address
        Thread(target=cclient, args=(client,)).start()


def cclient(client):
    name = client.recv(BUFSIZ).decode("utf8")
    welcome = 'Welcome %s! If you ever want to quit, type {quit} to exit.' % name
    client.send(bytes(welcome, "utf8"))
    msg = "%s has joined the chat!" % name
    broadcast_to_all(bytes(msg, "utf8"))
    clients[client] = name

    while True:
        msg = client.recv(BUFSIZ)
        if msg != bytes("{quit}", "utf8"):
            broadcast_to_all(msg, name + ": ")
        else:
            del clients[client]
            # client.send(bytes("{quit}", "utf8"))
            aa = "%s has left the chat." % name
            broadcast_to_all(bytes(aa, "utf8"))
            # client.close()
            break


def broadcast_to_all(msg, prefix=""):
    for sock in clients:
        sock.send(bytes(prefix, "utf8") + msg)


clients = {}
addresses = {}

hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
print("Enter IP Address to host the server. Press ENTER to use default IP Address (%s)" % (IPAddr))
HOST = input("->")
if not HOST:
    HOST = str(IPAddr)

PORT = 33000
server_name = ""
while server_name == "":
    server_name = input("Enter the room name -> ")
    if server_name == "":
        print("Room name cannot be blank.")

BUFSIZ = 1024
ADDR = (HOST, PORT)

SERVER = socket.socket(AF_INET, SOCK_STREAM)
try:
    SERVER.bind(ADDR)
except Exception as e:
    print(e)
    sys.exit()

if __name__ == "__main__":
    SERVER.listen(6)
    print("\nServer IP Address = %s" % (HOST))
    print("Server PORT Number = %d" % (PORT))
    print("Room Name = %s" % (server_name))
    print("\nWaiting for connections...")
    accepting_thread = Thread(target=accept)
    accepting_thread.start()
    accepting_thread.join()
    SERVER.close()
