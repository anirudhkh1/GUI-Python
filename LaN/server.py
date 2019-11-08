import tkinter
from tkinter import filedialog
from tkinter import *
import os
import socket


def search_for_file_path():
    currdir = os.getcwd()
    tempdir = filedialog.askopenfilename(filetypes=(("All files", "*"), ("Template files", "*.type")))
    if len(tempdir) > 0:
        print("You chose: %s" % tempdir)
    return tempdir


def hostip():
    global conn
    global s
    global host
    global port
    global addr
    s = socket.socket()
    host = socket.gethostname()
    port = 5000
    s.bind((host, port))
    s.listen(1)
    conn, addr = s.accept()
    print(addr, "Has connected to the server")


ch = input("Press Enter to select file.")
root = tkinter.Tk()
root.title("File transter")
root.geometry("400x250")
Label(root, text="Hostname:",font=("Arial Bold", 13)).grid(row=0, column=0)
# root.withdraw()
filename = search_for_file_path()
conn.send(str(filename).encode())
file = open(filename, 'rb')
file_data = file.read(40960000)
conn.send(file_data)
print("Data has been transmitted successfully")
