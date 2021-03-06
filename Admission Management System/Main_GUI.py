from tkinter import messagebox
import math
import pickle
from tkinter import *
from tkcalendar import Calendar, DateEntry
import os

users = {}
try:
    file = open("database", "rb")
    users = pickle.load(file)
    file.close()
    print(users)
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
    bb = Button(register_screen, text="Register", width=15, height=2, bg="black", fg="white", command=check)
    bb.place(x=178, y=350)
    register_screen.bind('<Return>', lambda event=None: bb.invoke())


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
        if "@" not in Email_ID_info or ".com" not in Email_ID_info:
            Email_ID_info_emptyy = Label(register_screen, text="Invalid Format.", fg="red", font=("calibri", 11))
            Email_ID_info_emptyy.place(x=312, y=220)
            register_screen.after(5000, Email_ID_info_emptyy.destroy)
            flag1 = 1
        try:
            i = int(ph_no_info)
            digits = int(math.log10(i)) + 1
            if digits != 10:
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
        username_entry.delete(0, END)
        password_entry.delete(0, END)
        username_entry.focus_set()
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
        users[str(username_info)]["Status"] = "pending"
        F_Name_entry.delete(0, END)
        L_Name_entry.delete(0, END)
        password_entry.delete(0, END)
        username_entry.delete(0, END)
        DOB_entry.delete(0, END)
        Email_ID_entry.delete(0, END)
        ph_no_entry.delete(0, END)
        percent_10_entry.delete(0, END)
        percent_12_entry.delete(0, END)
        F_Name_entry.focus_set()
        aaa = Label(register_screen, text="Registration Successful", fg="black", font=("calibri", 13))
        aaa.place(x=178, y=400)
        register_screen.after(5000, aaa.destroy)
        f = open("database", "wb")
        pickle.dump(users, f)
        f.close()
    print(users)


def admin_login():
    global admin_login_screen
    admin_login_screen = Toplevel(main_screen)
    admin_login_screen.title("Admin Login")
    admin_login_screen.geometry("300x250")
    Label(admin_login_screen, text="Enter Admin details.", bg="black", fg="white", width="300", height="2",
          font=("Calibri", 13)).pack()
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
    admin_username_login_entry.focus_set()
    Label(admin_login_screen, text="").pack()
    Label(admin_login_screen, text="Password * ").pack()
    admin_password_login_entry = Entry(admin_login_screen, textvariable=admin_password_verify, show='*')
    admin_password_login_entry.pack()
    Label(admin_login_screen, text="").pack()
    b1 = Button(admin_login_screen, text="Login", width=15, height=1, bg="black", fg="white",
                command=admin_login_verify)
    b1.pack()
    admin_login_screen.bind('<Return>', lambda event=None: b1.invoke())


# Implementing event on login button
def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen, text="Please enter details below to login", bg="black", fg="white", width="300", height="2",
          font=("Calibri", 13)).pack()
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
    username_login_entry.focus_set()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show='*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    b2 = Button(login_screen, text="Login", width=15, height=1, bg="black", fg="white", command=login_verify)
    b2.pack()
    login_screen.bind('<Return>', lambda event=None: b2.invoke())


def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    if str(username1) in users.keys():
        if str(password1) == users[str(username1)]["Password"]:
            login_sucess()
        else:
            pwd_wrng = Label(login_screen, text="Wrong Password.", fg="red", font=("calibri", 11))
            pwd_wrng.pack()
            password_login_entry.delete(0, END)
            password_login_entry.focus_set()
            pwd_wrng.after(5000, pwd_wrng.destroy)
    else:
        pwd_wrng = Label(login_screen, text="Username not found.", fg="red", font=("calibri", 11))
        pwd_wrng.pack()
        username_login_entry.delete(0, END)
        password_login_entry.delete(0, END)
        username_login_entry.focus_set()
        pwd_wrng.after(5000, pwd_wrng.destroy)


