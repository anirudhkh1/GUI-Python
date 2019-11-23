from tkinter import messagebox
import pickle
import tkinter
from tkinter import *


def contact_uss():
    global contact_screen
    contact_screen = Toplevel(user_home)
    contact_screen.geometry("300x200")
    contact_screen.title("Contact Us")
    Label(contact_screen, text="Contact Us", bg="black", fg="white", width="200", height="2",
          font=("Arial Bold", 13)).pack()
    Label(contact_screen, text="").pack()
    Label(contact_screen, text="Reception : 223", font=("Arial", 12)).pack()
    Label(contact_screen, text="").pack()
    Label(contact_screen, text="Restaurant : 224", font=("Arial 12")).pack()
    Label(contact_screen, text="").pack()
    Label(contact_screen, text="Room Service : 234", font=("Arial 12")).pack()
    Label(contact_screen, text="").pack()


def order_food():
    global food_screen
    food_screen = Toplevel(user_home)
    food_screen.geometry("350x390")
    food_screen.title("Food Ordering")
    Label(food_screen, text="Order Food", bg="black", fg="white", width="200", height="2",
          font=("Arial Bold", 14)).pack()

    def sub():
        rm = room_no.get()
        room_data[rm]["Food"] = []
        if cookie.get():
            room_data[rm]["Food"].append("Cookies")
        if sandwich.get():
            room_data[rm]["Food"].append("Sandwich")
        if nachos.get():
            room_data[rm]["Food"].append("Nachos")
        if paneer_tikka.get():
            room_data[rm]["Food"].append("PaneerTikka")
        if chicken_tikka.get():
            room_data[rm]["Food"].append("ChickenTikka")
        if spring_roll.get():
            room_data[rm]["Food"].append("SpringRolls")
        if long_iceland.get():
            room_data[rm]["Food"].append("LongIceland")
        if manhattan.get():
            room_data[rm]["Food"].append("Manhattan")
        if blue_lagoon.get():
            room_data[rm]["Food"].append("BlueLagoon")
        if paneer_masala.get():
            room_data[rm]["Food"].append("PaneeMasala")
        if chicken_masala.get():
            room_data[rm]["Food"].append("ChickenMasala")
        if veg_kofta.get():
            room_data[rm]["Food"].append("Veg.Kofta")
        f = open("auro_database", "wb")
        pickle.dump(room_data, f)
        f.close()
        print(room_data)
        messagebox.showinfo("Success", "Your Order has been placed.")
        food_screen.destroy()

    cookie = IntVar()
    sandwich = IntVar()
    nachos = IntVar()
    paneer_tikka = IntVar()
    chicken_tikka = IntVar()
    spring_roll = IntVar()
    long_iceland = IntVar()
    manhattan = IntVar()
    blue_lagoon = IntVar()
    paneer_masala = IntVar()
    chicken_masala = IntVar()
    veg_kofta = IntVar()
    Label(food_screen, text="Snacks", font=("Arial Bold", 14)).place(x=30, y=60)
    Checkbutton(food_screen, text="Cookies", variable=cookie, font=("Arial 12")).place(x=15, y=90)
    Checkbutton(food_screen, text="Sandwich", variable=sandwich, font=("Arial 12")).place(x=15, y=120)
    Checkbutton(food_screen, text="Nachos", variable=nachos, font=("Arial 12")).place(x=15, y=150)
    Label(food_screen, text="Starters", font=("Arial Bold", 14)).place(x=30, y=200)
    Checkbutton(food_screen, text="Paneer Tikka", variable=paneer_tikka, font=("Arial 12")).place(x=15, y=230)
    Checkbutton(food_screen, text="Chicken Tikka", variable=chicken_tikka, font=("Arial 12")).place(x=15, y=260)
    Checkbutton(food_screen, text="Spring Roll", variable=spring_roll, font=("Arial 12")).place(x=15, y=290)
    Label(food_screen, text="Cocktails", font=("Arial Bold", 14)).place(x=215, y=60)
    Checkbutton(food_screen, text="Long Iceland", variable=long_iceland, font=("Arial 12")).place(x=200, y=90)
    Checkbutton(food_screen, text="Manhattan", variable=manhattan, font=("Arial 12")).place(x=200, y=120)
    Checkbutton(food_screen, text="Blue Lagoon", variable=blue_lagoon, font=("Arial 12")).place(x=200, y=150)
    Label(food_screen, text="Main Course", font=("Arial Bold", 14)).place(x=215, y=200)
    Checkbutton(food_screen, text="Paneer Masala", variable=paneer_masala, font=("Arial 12")).place(x=200, y=230)
    Checkbutton(food_screen, text="Chicken Masala", variable=chicken_masala, font=("Arial 12")).place(x=200, y=260)
    Checkbutton(food_screen, text="Veg. Kofta", variable=veg_kofta, font=("Arial 12")).place(x=200, y=290)
    Button(food_screen, text="Submit", font=("Arial 12"), bg="black", fg="white", command=sub, height=1).place(
        x=140, y=340)


