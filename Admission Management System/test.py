from tkinter.filedialog import asksaveasfile
from tkinter import *

root = Tk()
root.geometry('200x150')


# function to call when user press
# the save button, a filedialog will 
# open and ask to save file 
def save():
    files = [('All Files', '*.*'),
             ('Python Files', '*.py'),
             ('Text Document', '*.txt')]
    file = asksaveasfile(filetypes=files, defaultextension=files)
    print(file.name)

btn = Button(root, text='Save', command=lambda: save())
btn.pack(side=TOP, pady=20)

mainloop()


# from tkinter import messagebox
#
# messagebox.showinfo("Title", "a Tk MessageBox")