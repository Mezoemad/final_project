import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

class LoginPage(tk.Frame):
    def __init__(self, root, app):
        tk.Frame.__init__(self, root, bg="blue")
        self.root = root
        self.app = app
        self.create_widgets()

    def create_widgets(self):
        self.email_label = tk.Label(self, text="Email:", bg="white", font=("Helvetica", 16))
        self.email_entry = tk.Entry(self)
        self.password_label = tk.Label(self, text="Password:", font=("Helvetica", 16), bg="white")
        self.password_entry = tk.Entry(self, show="*")
        self.login_button = tk.Button(self, text="Login", command=self.login, font=12, bg="white", fg="black")
        self.register_button = tk.Button(self, text="Register", command=self.register, font=12, bg="white", fg="black")

        image = Image.open("login.png")
        photo = ImageTk.PhotoImage(image)
        self.image_label = tk.Label(self, image=photo, bg="blue")
        self.image_label.image = photo

        self.email_label.pack(pady=10)
        self.email_entry.pack(pady=5)
        self.password_label.pack(pady=10)
        self.password_entry.pack(pady=5)
        self.login_button.pack(pady=10)
        self.register_button.pack(pady=5)
        self.image_label.pack()



    def login(self):
        email = self.email_entry.get()
        password = self.password_entry.get()
        if email in self.app.users and self.app.users[email]["password"] == password:
            name = self.app.users[email]['First name']
            messagebox.showinfo("Welcome", f"Welcome back, {name} to the social media platform!")
            self.app.current_user = email  # Set the current user
            self.app.show_page("HomePage")  # Show the "HomePage"
        else:
            messagebox.showerror("Login Failed", "Invalid email or password.")

    def register(self):
        self.app.show_page("RegisterPage")
