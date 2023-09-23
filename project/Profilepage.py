import tkinter as tk
from tkinter import messagebox
import json
class Profilepage(tk.Frame):
    def __init__(self, root, app):
        tk.Frame.__init__(self, root, bg="white")
        self.root = root
        self.app = app
        self.load_user_posts()
        self.create_widgets()

    def create_widgets(self):
        self.post_button = tk.Button(self, text="click to post", command=self.post, bg="blue", fg="white", font=12)
        self.post_button.pack(pady=5)
        self.back_button = tk.Button(self, text="Back", command=self.go_back, bg="blue", fg="white", font=12)
        self.back_button.pack(pady=5)
        self.showpost_button = tk.Button(self, text="show my posts", command=self.show_my_posts, bg="blue", fg="white", font=12)
        self.showpost_button.pack(pady=5)
        self.show_friends = tk.Button(self, text="Show my friends", command=self.user_friends, bg="blue", fg="white", font=12)
        self.show_friends.pack(pady=5)
        self.post_content_frame = tk.Frame(self, bg="white")
        self.post_content_frame.pack()

    def show_my_posts(self):
        self.post_content_frame.destroy()
        self.post_content_frame = tk.Frame(self, bg="white")
        self.post_content_frame.pack()

        current_user = self.app.current_user
        if current_user in self.feed:
            for post in self.feed[current_user]:
                post_content = tk.Label(self.post_content_frame, text=f"{post}\n_______________", bg="white", font=("Helvetica", 12))
                post_content.pack(anchor='w')

    def load_friends(self):
        file = open("friends.json", 'r')
        friends = json.load(file)
        file.close()
        return friends

    def user_friends(self):
        self.post_content_frame.destroy()
        self.post_content_frame = tk.Frame(self, bg="white")
        self.post_content_frame.pack()
        friends = self.load_friends()

        current_user = self.app.current_user
        if current_user in friends:
            for friend in friends[current_user]:
                post_content = tk.Label(self.post_content_frame, text=f"{friend}\n_______________", bg="white",
                                        font=("Helvetica", 12))
                post_content.pack(anchor='w')

    def post(self):
        self.post_content_frame.destroy()
        self.post_content_frame = tk.Frame(self, bg="white")
        self.post_content_frame.pack()
        self.text_label = tk.Label(self.post_content_frame, text="Enter your text:", bg="white", font=("Helvetica", 12))
        self.text_label.pack()
        self.text_entry = tk.Entry(self.post_content_frame)
        self.text_entry.pack()
        post_button = tk.Button(self.post_content_frame, text="Post", command=self.submit_post, bg="blue", fg="white", font=12)
        post_button.pack()

    def submit_post(self):
        current_user = self.app.current_user
        user_text = self.text_entry.get()
        if user_text:
            self.load_user_posts()
            if current_user in self.feed:
                self.feed[current_user].insert(0, user_text)
            else:
                self.feed[current_user] = [user_text]

            self.save_users_posts()

            messagebox.showinfo("Success", "posted successfully.")
        else:
            messagebox.showerror("Error", "Enter a text.")



    def go_back(self):
        self.app.show_previous_page()

    def load_user_posts(self):
        try:
            with open("feed.json", "r") as file:
                self.feed = json.load(file)
        except FileNotFoundError:
            self.feed = []

    def save_users_posts(self):
        with open("feed.json", "w") as file:
            json.dump(self.feed, file, indent=2)


