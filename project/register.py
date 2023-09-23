import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class RegisterPage(tk.Frame):
    def __init__(self, root, app):
        tk.Frame.__init__(self, root, bg="blue")
        self.root = root
        self.app = app
        self.create_widgets()

    def create_widgets(self):
        self.name_label1 = tk.Label(self, text="First name:", bg="white", font=("Helvetica", 16))
        self.name_entry1 = tk.Entry(self)
        self.name_label2 = tk.Label(self, text="Last name:", bg="white", font=("Helvetica", 16))
        self.name_entry2 = tk.Entry(self)
        self.phone_label = tk.Label(self, text="Phone:", bg="white", font=("Helvetica", 16))
        self.phone_entry = tk.Entry(self)
        self.gender_label = tk.Label(self, text="Gender:", bg="white", font=("Helvetica", 16))
        self.gender_combobox = ttk.Combobox(self, values=["Female", "Male"])
        self.email_label = tk.Label(self, text="Email:", bg="white", font=("Helvetica", 16))
        self.email_entry = tk.Entry(self)
        self.password_label = tk.Label(self, text="Password:", bg="white", font=("Helvetica", 16))
        self.password_entry = tk.Entry(self, show="*")
        self.confirm_password_label = tk.Label(self, text="Confirm Password:", bg="white", font=("Helvetica", 16))
        self.confirm_password_entry = tk.Entry(self, show="*")
        self.age_label = tk.Label(self, text="Age:", bg="white", font=("Helvetica", 16))
        self.age_entry = tk.Entry(self)

        self.register_button = tk.Button(self, text="Register", command=self.register, bg="blue", fg="white", font=12)
        self.back_button = tk.Button(self, text="Back", command=self.go_back, bg="blue", fg="white", font=12)

        self.name_label1.pack(pady=5)
        self.name_entry1.pack()
        self.name_label2.pack(pady=5)
        self.name_entry2.pack()
        self.phone_label.pack(pady=5)
        self.phone_entry.pack()
        self.gender_label.pack(pady=5)
        self.gender_combobox.pack()
        self.email_label.pack(pady=5)
        self.email_entry.pack()
        self.password_label.pack(pady=5)
        self.password_entry.pack()
        self.confirm_password_label.pack(pady=5)
        self.confirm_password_entry.pack()
        self.age_label.pack(pady=5)
        self.age_entry.pack()
        self.register_button.pack(pady=5)
        self.back_button.pack()

    def register(self):
        name1 = self.name_entry1.get()
        name2 = self.name_entry2.get()
        phone = self.phone_entry.get()
        gender = self.gender_combobox.get()
        email = self.email_entry.get()
        password = self.password_entry.get()
        confirm_password = self.confirm_password_entry.get()
        age = self.age_entry.get()

        if not name1 or not name2 or not phone or not gender or not email or not password or not confirm_password or not age :
            messagebox.showerror("Error", "Please fill in all fields.")
        elif password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match.")
        elif email in self.app.users:
            messagebox.showerror("Error", "Email already registered.")
        else:
            self.app.users[email] = {
                "First name": name1,
                "last name": name2,
                "phone": phone,
                "gender": gender,
                "email": email,
                "password": password,
                "age": age,
            }
            self.app.save_user_data()
            messagebox.showinfo("Success", "Registration successful.")
            self.go_back()

            self.app.save_user_data()
            messagebox.showinfo("Success", "Registration successful.")
            self.app.show_page("login")


    def go_back(self):
         self.app.show_previous_page()
