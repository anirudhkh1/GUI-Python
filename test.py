import tkinter
from tkinter import filedialog
import os

root = tkinter.Tk()
root.withdraw()  # use to hide tkinter window


def search_for_file_path():
    currdir = os.getcwd()
    tempdir = filedialog.askopenfilename(filetypes=(("All files", "*"),("Template files", "*.type")))
    if len(tempdir) > 0:
        print("You chose: %s" % tempdir)
    return tempdir


file_path_variable = search_for_file_path()
print("\nfile_path_variable = ", file_path_variable)
