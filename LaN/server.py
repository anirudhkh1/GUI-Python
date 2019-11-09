from threading import Thread
import tkinter
from tkinter import filedialog
from tkinter import *
from tkinter import messagebox
import os
import socket


def search_for_file_path():
    global tempdir
    currdir = os.getcwd()
    tempdir = filedialog.askopenfilename(filetypes=(("All files", "*"), ("Template files", "*.type")))
    if len(tempdir) > 0:
        print("You chose: %s" % tempdir)
    confirm()


def hostip():
    global conn
    global s
    global host
    global port
    global addr
    global hostt
    s = socket.socket()
    host = socket.gethostname()
    hostt = socket.gethostbyname(host)
    port = 5000


def send():
    flag = "1"
    conn.send(flag.encode())
    filename = tempdir
    ff = tempdir.split("/")
    conn.send(str(ff[-1]).encode())
    file = open(filename, 'rb')
    file_data = file.read(40960000)
    conn.send(file_data)
    print("Data has been transmitted successfully")


def confirm():
    def conf1():
        MsgBox = messagebox.askquestion('Confirm', 'Do you want to start the server and send %s ?' % (str(tempdir)),
                                        icon='warning')
        if MsgBox == 'yes':
            send()
        else:
            messagebox.showinfo('Return', 'You will now return to the application screen')

    cof = Button(root, text="Send", height=1, width=8, fg="white", font=("Arial", 10), bg="black", command=conf1)
    cof.place(x=130, y=220)


def wait_for_connection():
    try:
        s.bind((hostt, port))
        s.listen(10)
        conn, addr = s.accept()
        print(addr, "Has connected to the server")
        root.after(1, ww.destroy())
        conn = Label(root, text="%s has connected." % (str(addr[0])), font=("Arial", 13))
        conn.place(x=40, y=140)
        select_file = Label(root, text="Select File: ", font=("Arial Bold", 12))
        select_file.place(x=40, y=180)
        file_name = StringVar()
        sel_but = Button(root, text="Browse", height=1, width=8, fg="white", font=("Arial", 10), bg="black",
                         command=search_for_file_path)
        sel_but.place(x=130, y=180)

    except Exception as e:
        print(e)


def startserver():
    root.after(1, start_button.destroy())
    global ww
    ww = Label(root, text="Waiting for Incoming Connections", font=("Arial", 13))
    ww.place(x=40, y=140)
    global t
    t = Thread(target=wait_for_connection)
    try:
        t.start()
    except Exception as e:
        print(e)


# ch = input("Press Enter to select file.")
hostip()
global root
global start_button
root = tkinter.Tk()
root.title("File transter")
root.geometry("330x300")
Label(text="LAN File Transfer", bg="black", fg="white", width="300", height="2", font=("Calibri", 13)).pack()
Label(root, text="Hostname:", font=("Arial Bold", 13)).place(x=16, y=60)
aa = StringVar()
b = Entry(root, textvariable=aa, font=("Arial", 13), state="disabled")
aa.set(host)
b.place(x=120, y=60)
Label(root, text="IP Address:", font=("Arial Bold", 13)).place(x=10, y=100)
aaa = StringVar()
bb = Entry(root, textvariable=aaa, font=("Arial", 13), state="disabled")
aaa.set(socket.gethostbyname(host))
bb.place(x=120, y=100)
start_button = Button(root, text="Start Server", width=12, height=1, bg="black", fg="white", command=startserver)
start_button.place(x=120, y=140)
root.mainloop()