def admin_login_verify():
    username1 = admin_username_verify.get()
    password1 = admin_password_verify.get()

    if str(username1) in admin.keys():
        if str(password1) == admin[username1]:
            admin_login_sucess()
        else:
            pwd_wrng = Label(admin_login_screen, text="Wrong Password.", fg="red", font=("calibri", 11))
            pwd_wrng.pack()
            # admin_username_login_entry.delete(0, END)
            admin_password_login_entry.delete(0, END)
            admin_password_login_entry.focus_set()
            pwd_wrng.after(5000, pwd_wrng.destroy)
    else:
        pwd_wrng = Label(admin_login_screen, text="Username Not Found.", fg="red", font=("calibri", 11))
        pwd_wrng.pack()
        admin_username_login_entry.delete(0, END)
        admin_password_login_entry.delete(0, END)
        admin_username_login_entry.focus_set()
        pwd_wrng.after(5000, pwd_wrng.destroy)


def admin_login_sucess():
    admin_login_screen.destroy()
    global admin_dashboard
    admin_dashboard = Toplevel(main_screen)
    admin_dashboard.title("Dashboard")
    admin_dashboard.geometry("150x150")

    OPTIONS = [a for a in users.keys()]
    OPTIONS = sorted(OPTIONS)
    variable = StringVar(admin_dashboard)
    variable.set(OPTIONS[0])  # default value
    Label(admin_dashboard, text="Choose Student.").pack()
    w = OptionMenu(admin_dashboard, variable, *OPTIONS)
    w.pack()

    def okkk():
        global Status

        Status = StringVar()
        usern = str(variable.get())
        print(usern)
        global status_window
        status_window = Toplevel(admin_dashboard)
        status_window.title("Application Status")
        status_window.geometry("400x450")
        Label(status_window, text="Student Application", bg="black", fg="white", width="400", height="1",
              font=("Calibri", 13)).pack()
        Label(status_window, text="").pack()
        F_Name_lable = Label(status_window, text="FirsName : ")
        F_Name_lable.place(x=95, y=40)
        aa = StringVar()
        F_Name_entryy = Entry(status_window, textvariable=aa, state='disabled')
        aa.set(users[usern]["F_Name"])
        F_Name_entryy.place(x=180, y=40)
        L_Name_lable = Label(status_window, text="Last Name : ")
        L_Name_lable.place(x=96, y=70)
        aa1 = StringVar()
        L_Name_entry = Entry(status_window, textvariable=aa1, state='disabled')
        aa1.set(users[usern]["L_Name"])
        L_Name_entry.place(x=180, y=70)
        username_lable = Label(status_window, text="Username : ")
        username_lable.place(x=99, y=100)
        aa2 = StringVar()
        username_entry = Entry(status_window, textvariable=aa2, state='disabled')
        aa2.set(usern)
        username_entry.place(x=180, y=100)
        password_lable = Label(status_window, text="Password :")
        password_lable.place(x=102, y=130)
        aa3 = StringVar()
        password_entry = Entry(status_window, show='*', textvariable=aa3, state='disabled')
        aa3.set(users[usern]["Password"])
        password_entry.place(x=180, y=130)
        DOB_label = Label(status_window, text="Date of Birth :")
        DOB_label.place(x=86, y=160)
        aa4 = StringVar()
        DOB_entry = Entry(status_window, textvariable=aa4, state='disabled')
        aa4.set(users[usern]["DOB"])
        DOB_entry.place(x=180, y=160)
        Gender_label = Label(status_window, text="Gender :")
        Gender_label.place(x=114, y=190)
        aa11 = StringVar()
        Gender_entry = Entry(status_window, textvariable=aa11, state='disabled')
        aa11.set(users[usern]["Gender"])
        Gender_entry.place(x=180, y=190)
        Email_ID_label = Label(status_window, text="Email ID :")
        Email_ID_label.place(x=109, y=220)
        aa10 = StringVar()
        Email_ID_entry = Entry(status_window, textvariable=aa10, state='disabled')
        aa10.set(users[usern]["Email_ID"])
        Email_ID_entry.place(x=180, y=220)
        ph_no_label = Label(status_window, text="Phone Number :")
        ph_no_label.place(x=71, y=250)
        aa5 = StringVar()
        ph_no_entry = Entry(status_window, textvariable=aa5, state='disabled')
        aa5.set(users[usern]["ph_no"])
        ph_no_entry.place(x=180, y=250)
        percent_10_label = Label(status_window, text="10th Percentage :")
        percent_10_label.place(x=67, y=280)
        aa6 = StringVar()
        percent_10_entry = Entry(status_window, textvariable=aa6, state='disabled')
        aa6.set(users[usern]["10_percent"])
        percent_10_entry.place(x=180, y=280)
        percent_12_label = Label(status_window, text="12th Percentage :")
        percent_12_label.place(x=67, y=310)
        aa7 = StringVar()
        percent_12_entry = Entry(status_window, textvariable=aa7, state='disabled')
        aa7.set(users[usern]["12_percent"])
        percent_12_entry.place(x=180, y=310)
        aaa1 = StringVar()

        def abc():
            if users[usern]["Status"] == "pending":
                status_label = Label(status_window, text="Status :")
                status_label.place(x=120, y=340)
                status_entry = Entry(status_window, textvariable=aaa1, state='disabled')
                aaa1.set("Pending")
                status_entry.place(x=180, y=340)
            elif users[usern]["Status"] == "no":
                status_label = Label(status_window, text="Status :")
                status_label.place(x=120, y=340)
                status_entry = Entry(status_window, textvariable=aaa1, state='disabled')
                aaa1.set("Declined")
                status_entry.place(x=180, y=340)
            elif users[usern]["Status"] == "yes":
                status_label = Label(status_window, text="Status :")
                status_label.place(x=120, y=340)
                status_entry = Entry(status_window, textvariable=aaa1, state='disabled')
                aaa1.set("Accepted")
                status_entry.place(x=180, y=340)

        abc()

        if users[usern]["Status"] == "pending":
            r12 = Radiobutton(status_window, text="Accept", variable=Status, value="yes", font=("Calibri", 13))
            r12.place(x=40, y=370)
            r12.deselect()
            r22 = Radiobutton(status_window, text="Decline", variable=Status, value="no", font=("Calibri", 13))
            r22.place(x=130, y=370)
            r22.deselect()
            r222 = Radiobutton(status_window, text="Pending", variable=Status, value="pending", font=("Calibri", 13))
            r222.place(x=220, y=370)
            r222.select()
        elif users[usern]["Status"] == "no":
            r12 = Radiobutton(status_window, text="Accept", variable=Status, value="yes", font=("Calibri", 13))
            r12.place(x=120, y=370)
            r12.deselect()
            r22 = Radiobutton(status_window, text="Decline", variable=Status, value="no", font=("Calibri", 13))
            r22.place(x=210, y=370)
            r22.select()
        elif users[usern]["Status"] == "yes":
            r12 = Radiobutton(status_window, text="Accept", variable=Status, value="yes", font=("Calibri", 13))
            r12.place(x=120, y=370)
            r12.select()
            r22 = Radiobutton(status_window, text="Decline", variable=Status, value="no", font=("Calibri", 13))
            r22.place(x=210, y=370)
            r22.deselect()

        def gg():
            gg = Status.get()
            users[usern]["Status"] = gg
            print(users[usern])
            f = open("database", "wb")
            pickle.dump(users, f)
            f.close()
            status_window.after(1, abc)

        Button(status_window, text="Submit", command=gg, font=("Calibri", 12)).place(x=150, y=410)

    buttonn = Button(admin_dashboard, text="OK", font=("Calibri", 11), command=okkk)
    buttonn.pack()
    buttonn.focus_set()
    admin_dashboard.bind('<Return>', lambda event=None: buttonn.invoke())


