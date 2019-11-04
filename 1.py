import tkinter as TK

root = TK.Tk()
button= TK.Button(root)
button.pack()

def func1():
    print('func1 is called!')
    button.config(text='call func2', command=func2)
def func2():
    print('func2 is called!')

button.config(text='call func1', command=func1)

root.bind('<Return>', lambda event=None: button.invoke())
root.mainloop()