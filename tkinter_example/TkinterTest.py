from tkinter import *
import database as db

# Initialisations
root = Tk()
tbox1Text = StringVar()
tbox2Text = StringVar()
tbox3Text = StringVar()

root.geometry("300x400")
root.title("Rae's Program")

# Functions
def add_user():
    username = tbox1Text.get()
    password = tbox2Text.get()
    passwordreenter = tbox3Text.get()
    if (password == passwordreenter):
        print(username + " " + password)
        db.add_user(username, password)

label1 = Label(root, text = "Sign-up").pack()

label2 = Label(root, text = "Username").pack()
tbox1 = Entry(root, textvariable = tbox1Text).pack()

label3 = Label(root, text = "Password").pack()
tbox2 = Entry(root, textvariable = tbox2Text).pack()

label3 = Label(root, text = "Re-enter Password").pack()
tbox3 = Entry(root, textvariable = tbox3Text).pack()

button1 = Button(root, text = "Register", command = add_user).pack()

root.mainloop()