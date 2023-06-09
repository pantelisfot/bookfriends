import tkinter as tk
from tkinter import messagebox
import sqlite3

# Create a connection to the SQLite database
conn = sqlite3.connect('bookfriends.db')
cursor = conn.cursor()

# Create a table to store book
cursor.execute('''CREATE TABLE IF NOT EXISTS book
                  (isbn TEXT, title TEXT, author TEXT, category TEXT, language TEXT)''')

# Create a table to store users
cursor.execute('''CREATE TABLE IF NOT EXISTS users
                  (username TEXT, password TEXT, name TEXT, surname TEXT)''')

# Create a table to store book reviews
cursor.execute('''CREATE TABLE IF NOT EXISTS bookreviews
                  (isbn TEXT, username TEXT, comment TEXT, review TEXT)''')


class Book:
    def __init__(self, isbn, title, author, category, language):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.category = category
        self.language = language


class User:
    def __init__(self, username, password, name, surname):
        self.username = username
        self.password = password
        self.name = name
        self.surname = surname


class BookReview:
    def __init__(self, Book_ISBN, user_username, comment, review):
        self.Book_ISBN = Book_ISBN
        self.user_username = user_username
        self.comment = comment
        self.review = review


class LibraryApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Library App")
        self.geometry("500x300")
        self.resizable(False, False)

        self.username_label = tk.Label(self, text="Username:")
        self.username_label.pack()
        self.username_entry = tk.Entry(self)
        self.username_entry.pack()

        self.password_label = tk.Label(self, text="Password:")
        self.password_label.pack()
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack()

        self.login_button = tk.Button(self, text="Login", command=self.login)
        self.login_button.pack()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Query the database to check if the user exists
        cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        user = cursor.fetchone()

        if user: #If user has logged in succesfully:
            self.username_entry.delete(0, tk.END)
            self.password_entry.delete(0, tk.END)
            self.withdraw()  # Hide the login window
            self.show_add_bookReview()
        else:
            messagebox.showerror("Login Error", "Invalid username or password.")

    def show_book_list(self):
        book_list_window = tk.Toplevel(self)
        book_list_window.title("Book List")
        book_list_window.geometry("500x300")

        # Retrieve the list of books from the database
        cursor.execute("SELECT * FROM book")
        books = cursor.fetchall()

        for book in books:
            isbn, title, author, category, language = book
            book_label = tk.Label(book_list_window, text=f"{title} by {author}")
            book_label.pack()

        self.add_book_button = tk.Button(book_list_window, text="Add Book", command=self.show_add_book)
        self.add_book_button.pack()

    def show_add_book(self):
        add_book_window = tk.Toplevel(self)
        add_book_window.title("Add Book")
        add_book_window.geometry("500x300")

        self.isbn_label = tk.Label(add_book_window, text="ISBN:")
        self.isbn_label.pack()
        self.isbn_entry = tk.Entry(add_book_window)
        self.isbn_entry.pack()

        self.title_label = tk.Label(add_book_window, text="Title:")
        self.title_label.pack()
        self.title_entry = tk.Entry(add_book_window)
        self.title_entry.pack()

        self.author_label = tk.Label(add_book_window, text="Author:")
        self.author_label.pack()
        self.author_entry = tk.Entry(add_book_window)
        self.author_entry.pack()


        self.language_label = tk.Label(add_book_window, text="Language:")
        self.language_label.pack()
        self.language_entry = tk.Entry(add_book_window)
        self.language_entry.pack()

        self.category_label = tk.Label(add_book_window, text="Category:")
        self.category_label.pack()
        self.category_entry = tk.Entry(add_book_window)
        self.category_entry.pack()

        self.add_book_button = tk.Button(add_book_window, text="Add", command=self.add_book)
        self.add_book_button.pack()

    def show_add_bookReview(self):
        add_bookReview_window = tk.Toplevel(self)
        add_bookReview_window.title("Add Book Review")
        add_bookReview_window.geometry("500x300")

        self.book_isbn_label = tk.Label(add_bookReview_window, text="Book ISBN:")
        self.book_isbn_label.pack()
        self.book_isbn_entry = tk.Entry(add_bookReview_window)
        self.book_isbn_entry.pack()

        self.review_label = tk.Label(add_bookReview_window, text="Review from 1 to 5 stars:")
        self.review_label.pack()
        self.review_entry = tk.Entry(add_bookReview_window)
        self.review_entry.pack()

        self.comment_label = tk.Label(add_bookReview_window, text="Comment:")
        self.comment_label.pack()
        self.comment_entry = tk.Entry(add_bookReview_window)
        self.comment_entry.pack()

        self.user_username_label = tk.Label(add_bookReview_window, text="Username:")
        self.user_username_label.pack()
        self.user_username_entry = tk.Entry(add_bookReview_window)
        self.user_username_entry.pack()

        self.add_book_review_button = tk.Button(add_bookReview_window, text="Add Review", command=self.add_book_review)
        self.add_book_review_button.pack()

    def add_book(self):
        isbn = self.isbn_entry.get()
        title = self.title_entry.get()
        author = self.author_entry.get()
        language = self.language_entry.get()
        category = self.category_entry.get()


        # Insert the book into the database
        cursor.execute("INSERT INTO book VALUES (?, ?, ?, ?, ?)", (isbn, title, author, language, category))
        conn.commit()

        self.isbn_entry.delete(0, tk.END)
        self.title_entry.delete(0, tk.END)
        self.author_entry.delete(0, tk.END)
        self.language_entry.delete(0, tk.END)
        self.category_entry.delete(0, tk.END)

        messagebox.showinfo("Success", "Book added successfully.")

    def add_book_review(self):
        book_isbn = self.book_isbn_entry.get()
        review = self.review_entry.get()
        comment = self.comment_entry.get()
        user_username = self.user_username_entry.get()

        # Insert the book into the database
        cursor.execute("INSERT INTO BookReviews VALUES (?, ?, ?, ?)", (book_isbn, review, comment, user_username))
        conn.commit()

        self.book_isbn_entry.delete(0, tk.END)
        self.review_entry.delete(0, tk.END)
        self.comment_entry.delete(0, tk.END)
        self.user_username_entry.delete(0, tk.END)

        messagebox.showinfo("Success", "Book Review added successfully.")

    def start(self):
        self.mainloop()


if __name__ == "__main__":
    app = LibraryApp()
    app.start()
