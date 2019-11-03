import math
import pickle
from tkinter import *
from tkcalendar import Calendar, DateEntry
import os

# Designing window for registration
users = {}
try:
    file = open("database", "rb")
    users = pickle.load(file)
    file.close()
except FileNotFoundError:
    users = {}

try:
    file = open("admin", "rb")
    admin = pickle.load(file)
    file.close()
except FileNotFoundError:
    admin = {"ani": "ani"}
    f = open("admin", "wb")
    pickle.dump(admin, f)
    f.close()


def example2():
    DOB_entry.delete(0, END)
    DOB_entry.insert(0, date_fetch)
    return


def example1():
    def print_sel():
        global date_fetch
        date_fetch = cal.selection_get()
        top.destroy()
        example2()

    top = Toplevel(main_screen)

    cal = Calendar(top,
                   font="Arial 14", selectmode='day',
                   cursor="hand1", year=2018, month=2, day=5)
    cal.pack(fill="both", expand=True)
    c_b = Button(top, text="ok", command=print_sel).pack()


def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("500x450")

    global username
    global password
    global F_Name
    global L_Name
    global DOB
    global Gender
    global Email_ID
    global ph_no
    global percent_10
    global percent_12
    global username_entry
    global password_entry
    global F_Name_entry
    global L_Name_entry
    global DOB_entry
    global Gender_entry
    global Email_ID_entry
    global ph_no_entry
    global percent_10_entry
    global percent_12_entry
    username = StringVar()
    password = StringVar()
    F_Name = StringVar()
    L_Name = StringVar()
    DOB = StringVar()
    Gender = StringVar()
    Email_ID = StringVar()
    ph_no = StringVar()
    percent_10 = StringVar()
    percent_12 = StringVar()

    # Label(register_screen, text="Please enter details below", bg="blue").pack()
    # Label(register_screen, text="").pack()
    Label(register_screen, text="Enter your Registration Details.", bg="black", fg="white", width="400", height="1",
          font=("Calibri", 13)).pack()
    Label(register_screen, text="").pack()
    F_Name_lable = Label(register_screen, text="First Name : ")
    F_Name_lable.place(x=95, y=40)
    F_Name_entry = Entry(register_screen, textvariable=F_Name)
    F_Name_entry.place(x=180, y=40)
    F_Name_entry.focus_set()
    L_Name_lable = Label(register_screen, text="Last Name : ")
    L_Name_lable.place(x=96, y=70)
    L_Name_entry = Entry(register_screen, textvariable=L_Name)
    L_Name_entry.place(x=180, y=70)
    username_lable = Label(register_screen, text="Username : ")
    username_lable.place(x=99, y=100)
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.place(x=180, y=100)
    password_lable = Label(register_screen, text="Password :")
    password_lable.place(x=102, y=130)
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.place(x=180, y=130)
    DOB_label = Label(register_screen, text="Date of Birth :")
    DOB_label.place(x=86, y=160)
    DOB_entry = Entry(register_screen, textvariable=DOB)
    DOB_entry.place(x=180, y=160)
    DOB_button = Button(register_screen, text="Select Date", bg="black", fg="white",
                        command=example1)
    DOB_button.place(x=312, y=160)
    Gender_label = Label(register_screen, text="Gender :")
    Gender_label.place(x=114, y=190)
    r1 = Radiobutton(register_screen, text="Male", variable=Gender, value="Male")
    r1.place(x=180, y=190)
    r1.select()
    r2 = Radiobutton(register_screen, text="Female", variable=Gender, value="Female")
    r2.place(x=250, y=190)
    r2.deselect()
    Email_ID_label = Label(register_screen, text="Email ID :")
    Email_ID_label.place(x=109, y=220)
    Email_ID_entry = Entry(register_screen, textvariable=Email_ID)
    Email_ID_entry.place(x=180, y=220)
    ph_no_label = Label(register_screen, text="Phone Number :")
    ph_no_label.place(x=71, y=250)
    ph_no_entry = Entry(register_screen, textvariable=ph_no)
    ph_no_entry.place(x=180, y=250)
    percent_10_label = Label(register_screen, text="10th Percentage :")
    percent_10_label.place(x=67, y=280)
    percent_10_entry = Entry(register_screen, textvariable=percent_10)
    percent_10_entry.place(x=180, y=280)
    percent_12_label = Label(register_screen, text="12th Percentage :")
    percent_12_label.place(x=67, y=310)
    percent_12_entry = Entry(register_screen, textvariable=percent_12)
    percent_12_entry.place(x=180, y=310)

    # _lable = Label(register_screen, text="Password :")
    # password_lable.place(x=102, y=100)
    # password_entry = Entry(register_screen, textvariable=password, show='*')
    # password_entry.place(x=180, y=100)
    # password_lable = Label(register_screen, text="Password :")
    # password_lable.place(x=102, y=100)
    # password_entry = Entry(register_screen, textvariable=password, show='*')
    # password_entry.place(x=180, y=100)
    # Label(register_screen, text="").pack()
    # Button(register_screen, text="Register", width=15, height=2, bg="black", fg="white", command=register_user).place(
    #     x=178, y=350)
    bb = Button(register_screen, text="Register", width=15, height=2, bg="black", fg="white", command=check).place(
        x=178, y=350)


