import os
import sys
import pandas as pd
import pickle

global f_name


def display():
    data_table = pd.DataFrame(data)
    print(data_table)


def add_data():
    try:
        global data
        data_table = pd.DataFrame(data)
        s_name = input("Enter Name = ")
        p_marks = input("Python Marks = ")
        c_marks = input("C++ Marks = ")
        a_marks = input("ASP.net Marks = ")
        j_marks = input("JAVA Marks = ")
        aa_marks = input("Android Marks = ")
        line = pd.DataFrame(
            {"Name": s_name, "Python": p_marks, "C++": c_marks, "ASP.Net": a_marks, "JAVA": j_marks,
             "Android": aa_marks},
            index=[0])
        data_table = data_table.append(line, ignore_index=True)
        # df = df.sort_index().reset_index(drop=True)
        data_table = data_table.reindex(["Name", 'Python', 'C++', 'ASP.Net', 'JAVA', 'Android'], axis=1)
        data = data_table.to_dict()
        f = open("dd", "wb")
        pickle.dump(data, f)
        f.close()
        print("Data Added Successfully")

    except Exception as e:
        print(e)


def delete_record():
    try:
        global data
        data_table = pd.DataFrame(data)
        print(data_table)
        ind = int(input("Enter the Index Number to be deleted = "))
        data_table = data_table.drop(data_table.index[ind])
        data = data_table.to_dict()
        f = open("dd", "wb")
        pickle.dump(data, f)
        f.close()
        print("Successfully Deleted.")
    except Exception as e:
        print(e)


def open_file():
    try:
        cc = input("Enter File Name (without extension) = ")
        os.startfile(str(cc) + ".xlsx")
    except Exception as FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(e)


def prnt_data():
    print(data)


def export_data():
    try:
        f_name = input("Enter File Name = ")
        try:
            fff = open("F_Name", "wb")
            pickle.dump(f_name, fff)
            fff.close()
        except:
            pass
        data_table = pd.DataFrame(data)
        data_table.to_excel(str(f_name) + ".xlsx")
        print("File Created.\n")
        cc = input("Do you want to open the Excel File (Y/N) = ")
        if cc == "Y" or cc == "y":
            os.startfile(str(f_name) + ".xlsx")
        else:
            pass
    except Exception as e:
        print(e)


def options():
    while 1:
        print("\n--------------------------------------\n")
        print("1. Display the current Data in tabular form.")
        print("2. Add a student record.")
        print("3. Delete a student record.")
        print("4. Export data to Excel File.")
        print("5. Print data in Dictionary Format.")
        print("6. Open the excel file (if created).")
        print("Press 9 to exit.")
        ch = input("\nEnter your choice = ")
        if ch == "1":
            display()
        elif ch == "3":
            delete_record()
        elif ch == "2":
            add_data()
        elif ch == "4":
            export_data()
        elif ch == "9":
            sys.exit()
        elif ch == "5":
            prnt_data()
        elif ch == "6":
            open_file()
        else:
            print("Invalid choice.\n")


try:
    file = open("dd", "rb")
    data = pickle.load(file)
    file.close()
    # fff = open("F_Name", "rb")
    # f_name = pickle.load(fff)
    # fff.close()
except FileNotFoundError:
    # global data
    data = {'Name': {}, 'Python': {}, 'C++': {}, 'ASP.Net': {}, 'JAVA': {}, 'Android': {}}
options()
