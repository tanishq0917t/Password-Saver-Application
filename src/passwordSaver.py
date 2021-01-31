# Some lines are skipped or kept incomplete due to security issues.

from tkinter import *
from tkinter import messagebox as messagebox
import os.path
root = Tk()
root.title("Password Saver Tool By Tanishq Rawat")
root.iconbitmap("C:/Work/Python/Codes/"+"logo.ico")
#
root.configure(bg='black')
label1 = Label(root, text='User Name',bg="black",fg="white")
label2 = Label(root, text='Password',bg="black",fg="white")
label3 = Label(root, text='Website',bg="black",fg="white")
label4 = Label(root, text='',bg="black",fg="white").grid(row=3)
label5 = Label(root, text="Click Add until Confirmation Dialog Appears",bg="black",fg="white").grid(row=5,column=1)
def popUp():
    messagebox.showinfo("Confirmation","Your Password is Saved")

def error():
    messagebox.showerror("Check Inputs","Enter Details Correctly")

def ClickAdd():
    if not os.path.exists("info.txt"):
        file1 = open("info.txt", 'w')
        #
        file1.close()
    else:
        file = open("info.txt", 'a')
        if e1.get() == "" or e2.get() == "" or e3.get() == "":
            error()
        else:
            uName = "UserName: " + e1.get() + "\n"
            pwd = "Password: " + e2.get() + "\n"
            web = "Website: " + e3.get() + "\n"
            file.write("---------------------------------\n")
            file.write(uName)
            file.write(pwd)
            file.write(web)
            file.write("---------------------------------\n")
            file.write("\n")
            file.close()
            #
            #
            #
            popUp()


def readPasswords():
    file = open("info.txt").read()
    root1 = Tk()
    root1.title("Passwords Viewer")
    root1.iconbitmap("C:/Work/Python/Codes/"+"logo.ico")
    Label(root1, text=file, width=50,bg="black",fg="white").grid(row=0,column=0)
e1 = Entry(root, width=50)
e2 = Entry(root, width=50)
e3 = Entry(root, width=50)
label1.grid(row=0)
label2.grid(row=1)
label3.grid(row=2)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
e1.insert(0,"")
e2.insert(0,"")
e3.insert(0,"")

button = Button(root, text="Add", borderwidth=5, padx=50, pady=10, command=ClickAdd, fg="white",bg="Green").grid(row=4, column=0)
button1 = Button(root, text="Show Passwords", borderwidth=5, padx=50, pady=10, command=readPasswords, fg="black", bg="Yellow").grid(row=4, column=1)
button_exit = Button(root, text="Exit", command=root.quit, fg="black", bg="Red", borderwidth=5, padx=50, pady=10).grid(row=4, column=2)

root.mainloop()