# Designing popup for login success

def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Student Dashboard")
    login_success_screen.geometry("300x200")
    Label(login_success_screen, text="Welcome %s" % (users[username_verify.get()]["F_Name"]), bg="black", fg="white",
          width="300",
          height="2", font=("Calibri", 13)).pack()
    Label(login_success_screen, text="").pack()
    b1 = Button(login_success_screen, text="Edit Details", width=13, height=1, bg="black", fg="white",
                command=edit_details).pack()
    Label(login_success_screen, text="").pack()
    b2 = Button(login_success_screen, text="Check Status", width=13, height=1, bg="black", fg="white",
                command=check_status).pack()


def edit_details():
    usern = username_verify.get()
    global edit_details_window
    global new_password
    global new_email
    global new_number
    new_password = StringVar()
    new_email = StringVar()
    new_number = StringVar()
    edit_details_window = Toplevel(login_success_screen)
    edit_details_window.title("Edit Details")
    edit_details_window.geometry("500x400")
    Label(edit_details_window, text="Edit Details", bg="black", fg="white", width="400", height="1",
          font=("Calibri", 13)).pack()
    Label(edit_details_window, text="").pack()
    F_Name_lable = Label(edit_details_window, text="FirsName : ")
    F_Name_lable.place(x=95, y=40)
    aa = StringVar()
    F_Name_entryy = Entry(edit_details_window, textvariable=aa, state='disabled')
    aa.set(users[usern]["F_Name"])
    F_Name_entryy.place(x=180, y=40)
    L_Name_lable = Label(edit_details_window, text="Last Name : ")
    L_Name_lable.place(x=96, y=70)
    aa1 = StringVar()
    L_Name_entry = Entry(edit_details_window, textvariable=aa1, state='disabled')
    aa1.set(users[usern]["L_Name"])
    L_Name_entry.place(x=180, y=70)
    username_lable = Label(edit_details_window, text="Username : ")
    username_lable.place(x=99, y=100)
    aa2 = StringVar()
    username_entry = Entry(edit_details_window, textvariable=aa2, state='disabled')
    aa2.set(usern)
    username_entry.place(x=180, y=100)
    password_lable = Label(edit_details_window, text="Password :")
    password_lable.place(x=102, y=130)
    password_entry = Entry(edit_details_window, textvariable=new_password)
    new_password.set(users[usern]["Password"])
    password_entry.place(x=180, y=130)
    DOB_label = Label(edit_details_window, text="Date of Birth :")
    DOB_label.place(x=86, y=160)
    aa4 = StringVar()
    DOB_entry = Entry(edit_details_window, textvariable=aa4, state='disabled')
    aa4.set(users[usern]["DOB"])
    DOB_entry.place(x=180, y=160)
    Gender_label = Label(edit_details_window, text="Gender :")
    Gender_label.place(x=114, y=190)
    aa11 = StringVar()
    Gender_entry = Entry(edit_details_window, textvariable=aa11, state='disabled')
    aa11.set(users[usern]["Gender"])
    Gender_entry.place(x=180, y=190)
    Email_ID_label = Label(edit_details_window, text="Email ID :")
    Email_ID_label.place(x=109, y=220)
    Email_ID_entry = Entry(edit_details_window, textvariable=new_email)
    new_email.set(users[usern]["Email_ID"])
    Email_ID_entry.place(x=180, y=220)
    ph_no_label = Label(edit_details_window, text="Phone Number :")
    ph_no_label.place(x=71, y=250)
    ph_no_entry = Entry(edit_details_window, textvariable=new_number)
    new_number.set(users[usern]["ph_no"])
    ph_no_entry.place(x=180, y=250)
    percent_10_label = Label(edit_details_window, text="10th Percentage :")
    percent_10_label.place(x=67, y=280)
    aa6 = StringVar()
    percent_10_entry = Entry(edit_details_window, textvariable=aa6, state='disabled')
    aa6.set(users[usern]["10_percent"])
    percent_10_entry.place(x=180, y=280)
    percent_12_label = Label(edit_details_window, text="12th Percentage :")
    percent_12_label.place(x=67, y=310)
    aa7 = StringVar()
    percent_12_entry = Entry(edit_details_window, textvariable=aa7, state='disabled')
    aa7.set(users[usern]["12_percent"])
    percent_12_entry.place(x=180, y=310)
    v_b = Button(edit_details_window, text="Submit", width=13, height=1, bg="black", fg="white",
                 command=verify_edit_details)
    v_b.place(x=180, y=340)
    edit_details_window.bind('<Return>', lambda event=None: v_b.invoke())