def room_service():
    global room_service_home
    room_service_home = Toplevel(user_home)
    room_service_home.geometry("300x310")
    room_service_home.title("Room Service")
    Label(room_service_home, text="Room Service", bg="black", fg="white", width="200", height="2",
          font=("Arial Bold", 14)).pack()
    Label(room_service_home, text="").pack()
    Label(room_service_home, text="Check on the services you need.", font=("Arial 13")).pack()
    cleaning = IntVar()
    Checkbutton(room_service_home, text="Cleaning", variable=cleaning, font=("Arial 12")).place(x=110, y=100)
    laundary = IntVar()
    Checkbutton(room_service_home, text="Laundary", variable=laundary, font=("Arial 12")).place(x=110, y=130)
    bathroom_kit = IntVar()
    Checkbutton(room_service_home, text="Bathroom Kit", variable=bathroom_kit, font=("Arial 12")).place(x=110, y=160)
    room_kit = IntVar()
    Checkbutton(room_service_home, text="Room Kit", variable=room_kit, font=("Arial 12")).place(x=110, y=190)
    towel = IntVar()
    Checkbutton(room_service_home, text="Towel", variable=towel, font=("Arial 12")).place(x=110, y=220)

    def printt():
        rm = room_no.get()
        c = cleaning.get()
        l = laundary.get()
        b = bathroom_kit.get()
        r = room_kit.get()
        t = towel.get()
        room_data[rm]["Service"] = []
        if c:
            room_data[rm]["Service"].append("Cleaning")
        if l:
            room_data[rm]["Service"].append("Laundary")
        if b:
            room_data[rm]["Service"].append("BathroomKit")
        if r:
            room_data[rm]["Service"].append("RoomKit")
        if t:
            room_data[rm]["Service"].append("Towel")
        f = open("auro_database", "wb")
        pickle.dump(room_data, f)
        f.close()
        print(room_data)
        messagebox.showinfo("Success", "Room Services Updated.")
        room_service_home.destroy()

    Button(room_service_home, text="Submit", font=("Arial 12"), bg="black", fg="white", command=printt, height=1).place(
        x=120, y=260)


def user_home():
    global user_home
    try:
        user_home.deiconify()
    except:
        pass
    root.withdraw()
    user_home = Toplevel(root)
    user_home.title("Auro Service")
    user_home.geometry("300x250")
    Label(user_home, text="Select Your Service", bg="black", fg="white", width="200", height="2",
          font=("Arial Bold", 13)).pack()
    Label(user_home, text="").pack()
    Button(user_home, text="Room Service", width=20, height=2, font=("Arial", 12), command=room_service).pack()
    Label(user_home, text="").pack()
    Button(user_home, text="Food Service", width=20, height=2, font=("Arial", 12), command=order_food).pack()
    bb = Button(user_home, text="Contact Us", width=9, height=1, font=("Arial", 10), command=contact_uss)
    bb.place(x=190, y=200)

    def on_close():
        user_home.destroy()
        root.deiconify()

    user_home.protocol("WM_DELETE_WINDOW", on_close)


def check_room():
    n = room_no.get()
    if n == "":
        messagebox.showerror("Error", "Invalid Format")
    else:
        if n not in room_data.keys():
            room_data[n] = {"Service": [], "Food": []}
        f = open("auro_database", "wb")
        pickle.dump(room_data, f)
        f.close()
        user_home()


def user_room_enter():
    global root
    global room_data
    try:
        f = open("auro_database", "rb")
        room_data = pickle.load(f)
        f.close()
    except FileNotFoundError:
        room_data = {}
    print(room_data)
    root = Tk()
    root.geometry("300x200")
    root.title("Auro Hotels")
    Label(root, text="Auro Hotels", bg="black", fg="white", width="200", height="2", font=("Arial Bold", 13)).pack()
    Label(root, text="").pack()
    Label(root, text="Type your room number", font=("Arial", 12)).pack()
    Label(root, text="").pack()
    global room_no
    room_no = StringVar()
    a = Entry(root, textvariable=room_no)
    a.pack()
    a.focus_set()
    Label(root, text="").pack()
    room_submit = Button(text="Submit", height="1", width="10", fg="white", bg="black", command=check_room)
    room_submit.pack()
    root.bind('<Return>', lambda event=None: room_submit.invoke())
    root.mainloop()


user_room_enter()