def check():
    flag = 0
    flag1 = 0
    F_Name_info = F_Name.get()
    L_Name_info = L_Name.get()
    username_info = username.get()
    password_info = password.get()
    DOB_info = DOB.get()
    Gender_info = Gender.get()
    Email_ID_info = Email_ID.get()
    ph_no_info = ph_no.get()
    percent_10_info = percent_10.get()
    percent_12_info = percent_12.get()
    if F_Name_info == "":
        F_Name_info_empty = Label(register_screen, text="First Name cannot be empty.", fg="red", font=("calibri", 11))
        F_Name_info_empty.place(x=312, y=40)
        flag = 1
        register_screen.after(5000, F_Name_info_empty.destroy)
    if L_Name_info == "":
        L_Name_info_empty = Label(register_screen, text="First Name cannot be empty.", fg="red", font=("calibri", 11))
        L_Name_info_empty.place(x=312, y=70)
        flag = 1
        register_screen.after(5000, L_Name_info_empty.destroy)
    if username_info == "":
        username_info_empty = Label(register_screen, text="Username cannot be empty.", fg="red", font=("calibri", 11))
        username_info_empty.place(x=312, y=100)
        flag = 1
        register_screen.after(5000, username_info_empty.destroy)
    if password_info == "":
        password_info_empty = Label(register_screen, text="Password cannot be empty.", fg="red", font=("calibri", 11))
        password_info_empty.place(x=312, y=130)
        flag = 1
        register_screen.after(5000, password_info_empty.destroy)
    if DOB_info == "":
        DOB_info_empty = Label(register_screen, text="DOB cannot be empty.", fg="red", font=("calibri", 11))
        DOB_info_empty.place(x=312, y=160)
        flag = 1
        register_screen.after(5000, DOB_info_empty.destroy)
    if Email_ID_info == "":
        Email_ID_info_empty = Label(register_screen, text="E-Mail cannot be empty.", fg="red", font=("calibri", 11))
        Email_ID_info_empty.place(x=312, y=220)
        flag = 1
        register_screen.after(5000, Email_ID_info_empty.destroy)
    if ph_no_info == "":
        ph_no_info_empty = Label(register_screen, text="Ph.No cannot be empty.", fg="red", font=("calibri", 11))
        ph_no_info_empty.place(x=312, y=250)
        flag = 1
        register_screen.after(5000, ph_no_info_empty.destroy)
    if percent_10_info == "":
        percent_10_info_empty = Label(register_screen, text="Cannot be empty.", fg="red", font=("calibri", 11))
        percent_10_info_empty.place(x=312, y=280)
        flag = 1
        register_screen.after(5000, percent_10_info_empty.destroy)
    if percent_12_info == "":
        percent_12_info_empty = Label(register_screen, text="Cannot be empty.", fg="red", font=("calibri", 11))
        percent_12_info_empty.place(x=312, y=310)
        flag = 1
        register_screen.after(5000, percent_12_info_empty.destroy)
    if flag == 0:
        if "@" not in Email_ID_info and ".com" not in Email_ID_info:
            Email_ID_info_emptyy = Label(register_screen, text="Invalid Format.", fg="red", font=("calibri", 11))
            Email_ID_info_emptyy.place(x=312, y=220)
            register_screen.after(5000, Email_ID_info_emptyy.destroy)
            flag1 = 1
        try:
            i = int(ph_no_info)
            digits = int(math.log10(i)) + 1
            if digits != 10 and digits != 12:
                flag1 = 1
                ph_no_info_wrong = Label(register_screen, text="Invalid Format.", fg="red", font=("calibri", 11))
                ph_no_info_wrong.place(x=312, y=250)
                register_screen.after(5000, ph_no_info_wrong.destroy)
        except Exception as e:
            print(e)
            flag1 = 1
            ph_no_info_wrong = Label(register_screen, text="Enter only Digits", fg="red", font=("calibri", 11))
            ph_no_info_wrong.place(x=312, y=250)
            register_screen.after(5000, ph_no_info_wrong.destroy)
        try:
            ii = int(percent_10_info)
            digits = int(math.log10(ii)) + 1
            if digits != 1 and digits != 2 and digits != 3:
                flag1 = 1
                percent_10_info_wrong = Label(register_screen, text="Wrong Percentage.", fg="red", font=("calibri", 11))
                percent_10_info_wrong.place(x=312, y=280)
                register_screen.after(5000, percent_10_info_wrong.destroy)
        except:
            flag1 = 1
            percent_10_info_wrong = Label(register_screen, text="Enter only Digits.", fg="red", font=("calibri", 11))
            percent_10_info_wrong.place(x=312, y=280)
            register_screen.after(5000, percent_10_info_wrong.destroy)
        try:
            iii = int(percent_12_info)
            digits = int(math.log10(iii)) + 1
            if digits != 1 and digits != 2 and digits != 3:
                flag1 = 1
                percent_12_info_wrong = Label(register_screen, text="Wrong Percentage.", fg="red", font=("calibri", 11))
                percent_12_info_wrong.place(x=312, y=310)
                register_screen.after(5000, percent_12_info_wrong.destroy)
        except:
            flag1 = 1
            percent_12_info_wrong = Label(register_screen, text="Enter only Digits", fg="red", font=("calibri", 11))
            percent_12_info_wrong.place(x=312, y=310)
            register_screen.after(5000, percent_12_info_wrong.destroy)
    if flag1 == 0 and flag == 0:
        register_user()


