from tkinter import *
import database as db

# Initialisations
root = Tk()
tbox1Text = StringVar()
tbox2Text = StringVar()
tbox3Text = StringVar()

login_tbox1Text = StringVar()
login_tbox2Text = StringVar()

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

def check_user():
    username = login_tbox1Text.get()
    password = login_tbox2Text.get()

    if db.check_user(username, password):
        print("welcome ", username)

    else:
        print("who are you??")


# Register

label1 = Label(root, text = "Sign-up").pack()

label2 = Label(root, text = "Username").pack()
tbox1 = Entry(root, textvariable = tbox1Text).pack()

label3 = Label(root, text = "Password").pack()
tbox2 = Entry(root, textvariable = tbox2Text).pack()

label3 = Label(root, text = "Re-enter Password").pack()
tbox3 = Entry(root, textvariable = tbox3Text).pack()

button1 = Button(root, text = "Register", command = add_user).pack()

#space
login_label = Label(root).pack()

#Login
login_label1 = Label(root, text = "Login").pack()

login_label2 = Label(root, text = "Username").pack()
login_tbox1 = Entry(root, textvariable = login_tbox1Text).pack()

login_label3 = Label(root, text = "Password").pack()
login_tbox2 = Entry(root, textvariable = login_tbox2Text).pack()


login_button1 = Button(root, text = "sign in ", command = check_user).pack()
root.mainloop()
