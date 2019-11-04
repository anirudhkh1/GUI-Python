from tkinter import *
root = Tk()
mystr = StringVar()
entry = Entry(textvariable=mystr, state=DISABLED).pack(side=LEFT)
mystr.set('hello world')
mainloop()