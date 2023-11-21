from tkinter import *
from tkinter import messagebox
import pymysql

class SignUpPage:
    def __init__(self, root, switch_page_callback):
        self.root = root
        self.switch_page_callback = switch_page_callback
        self.frame = Frame(root, bg="#dfdee2", bd=5)

        username_label = Label(self.frame, text="Username:", bg="#dfdee2")
        username_label.place(relx=0.05, rely=0.1, relwidth=0.4, relheight=0.4)

        self.username_entry = Entry(self.frame)
        self.username_entry.place(relx=0.5, rely=0.1, relwidth=0.4, relheight=0.4)

        password_label = Label(self.frame, text="Password:", bg="#dfdee2")
        password_label.place(relx=0.05, rely=0.55, relwidth=0.4, relheight=0.4)

        self.password_entry = Entry(self.frame, show="*")
        self.password_entry.place(relx=0.5, rely=0.55, relwidth=0.4, relheight=0.4)

        register_button = Button(self.frame, text="Register", font='Helvetica 10 bold', bg='black', fg='white', command=self.on_register_button_click)
        register_button.place(relx=0.28, rely=0.7, relwidth=0.45, relheight=0.1)

    def on_register_button_click(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Call the register_user function or your registration logic here
        # For simplicity, we'll show a messagebox
        messagebox.showinfo("Registration", f"User {username} registered successfully!")

        # Switch to the sign-in page after registration
        self.switch_page_callback()

    def show(self):
        self.frame.place(relx=0.2, rely=0.3, relwidth=0.6, relheight=0.2)

    def hide(self):
        self.frame.place_forget()

class SignInPage:
    def __init__(self, root, switch_page_callback):
        self.root = root
        self.switch_page_callback = switch_page_callback
        self.frame = Frame(root, bg="#dfdee2", bd=5)

        username_label = Label(self.frame, text="Username:", bg="#dfdee2")
        username_label.place(relx=0.05, rely=0.1, relwidth=0.4, relheight=0.4)

        self.username_entry = Entry(self.frame)
        self.username_entry.place(relx=0.5, rely=0.1, relwidth=0.4, relheight=0.4)

        password_label = Label(self.frame, text="Password:", bg="#dfdee2")
        password_label.place(relx=0.05, rely=0.55, relwidth=0.4, relheight=0.4)

        self.password_entry = Entry(self.frame, show="*")
        self.password_entry.place(relx=0.5, rely=0.55, relwidth=0.4, relheight=0.4)

        signin_button = Button(self.frame, text="Sign In", font='Helvetica 10 bold', bg='black', fg='white', command=self.on_signin_button_click)
        signin_button.place(relx=0.28, rely=0.7, relwidth=0.45, relheight=0.1)

    def on_signin_button_click(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Call the authenticate_user function or your authentication logic here
        # For simplicity, we'll show a messagebox
        messagebox.showinfo("Authentication", f"User {username} authenticated successfully!")

        # Switch to the sign-up page after authentication
        self.switch_page_callback()

    def show(self):
        self.frame.place(relx=0.2, rely=0.3, relwidth=0.6, relheight=0.2)

    def hide(self):
        self.frame.place_forget()
