import tkinter as tk
import database as db


class LoginGUI(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_columnconfigure(0, weight=1)
        container.grid_rowconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, RegisterPage, MainMenu, ForgetPass, Security, ResetPass):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()

    def add_user(self, username, password, passwordreenter):
        if password == passwordreenter:
            print(username + " " + password)
            db.add_user(username, password)
            self.show_frame(StartPage)

    def check_user(self, username, password):
        if db.check_user(username, password):
            print("welcome ", username)
            self.show_frame(MainMenu)

        else:
            print("who are you??")

    def f_check_user(self,username):
        if db.fp_check_user(username):
            self.show_frame(Security)
        else:
            self.show_frame(StartPage)
            print("who are you")

    def security_question(self,ans):
        if ans == "mesha" :
            self.show_frame(ResetPass)
        else:
            print("wrong")

    def reset_pass(self,username, password,re_pass):
        if password == re_pass:
            db.change_pass(username, password)
            print("password reset")
            self.show_frame(StartPage)
        else:
            print("password does not match")


class StartPage(tk.Frame):

    def __init__(self, window, controller):
        tk.Frame.__init__(self, window)

        self.login_tbox1Text = tk.StringVar()
        self.login_tbox2Text = tk.StringVar()

        login_label1 = tk.Label(self, text="Login").pack()

        login_label2 = tk.Label(self, text="Username").pack()
        login_tbox1 = tk.Entry(self, textvariable=self.login_tbox1Text).pack()

        login_label3 = tk.Label(self, text="Password").pack()
        login_tbox2 = tk.Entry(self, textvariable=self.login_tbox2Text).pack()

        login_button1 = tk.Button(self, text="Sign in", command=lambda: controller.check_user(self.login_tbox1Text.get(), self.login_tbox2Text.get())).pack()
        login_button2 = tk.Button(self, text="Register", command=lambda: controller.show_frame(RegisterPage)).pack()
        forget_button2 = tk.Button(self, text="Forgot Password", command=lambda: controller.show_frame(ForgetPass)).pack()


class RegisterPage(tk.Frame):

    def __init__(self, window, controller):
        tk.Frame.__init__(self, window)

        # self.controller = controller

        self.tbox1Text = tk.StringVar()
        self.tbox2Text = tk.StringVar()
        self.tbox3Text = tk.StringVar()

        label1 = tk.Label(self, text="Sign-up").pack()

        label2 = tk.Label(self, text="Username").pack()
        tbox1 = tk.Entry(self, textvariable=self.tbox1Text).pack()

        label3 = tk.Label(self, text="Password").pack()
        tbox2 = tk.Entry(self, textvariable=self.tbox2Text).pack()

        label3 = tk.Label(self, text="Re-enter Password").pack()
        tbox3 = tk.Entry(self, textvariable=self.tbox3Text).pack()

        button= tk.Button(self, text="Register", command=lambda: controller.add_user(self.tbox1Text.get(), self.tbox2Text.get(), self.tbox3Text.get())).pack()


class MainMenu(tk.Frame):

    def __init__(self, window, controller):
        tk.Frame.__init__(self, window)

        label1 = tk.Label(self, text="You've successfully logged in!").pack()


class ForgetPass(tk.Frame):

    def __init__(self, window, controller):
        tk.Frame.__init__(self, window)

        self.ftbox1Text = tk.StringVar()

        label1 = tk.Label(self, text="Please Enter your username:").pack()
        tbox1 = tk.Entry(self, textvariable=self.ftbox1Text).pack()

        button = tk.Button(self, text="Submit", command=lambda: controller.f_check_user(self.ftbox1Text.get())).pack()


class Security(tk.Frame):

    def __init__(self, window, controller):
        tk.Frame.__init__(self, window)

        self.box1Text = tk.StringVar()

        label1 = tk.Label(self, text="What is you first cats name:").pack()
        tbox1 = tk.Entry(self, textvariable=self.box1Text).pack()

        button1 = tk.Button(self, text="Submit", command=lambda: controller.security_question(self.box1Text.get())).pack()


class ResetPass(tk.Frame):

    def __init__(self, window, controller):
        tk.Frame.__init__(self, window)

        self.t1Text = tk.StringVar()
        self.t2Text = tk.StringVar()
        self.Text3 = tk.StringVar()

        label1 = tk.Label(self, text="Please Enter your username:").pack()
        tbox1 = tk.Entry(self, textvariable=self.t1Text).pack()

        label3 = tk.Label(self, text="new Password").pack()
        tbox2 = tk.Entry(self, textvariable=self.t2Text).pack()

        label3 = tk.Label(self, text="Re-enter Password").pack()
        tbox3 = tk.Entry(self, textvariable=self.Text3).pack()

        button1 = tk.Button(self, text="Submit", command=lambda: controller.reset_pass(self.t1Text.get(),self.t2Text.get(),self.Text3.get())).pack()


app = LoginGUI()
app.mainloop()

# root.geometry("300x400")
# root.title("Rae's Program")
