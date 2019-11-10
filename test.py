# socket.gaierror
#
# OSError: [WinError 10049] The requested address is not valid in its context

import socket

s = socket.socket()
host = "192.168.0.155"
port = 5000
s.connect((host, port))
# s.settimeout(3)