# Designing window for login


def register_user():
    F_Name_info = F_Name.get()
    L_Name_info = L_Name.get()
    username_info = username.get()
    password_info = password.get()
    DOB_info = DOB.get()
    Gender_info = Gender.get()
    Email_ID_info = Email_ID.get()
    ph_no_info = ph_no.get()
    percent_10_info = percent_10.get()
    percent_12_info = percent_12.get()
    if str(username_info) in users.keys():
        # username_entry.delete(0, END)
        # password_entry.delete(0, END)
        userr_already_register = Label(register_screen, text="User Already Registered.", fg="black",
                                       font=("calibri", 13))
        userr_already_register.place(x=178, y=400)
        register_screen.after(2000, userr_already_register.destroy)
    else:
        users[str(username_info)] = {}
        users[str(username_info)]["F_Name"] = str(F_Name_info)
        users[str(username_info)]["L_Name"] = str(L_Name_info)
        users[str(username_info)]["DOB"] = str(DOB_info)
        users[str(username_info)]["Gender"] = str(Gender_info)
        users[str(username_info)]["Email_ID"] = str(Email_ID_info)
        users[str(username_info)]["ph_no"] = str(ph_no_info)
        users[str(username_info)]["10_percent"] = str(percent_10_info)
        users[str(username_info)]["12_percent"] = str(percent_12_info)
        users[str(username_info)]["Password"] = str(password_info)
        # username_entry.delete(0, END)
        # password_entry.delete(0, END)
        aaa = Label(register_screen, text="Registration Successful", fg="black", font=("calibri", 13))
        aaa.place(x=178, y=400)
        register_screen.after(5000, aaa.destroy)
        f = open("database", "wb")
        pickle.dump(users, f)
        f.close()

    # if os.path.exists(username_info):
    #     username_entry.delete(0, END)
    #     password_entry.delete(0, END)
    #     Label(register_screen, text="User Already Registered.", fg="green", font=("calibri", 11)).pack()
    #
    # else:
    #     file = open(username_info, "w")
    #     file.write(username_info + "\n")
    #     file.write(password_info)
    #     file.close()
    #     username_entry.delete(0, END)
    #     password_entry.delete(0, END)
    #
    #     Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()
    print(users)


