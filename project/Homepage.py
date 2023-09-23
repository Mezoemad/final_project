import tkinter as tk
from tkinter import messagebox
import json

class HomePage(tk.Frame):
    def __init__(self, root, app):
        tk.Frame.__init__(self, root, width=1000, height=800, bg="white")
        self.pack_propagate(0)
        self.root = root
        self.app = app
        self.search_result = []
        self.likes = {}
        self.create_widgets()

    def create_widgets(self):
        self.draw_posts(self.load_feed())
        self.nav = tk.Frame(self, width=120, bg='light blue')

        self.nav.pack_propagate(0)
        self.nav.place(relx=0, rely=0, relheight=1)

        self.back_button = tk.Button(self.nav, text="Back", command=self.go_back, padx=30, bg="blue", fg="white", font=12)
        self.back_button.pack()

        self.profile_button = tk.Button(self.nav, text="profile page", command=self.profile, padx=30, bg="blue", fg="white", font=12)
        self.profile_button.pack(pady=20)

        self.entry = tk.Entry(self.nav, bg="white")
        self.entry.pack()

        self.search_button = tk.Button(self.nav, text="Search post", padx=30, bg="blue", fg="white", font=12, command=self.search_post)
        self.search_button.pack(pady=20)

        self.search_friend = tk.Button(self.nav, text="Search friend", bg="blue", fg="white", font=12, command=self.search_friend)
        self.search_friend.pack(pady=20)

    def profile(self):
        self.app.show_page("Profilepage")

    def go_back(self):
        self.app.show_previous_page()

    def load_feed(self):
        handler = open("feed.json", 'r')
        feed_posts = json.load(handler)
        handler.close()
        return feed_posts

    def load_friends(self):
        file = open("friends.json", 'r')
        friends = json.load(file)
        file.close()
        return friends

    def search_post(self):
        search_post = self.entry.get()
        feed = self.load_feed()
        for item in self.search_result:
            item.destroy()
        found_post = self.linear_search(feed, search_post)
        if found_post:
            for account, post in found_post:
                found_post_label = tk.Label(self, text=f"account: {account}\npost: {post}\n_______________", font=("Helvetica", 11), bg="white")
                found_post_label.pack()
                self.search_result.append(found_post_label)
        else:
            messagebox.showerror("Search Result", "Post not found.")

    def search_friend(self):
        search_friend = self.entry.get()
        friends = self.load_friends()
        for item in self.search_result:
            item.destroy()
        found_friend = self.linear_search(friends, search_friend)
        if found_friend:
            for friend in found_friend:
                found_friend_label = tk.Label(self, text=f"account: {friend[1]}\n_______________", font=("Helvetica", 11), bg="white")
                found_friend_label.pack()
                add_friend_button = tk.Button(self, text="Add Friend", command=lambda friend=friend[1]: self.add_friend(friend))
                add_friend_button.pack()
                self.search_result.append(found_friend_label)
                break
        else:
            messagebox.showerror("Search Result", "friend not found.")

    def linear_search(self, feed, search_item):
        result = []
        for account in feed:
            for post in feed[account]:
                if search_item == post:
                    result.append((account, post))
        return result

    def add_friend(self, friend_name):
        current_user = self.app.current_user
        try:
            friends_data = self.load_friends()
        except FileNotFoundError:
            friends_data = {}

        if current_user in friends_data and friend_name in friends_data[current_user]:
            messagebox.showinfo("Friend request", f"You are already friends with {friend_name}.")
        else:
            if current_user not in friends_data:
                friends_data[current_user] = []
                friends_data[current_user].append(friend_name)
                friends_data[friend_name].append(current_user)
            else:
                if friend_name in friends_data:
                    friends_data[current_user].append(friend_name)
                    friends_data[friend_name].append(current_user)
                else:
                    friends_data[friend_name] = []
                    friends_data[friend_name].append(current_user)
                    friends_data[current_user].append(friend_name)

            with open("friends.json", "w") as friends_file:
                json.dump(friends_data, friends_file, indent=2)

                messagebox.showinfo("Friend Request", f"You added {friend_name} to your friends.")

    def like_post(self, account, post_id, like_label):
        if account not in self.likes:
            self.likes[account] = {}
        if post_id not in self.likes[account]:
            self.likes[account][post_id] = 1
            print(post_id)
        like_label.config(text=f"{self.likes[account][post_id]} like")



    def draw_posts(self, feed_posts):

        my_canvas = tk.Canvas(self, bg='white')
        my_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

        my_scrollbar = tk.Scrollbar(self, orient=tk.VERTICAL, command=my_canvas.yview)
        my_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        my_canvas.configure(yscrollcommand=my_scrollbar.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox('all')))

        self.feed = tk.Frame(my_canvas, width=500, height=5000, bg="white")
        my_canvas.create_window(500, 0, window=self.feed)

        friends = self.load_friends()
        for account in feed_posts:
            if self.app.current_user in friends and account in friends[self.app.current_user] or account == self.app.current_user:
                post_frame = tk.Frame(self.feed, bg="white")
                post_frame.pack(pady=20)
                for post_id, post in enumerate(feed_posts[account]):
                    account_name = tk.Label(post_frame, text=f"{account} post: ", font=("Helvetica", 11), bg="white")
                    account_name.pack(anchor='w')

                    post_content = tk.Label(post_frame, text=f"{post}\n\n____________________________\n\n", font=("Helvetica", 11), bg="white")
                    post_content.pack()

                    like_label = tk.Label(post_frame, text=f"0 like", font=("Helvetica", 11), bg="white")
                    like_label.pack()

                    like_button = tk.Button(post_frame, text="Like", font=("Helvetica", 8), bg="white", command=lambda post_id2=post_id, label=like_label: self.like_post(account, post_id2, like_label))
                    like_button.pack()




