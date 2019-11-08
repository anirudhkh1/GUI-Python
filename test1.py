try:                        # In order to be able to import tkinter for
    import tkinter as tk    # either in python 2 or in python 3
except ImportError:
    import Tkinter as tk


def toggle_password():
    global entry, checkbutton
    if checkbutton.var.get():
        entry['show'] = "*"
    else:
        entry['show'] = ""


if __name__ == '__main__':
    root = tk.Tk()
    entry = tk.Entry(root)
    entry.default_show_val = entry['show']
    entry['show'] = "*"
    checkbutton = tk.Checkbutton(root,
                                        text="Hide password",
                                        onvalue=True,
                                        offvalue=False,
                                        command=toggle_password)
    checkbutton.var = tk.BooleanVar(value=True)
    checkbutton['variable'] = checkbutton.var
    entry.pack()
    checkbutton.pack()
    tk.mainloop()