def verify_edit_details():
    flag = 0
    flag1 = 0
    password_info = new_password.get()
    Email_ID_info = new_email.get()
    ph_no_info = new_number.get()
    if password_info == "":
        password_info_empty = Label(edit_details_window, text="Password cannot be empty.", fg="red",
                                    font=("calibri", 11))
        password_info_empty.place(x=312, y=130)
        flag = 1
        edit_details_window.after(5000, password_info_empty.destroy)
    if Email_ID_info == "":
        Email_ID_info_empty = Label(edit_details_window, text="E-Mail cannot be empty.", fg="red", font=("calibri", 11))
        Email_ID_info_empty.place(x=312, y=220)
        flag = 1
        register_screen.after(5000, Email_ID_info_empty.destroy)
    if ph_no_info == "":
        ph_no_info_empty = Label(edit_details_window, text="Ph.No cannot be empty.", fg="red", font=("calibri", 11))
        ph_no_info_empty.place(x=312, y=250)
        flag = 1
        edit_details_window.after(5000, ph_no_info_empty.destroy)
    if flag == 0:
        if "@" not in Email_ID_info or ".com" not in Email_ID_info:
            Email_ID_info_emptyy = Label(edit_details_window, text="Invalid Format.", fg="red", font=("calibri", 11))
            Email_ID_info_emptyy.place(x=312, y=220)
            edit_details_window.after(5000, Email_ID_info_emptyy.destroy)
            flag1 = 1
        try:
            i = int(ph_no_info)
            digits = int(math.log10(i)) + 1
            if digits != 10:
                flag1 = 1
                ph_no_info_wrong = Label(edit_details_window, text="Invalid Format.", fg="red", font=("calibri", 11))
                ph_no_info_wrong.place(x=312, y=250)
                edit_details_window.after(5000, ph_no_info_wrong.destroy)
        except Exception as e:
            print(e)
            flag1 = 1
            ph_no_info_wrong = Label(edit_details_window, text="Enter only Digits", fg="red", font=("calibri", 11))
            ph_no_info_wrong.place(x=312, y=250)
            edit_details_window.after(5000, ph_no_info_wrong.destroy)
    if flag1 == 0 and flag == 0:
        done_editing()