def admin_login():
    global admin_login_screen
    admin_login_screen = Toplevel(main_screen)
    admin_login_screen.title("Admin Login")
    admin_login_screen.geometry("300x250")
    Label(admin_login_screen, text="Please enter Admin details below to login").pack()
    Label(admin_login_screen, text="").pack()

    global admin_username_verify
    global admin_password_verify

    admin_username_verify = StringVar()
    admin_password_verify = StringVar()

    global admin_username_login_entry
    global admin_password_login_entry

    Label(admin_login_screen, text="Username * ").pack()
    admin_username_login_entry = Entry(admin_login_screen, textvariable=admin_username_verify)
    admin_username_login_entry.pack()
    Label(admin_login_screen, text="").pack()
    Label(admin_login_screen, text="Password * ").pack()
    admin_password_login_entry = Entry(admin_login_screen, textvariable=admin_password_verify, show='*')
    admin_password_login_entry.pack()
    Label(admin_login_screen, text="").pack()
    Button(admin_login_screen, text="Login", width=10, height=1, command=admin_login_verify).pack()


# Implementing event on login button
def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry

    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show='*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command=login_verify).pack()


def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)

    # list_of_files = os.listdir()
    # if username1 in list_of_files:
    #     file1 = open(username1, "r")
    #     verify = file1.read().splitlines()
    #     if password1 in verify:
    #         login_sucess()
    #
    #     else:
    #         password_not_recognised()
    #
    # else:
    #     user_not_found()
    if str(username1) in users.keys():
        if str(password1) == users[str(username1)]["Password"]:
            login_sucess()
        else:
            password_not_recognised()
    else:
        user_not_found()


def admin_login_verify():
    username1 = admin_username_verify.get()
    password1 = admin_password_verify.get()
    admin_username_login_entry.delete(0, END)
    admin_password_login_entry.delete(0, END)

    if str(username1) in admin.keys():
        if str(password1) == admin[username1]:
            admin_login_sucess()
        else:
            admin_password_not_recognised()
    else:
        admin_user_not_found()


def admin_login_sucess():
    pass


def admin_password_not_recognised():
    pass


def admin_user_not_found():
    global admin_not_found_screen
    admin_not_found_screen = Toplevel(admin_login_screen)
    admin_not_found_screen.title("Failed")
    admin_not_found_screen.geometry("200x200")
    Label(admin_not_found_screen, text="Admin Not Found").pack()
    Button(admin_not_found_screen, text="OK", command=admin_delete_user_not_found_screen).pack()


# Designing popup for login success

def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Success").pack()
    Button(login_success_screen, text="OK", command=delete_login_success).pack()


# Designing popup for login invalid password

def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()


# Designing popup for user not found

def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()


# Deleting popups

def delete_login_success():
    login_success_screen.destroy()


def delete_password_not_recognised():
    password_not_recog_screen.destroy()

def admin_delete_password_not_recognised():
    password_not_recog_screen.destroy()


def delete_user_not_found_screen():
    user_not_found_screen.destroy()


# Designing Main(first) window

def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("300x250")
    main_screen.title("Account Login")
    # Label(text="Select Your Choice", bg="blue", width="300", height="2", font=("Calibri", 13)).pack()
    # Label(text="").pack()
    # Button(text="Login", height="2", width="30", command=login).pack()
    # Label(text="").pack()
    # Button(text="Register", height="2", width="30", command=register).pack()
    Label(text="Choose Login Or Register", bg="black", fg="white", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()

    Button(text="Student Login", height="2", width="30", command=login).pack()
    Label(text="").pack()
    Button(text="Student Register", height="2", width="30", command=register).pack()
    Label(text="").pack()
    Button(text="Admin Login", height="2", width="30", command=admin_login).pack()
    Label(text="").pack()
    main_screen.mainloop()


main_account_screen()
