from threading import Thread
import socket
from time import sleep


def ss():
    amm = 0
    while True:
        aaa = s.recv(1024)
        b = aaa.decode()
        print(b)
        if b != "":
            print(b)
            b = aaa.decode().split("/")
            filename = str(b[-1])
            file = open(filename, 'wb')
            file_data = s.recv(40960000)
            file.write(file_data)
            file.close()
            print("File has been received successfully.")
            amm += 1
            if file_data:
                break
            if amm > 10:
                break


global s
s = socket.socket()
host = "192.168.0.107"
port = 5000
s.connect((host, port))
print("Connected ... ")
t = Thread(target=ss)
t.start()