def done_editing():
    usern = username_verify.get()
    password_info = new_password.get()
    Email_ID_info = new_email.get()
    ph_no_info = new_number.get()
    aaa = Label(edit_details_window, text="Details Edited Successfully", fg="black", font=("calibri", 13))
    aaa.place(x=178, y=370)
    edit_details_window.after(5000, aaa.destroy)
    users[usern]["Password"] = password_info
    users[usern]["Email_ID"] = Email_ID_info
    users[usern]["ph_no"] = ph_no_info
    f = open("database", "wb")
    pickle.dump(users, f)
    f.close()
    print(users)


def check_status():
    usern = username_verify.get()
    if users[usern]["Status"] == "pending":
        messagebox.showinfo("Status", "Your Application is still pending.")
    elif users[usern]["Status"] == "yes":
        messagebox.showinfo("Status", "Congratulations!! Your Application is Accepted.")
    elif users[usern]["Status"] == "no":
        messagebox.showinfo("Status", "Your Application is declined. Try again next year.")
    login_success_screen.lift(aboveThis=main_screen)


def main_account_screen():
    def on_close():
        main_screen.quit()
        pass

    global main_screen
    main_screen = Tk()
    main_screen.geometry("300x250")
    main_screen.title("Account Login")
    Label(text="Choose Login Or Register", bg="black", fg="white", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()

    Button(text="Student Login", height="2", width="30", command=login).pack()
    Label(text="").pack()
    Button(text="Student Register", height="2", width="30", command=register).pack()
    Label(text="").pack()
    Button(text="Admin Login", height="2", width="30", command=admin_login).pack()
    Label(text="").pack()
    main_screen.protocol("WM_DELETE_WINDOW", on_close)
    main_screen.mainloop()


main_account_screen()
