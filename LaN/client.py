import socket

s = socket.socket()
host = "192.168.46.174"
port = 5000
s.connect((host, port))
print("Connected ... ")
aaa = s.recv(1024)
b = aaa.decode().split("/")
filename = str(b[-1])
file = open(filename, 'wb')
file_data = s.recv(40960000)
file.write(file_data)
file.close()
print("File has been received successfully.")
