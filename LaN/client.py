from tkinter.filedialog import asksaveasfile
from threading import Thread
import socket
from time import sleep
from tkinter import *


def ss():
    global file_data
    global filename
    global b
    try:
        conn_label.destroy()
    except:
        pass
    Label(text="Connected.", font=("Arial Bold", 11), fg="black").place(x=145, y=130)
    amm = 0
    while True:
        aaa = s.recv(1024)
        b = aaa.decode()
        print(b)
        if b != "":
            print(b)
            b = aaa.decode().split("/")
            filename = str(b[-1])
            # file = open(filename, 'wb')
            file_data = s.recv(40960000)
            # file.write(file_data)
            # file.close()
            # print("File has been received successfully.")
            amm += 1
            if file_data:
                break
            if amm > 10:
                break
    Label(text="%s recived successfully" % (str(b[-1])), font=("Arial Bold", 11), fg="black").place(x=145, y=150)
    global save_file_button
    save_file_button = Button(text="Save File", width=15, height=1, bg="black", fg="white", command=save_file_location)
    save_file_button.place(x=145, y=180)


def save_file_location():
    files = [("Custom File", '*.' + str(filename.split(".")[-1])),
             ('All Files', '*.*')]
    file = asksaveasfile(filetypes=files, defaultextension=files)
    if file.name == "":
        Label(root, text="Enter file name.", fg="red", font=("Arial", 12)).place(x=130, y=210)
    ff = open(str(file.name), 'wb')
    ff.write(file_data)
    file.close()
    save_file_button.destroy()
    print(file.name)
    aa = str(file.name).split("/")
    Label(root, text="File saved as %s" % (aa[-1]), font=("Arial", 12)).place(x=130, y=180)


def conn_to_server():
    global s
    s = socket.socket()
    host = str(aa.get())
    print(host)
    port = 6000
    global t_error
    try:
        global conn_label
        try:
            conn_label.destroy()
        except:
            pass
        conn_label = Label(text="Connecting to server...", font=("Arial Bold", 11))
        conn_label.place(x=145, y=130)
        s.connect((host, port))

    except TimeoutError:
        print("In exception")
        root.after(1, conn_label.destroy())
        conn_label = Label(text="Host failed to respond.", font=("Arial", 11), fg="red")
        conn_label.place(x=145, y=130)

    except socket.gaierror:
        root.after(1, conn_label.destroy())
        conn_label = Label(text="Bad Address.", font=("Arial", 11), fg="red")
        conn_label.place(x=145, y=130)

    except OSError:
        root.after(1, conn_label.destroy())
        conn_label = Label(text="Bad Address.", font=("Arial", 11), fg="red")
        conn_label.place(x=145, y=130)

    except Exception as e:
        root.after(1, conn_label.destroy())
        conn_label = Label(text="%s" % (e), font=("Arial", 11), fg="red")
        conn_label.place(x=145, y=130)
    else:
        ss()


def t():
    tt = Thread(target=conn_to_server)
    tt.start()


global root
global server_ip
root = Tk()
root.title("File Transfer")
root.geometry("450x400")
Label(text="LAN File Transfer", bg="black", fg="white", width="300", height="2", font=("Calibri", 13)).pack()
server_ip_label = Label(root, text="Enter server IP: ", font=("Arial Bold", 13)).place(x=16, y=60)
aa = StringVar()
b = Entry(root, textvariable=aa, font=("Arial", 13),width="25")
b.place(x=150, y=60)
con_s = Button(text="Connect to server", width=15, height=1, bg="black", fg="white",
               command=t)
con_s.place(x=150, y=90)
root.bind('<Return>', lambda event=None: con_s.invoke())

root.mainloop()
