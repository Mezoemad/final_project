import json
import tkinter as tk

from Login import LoginPage
from register import RegisterPage
from Homepage import HomePage
from Profilepage import Profilepage

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Social Media Platform")
        self.root.geometry("900x600")
        self.root.resizable(width=False, height=False)
        self.pages = []
        self.page_stack = []
        self.current_user = None
        self.load_user_data()

        self.initialize_pages()

        self.show_page("LoginPage")

    def load_user_data(self):
        try:
            with open("users.json", "r") as file:
                self.users = json.load(file)
        except FileNotFoundError:
            self.users = {}

    def save_user_data(self):
        with open("users.json", "w") as file:
            json.dump(self.users, file, indent=2)

    def add_page(self, page_class, page_instance):
        self.pages.append([page_class, page_instance])

    def initialize_pages(self):
        self.login_page = LoginPage(self.root, self)
        self.register_page = RegisterPage(self.root, self)
        self.home_page = HomePage(self.root, self)
        self.profile_page = Profilepage(self.root, self)

        self.add_page(LoginPage, self.login_page)
        self.add_page(RegisterPage, self.register_page)
        self.add_page(HomePage, self.home_page)
        self.add_page(Profilepage, self.profile_page)

    def show_page(self, page_name):
        for page_class, class_instance in self.pages:
            if page_class.__name__ == page_name:
                if self.page_stack:
                    previous_page = self.page_stack[-1]
                    previous_page[1].pack_forget()
                page = page_class(self.root, self)
                page.pack()
                self.page_stack.append([page_class, page])
                break

    def show_previous_page(self):
        if len(self.page_stack) > 1:
            self.page_stack.pop()[1].pack_forget()
            previous_page = self.page_stack[-1]
            page = previous_page[0](self.root, self)
            page.pack()
            self.page_stack[-1] = [previous_page[0], page]


root = tk.Tk()
root.configure(bg="blue")
app = App(root)
root.mainloop()
