from tkinter import *

main_screen = Tk()
main_screen.geometry("400x280")
main_screen.title("Account Login")

Label(text="Choose Login Or Register", bg="black",fg="white", width="300", height="2", font=("Calibri", 13)).pack()
Label(text="").pack()

Button(text="Student Login", height="2", width="30").pack()
Label(text="").pack()
Button(text="Student Register", height="2", width="30").pack()
Label(text="").pack()
Button(text="Admin Login", height="2", width="30").pack()
Label(text="").pack()

main_screen.mainloop()
