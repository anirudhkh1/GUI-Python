import pickle
from tkinter import *
from tkinter import messagebox

global room_data
f = open("auro_database", "rb")
room_data = pickle.load(f)
f.close()


def room_service():
    def abc():
        a = str(listbox.selection_get())
        b = a.split()
        room_data[b[2]][b[-1][1:-1]].remove(b[-2])
        f = open("auro_database", "wb")
        pickle.dump(room_data, f)
        f.close()
        listbox.delete(ACTIVE)

    room_service_check = Toplevel(user_home)
    room_service_check.geometry("400x400")
    Label(room_service_check, text="Auro Hotels", bg="black", fg="white", width="200", height="2",
          font=("Arial Bold", 13)).pack()
    scrollbar = Scrollbar(room_service_check, orient=VERTICAL)
    listbox = Listbox(room_service_check, yscrollcommand=scrollbar.set, selectmode=SINGLE, width=55, height=20)
    scrollbar.config(command=listbox.yview)
    b = Button(room_service_check, text="Completed", width=10, height=2, bg="black", fg="white", command=abc)
    b.pack(side=RIGHT)

    scrollbar.pack(side=RIGHT, fill=Y)
    listbox.pack(side=LEFT)

    for i in room_data.keys():
        a = room_data[i]["Service"]
        b = room_data[i]["Food"]
        if len(a):
            for j in a:
                item = "Room No- " + str(i) + " --> " + str(j) + " (Service)"
                listbox.insert(END, item)
        # if len(b):
        #     for j in b:
        #         item = "Room No- " + str(i) + " --> " + str(j) + " (Food)"
        #         listbox.insert(END, item)


def order_food():
    def abc():
        a = str(listbox.selection_get())
        b = a.split()
        room_data[b[2]][b[-1][1:-1]].remove(b[-2])
        f = open("auro_database", "wb")
        pickle.dump(room_data, f)
        f.close()
        listbox.delete(ACTIVE)

    room_service_check = Toplevel(user_home)
    room_service_check.geometry("400x400")
    Label(room_service_check, text="Auro Hotels", bg="black", fg="white", width="200", height="2",
          font=("Arial Bold", 13)).pack()
    scrollbar = Scrollbar(room_service_check, orient=VERTICAL)
    listbox = Listbox(room_service_check, yscrollcommand=scrollbar.set, selectmode=SINGLE, width=55, height=20)
    scrollbar.config(command=listbox.yview)
    b = Button(room_service_check, text="Completed", width=10, height=2, bg="black", fg="white", command=abc)
    b.pack(side=RIGHT)

    scrollbar.pack(side=RIGHT, fill=Y)
    listbox.pack(side=LEFT)

    for i in room_data.keys():
        a = room_data[i]["Service"]
        b = room_data[i]["Food"]
        # if len(a):
        #     for j in a:
        #         item = "Room No- " + str(i) + " --> " + str(j) + " (Service)"
        #         listbox.insert(END, item)
        if len(b):
            for j in b:
                item = "Room No- " + str(i) + " --> " + str(j) + " (Food)"
                listbox.insert(END, item)


def bb():
    global user_home
    try:
        user_home.deiconify()
    except:
        pass
    admin_login_screen.withdraw()
    user_home = Toplevel(admin_login_screen)
    user_home.title("Auro Service")
    user_home.geometry("300x250")
    Label(user_home, text="Select Your Service", bg="black", fg="white", width="200", height="2",
          font=("Arial Bold", 13)).pack()
    Label(user_home, text="").pack()
    Button(user_home, text="Room Service", width=20, height=2, font=("Arial", 12), command=room_service).pack()
    Label(user_home, text="").pack()
    Button(user_home, text="Food Service", width=20, height=2, font=("Arial", 12), command=order_food).pack()

    def on_close():
        user_home.destroy()
        admin_login_screen.deiconify()

    user_home.protocol("WM_DELETE_WINDOW", on_close)


def login():
    global admin_login_screen
    admin_login_screen = Tk()
    admin_login_screen.title("Admin Login")
    admin_login_screen.geometry("300x250")
    Label(admin_login_screen, text="Enter Admin details.", bg="black", fg="white", width="300", height="2",
          font=("Calibri", 13)).pack()
    Label(admin_login_screen, text="").pack()
    Label(admin_login_screen, text="Username ").pack()
    u = StringVar()
    admin_username_login_entry = Entry(admin_login_screen, textvariable=u)
    admin_username_login_entry.pack()
    admin_username_login_entry.focus_set()
    uu = StringVar()
    Label(admin_login_screen, text="").pack()
    Label(admin_login_screen, text="Password ").pack()
    admin_password_login_entry = Entry(admin_login_screen, show='*', textvariable=uu)
    admin_password_login_entry.pack()
    Label(admin_login_screen, text="").pack()

    def bbb():
        if u.get() == "ani" and uu.get() == "ani":
            bb()
        else:
            messagebox.showerror("Error!", "Wrong Password")

    b1 = Button(admin_login_screen, text="Login", width=15, height=1, bg="black", fg="white", command=bbb)
    b1.pack()
    admin_login_screen.bind('<Return>', lambda event=None: b1.invoke())
    admin_login_screen.mainloop()


print(room_data)
login()
