import socket
s = socket.socket()
host = "192.168.46.174"
port = 5000
s.connect((host,port))
print("Connected ... ")

filename = input(str("Konse naam se file save karna chathe ho? -> "))
file = open(filename, 'wb')
file_data = s.recv(1024)
file.write(file_data)
file.close()
print("File has been received successfully.")