from threading import Thread
import tkinter
from tkinter import filedialog
from tkinter import *
from tkinter import messagebox
import os
import socket


def confirm():
    def conf1():
        MsgBox = messagebox.askquestion('Confirm', 'Do you want to start the server and send %s ?' % (str(tempdir)),
                                        icon='warning')
        if MsgBox == 'yes':
            send()
        else:
            messagebox.showinfo('Return', 'You will now return to the application screen')

    cof = Button(root, text="Send file", height=1, width=12, fg="white", bg="black", command=conf1)
    cof.place(x=120, y=180)


def send3():
    try:
        s.bind((hostt, port))
        s.listen(10)
        conn, addr = s.accept()
        root.after(1, ww1.destroy())
        root.after(1, ww.destroy())
        ip_con = Label(root, text="%s connected." % (addr[0]), font=("Arial", 13))
        ip_con.place(x=40, y=230)
        filename = tempdir
        ff = tempdir.split("/")
        conn.send(str(ff[-1]).encode())
        file = open(filename, 'rb')
        file_data = file.read(40960000)
        conn.send(file_data)
        conn.close()
        send_done = Label(root, text="File send successfully.", font=("Arial", 13))
        send_done.place(x=40, y=255)
    except Exception as e:
        print(e)


def send2():
    global ww
    global ww1
    ww1 = Label(root, text="Server Started", font=("Arial", 13))
    ww1.place(x=40, y=230)
    ww = Label(root, text="Waiting for Incoming Connections", font=("Arial", 13))
    ww.place(x=40, y=250)
    send3()


def send():
    t = Thread(target=send2)
    try:
        t.start()
    except Exception as e:
        print(e)


def search_for_file_path():
    global tempdir
    currdir = os.getcwd()
    tempdir = filedialog.askopenfilename(filetypes=(("All files", "*"), ("Template files", "*.type")))
    if len(tempdir) > 0:
        print("You chose: %s" % tempdir)
    b = tempdir.split("/")
    if b[-1] != "":
        file_name = Label(root, text="%s" % (b[-1]), font=("Arial Bold", 10))
        file_name.place(x=230, y=140)
        confirm()
    else:
        file_name = Label(root, text="No File Selected", fg='red')
        file_name.place(x=230, y=140)


def ask_for_file():
    pass
    # select_file = Label(root, text="Select File: ", font=("Arial Bold", 12))
    # select_file.place(x=40, y=180)
    # file_name = StringVar()
    # sel_but = Button(root, text="Browse", height=1, width=8, fg="white", font=("Arial", 10), bg="black",
    #                  command=search_for_file_path)
    # sel_but.place(x=130, y=180)


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


hostip()
global root
global start_button
root = tkinter.Tk()
root.title("File transter")
root.geometry("350x300")
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
start_button = Button(root, text="Select File", width=12, height=1, bg="black", fg="white",
                      command=search_for_file_path)
start_button.place(x=120, y=140)
root.mainloop()
