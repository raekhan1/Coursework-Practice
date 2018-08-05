import database as db

from Tkinter import *

root = Tk()

user_label = Label(root, text="Enter your username:")
user_label.pack()

username = Entry(root)
username.pack()

pass_label = Label(root, text="Enter your password:")
pass_label.pack()

password = Entry(root)
password.pack()

user_value = username.get()
pass_value = password.get()

data = [
    ("Rae", "Khan"),
    ("Abby", "H"),

]

db.create_table()
db.add_user(data)


def con():
    if db.check(user_value,pass_value):
        confirm = Label(root, text="welcome")
    else:
        confirm = Label(root, text="try again")
    confirm.pack()


submit = Button(root, text="Submit", command=con)
submit.pack()

root.mainloop()
