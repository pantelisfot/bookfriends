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
        self.root.isbn = isbn
        self.root.title = title
        self.root.author = author
        self.root.category = category
        self.root.language = language


class User:
    def __init__(self, username, password, name, surname):
        self.rootusername = username
        self.rootpassword = password
        self.rootname = name
        self.rootsurname = surname


class BookReview:
    def __init__(self, Book_ISBN, user_username, comment, review):
        self.rootBook_ISBN = Book_ISBN
        self.rootuser_username = user_username
        self.rootcomment = comment
        self.rootreview = review


class BookManagementApp():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Book Management")
        self.root.geometry("400x300")

        # Create menu bar
        self.menu_bar = tk.Menu(self.root)

        # Create File menu
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Exit", command=self.root.quit)

        # Add menus to the menu bar
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)

        # Set the default menu bar
        self.root.config(menu=self.menu_bar)

        # Other widgets
        self.login_frame = tk.Frame(self.root)
        self.username_label = tk.Label(self.login_frame, text="Username:")
        self.username_entry = tk.Entry(self.login_frame)
        self.password_label = tk.Label(self.login_frame, text="Password:")
        self.password_entry = tk.Entry(self.login_frame, show="*")
        self.login_button = tk.Button(self.login_frame, text="Login", command=self.login)

        # Position login page widgets
        self.username_label.grid(row=0, column=0, sticky="e")
        self.username_entry.grid(row=0, column=1)
        self.password_label.grid(row=1, column=0, sticky="e")
        self.password_entry.grid(row=1, column=1)
        self.login_button.grid(row=2, column=1, pady=10)
        self.login_frame.pack(pady=50)

    def login(self):  # koumpi Login
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Query the database to check if the user exists
        cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        user = cursor.fetchone()

        if user:  # If user has logged in succesfully:
            self.login_frame.destroy()
            self.file_menu.delete(0, tk.END)
            self.file_menu.add_command(label="Logout", command=self.logout)
            self.file_menu.add_separator()
            self.file_menu.add_command(label="Exit", command=self.root.quit)

            # Create Book menu
            self.book_menu = tk.Menu(self.menu_bar, tearoff=0)
            self.book_menu.add_command(label="Add Book", command=self.show_add_book)
            self.book_menu.add_command(label="Review Book", command=self.show_add_bookReview)
            self.book_menu.add_command(label="View All Books", command=self.show_view_all_books)
            self.book_menu.add_command(label="Delete Book", command="")
            self.menu_bar.add_cascade(label="Book", menu=self.book_menu)

        else:
            messagebox.showerror("Login Error", "Invalid username or password.")

    def show_book_list(self):  # koumpi Show Books
        book_list_window = tk.Toplevel(self.root)
        book_list_window.title("Book List")
        book_list_window.geometry("500x300")

        # Retrieve the list of books from the database
        cursor.execute("SELECT * FROM book")
        books = cursor.fetchall()

        for book in books:
            isbn, title, author, category, language = book
            book_label = tk.Label(book_list_window, text=f"{title} by {author}")
            book_label.pack()

        self.root.add_book_button = tk.Button(book_list_window, text="Add Book", command=self.root.show_add_book)
        self.root.add_book_button.pack()

    def show_add_book(self):  # koumpi Add Book
        add_book_window = tk.Toplevel(self.root)
        add_book_window.title("Add Book")
        add_book_window.geometry("500x300")

        self.root.isbn_label = tk.Label(add_book_window, text="ISBN:")
        self.root.isbn_label.pack()
        self.root.isbn_entry = tk.Entry(add_book_window)
        self.root.isbn_entry.pack()

        self.root.title_label = tk.Label(add_book_window, text="Title:")
        self.root.title_label.pack()
        self.root.title_entry = tk.Entry(add_book_window)
        self.root.title_entry.pack()

        self.root.author_label = tk.Label(add_book_window, text="Author:")
        self.root.author_label.pack()
        self.root.author_entry = tk.Entry(add_book_window)
        self.root.author_entry.pack()

        self.root.language_label = tk.Label(add_book_window, text="Language:")
        self.root.language_label.pack()
        self.root.language_entry = tk.Entry(add_book_window)
        self.root.language_entry.pack()

        self.root.category_label = tk.Label(add_book_window, text="Category:")
        self.root.category_label.pack()
        self.root.category_entry = tk.Entry(add_book_window)
        self.root.category_entry.pack()

        self.root.add_book_button = tk.Button(add_book_window, text="Add Book", command=self.add_book)
        self.root.add_book_button.pack()

    def show_add_bookReview(self):  # koumpi Add Review
        add_bookReview_window = tk.Toplevel(self.root)
        add_bookReview_window.title("Add Book Review")
        add_bookReview_window.geometry("500x300")

        self.root.book_isbn_label = tk.Label(add_bookReview_window, text="Book ISBN:")
        self.root.book_isbn_label.pack()
        self.root.book_isbn_entry = tk.Entry(add_bookReview_window)
        self.root.book_isbn_entry.pack()

        self.root.review_label = tk.Label(add_bookReview_window, text="Review from 1 to 5 stars:")
        self.root.review_label.pack()
        self.root.review_entry = tk.Entry(add_bookReview_window)
        self.root.review_entry.pack()

        self.root.comment_label = tk.Label(add_bookReview_window, text="Comment:")
        self.root.comment_label.pack()
        self.root.comment_entry = tk.Entry(add_bookReview_window)
        self.root.comment_entry.pack()

        self.root.user_username_label = tk.Label(add_bookReview_window, text="Username:")
        self.root.user_username_label.pack()
        self.root.user_username_entry = tk.Entry(add_bookReview_window)
        self.root.user_username_entry.pack()

        self.root.add_book_review_button = tk.Button(add_bookReview_window, text="Add Review",command=self.add_book_review)
        self.root.add_book_review_button.pack()

    def show_view_all_books(self):  # koumpi Add Book
        view_all_books_window = tk.Toplevel(self.root)
        view_all_books_window.title("View All Books")
        view_all_books_window.geometry("640x480")
        text_widget = tk.Text(view_all_books_window)
        text_widget.pack()

        cursor.execute("SELECT ISBN, title, author, category, language FROM Book")
        books = cursor.fetchall()
 #Print all the books
        for book in books:
            text_widget.insert(tk.END, f"ISBN: {book[0]}\n")
            text_widget.insert(tk.END, f"Title: {book[1]}\n")
            text_widget.insert(tk.END, f"Author: {book[2]}\n")
            text_widget.insert(tk.END, f"Category: {book[3]}\n")
            text_widget.insert(tk.END, f"Language: {book[4]}\n\n")

        # Close the database connection
        conn.close()


    def add_book(self):
        isbn = self.root.isbn_entry.get()
        title = self.root.title_entry.get()
        author = self.root.author_entry.get()
        language = self.root.language_entry.get()
        category = self.root.category_entry.get()

        # Insert the book into the database
        cursor.execute("INSERT INTO book VALUES (?, ?, ?, ?, ?)", (isbn, title, author, language, category))
        conn.commit()

        self.root.isbn_entry.delete(0, tk.END)
        self.root.title_entry.delete(0, tk.END)
        self.root.author_entry.delete(0, tk.END)
        self.root.language_entry.delete(0, tk.END)
        self.root.category_entry.delete(0, tk.END)

        messagebox.showinfo("Success", "Book added successfully.")

    def add_book_review(self):
        book_isbn = self.root.book_isbn_entry.get()
        review = self.root.review_entry.get()
        comment = self.root.comment_entry.get()
        user_username = self.root.user_username_entry.get()

        # Insert the book into the database
        cursor.execute("INSERT INTO BookReviews VALUES (?, ?, ?, ?)", (book_isbn, review, comment, user_username))
        conn.commit()

        self.root.book_isbn_entry.delete(0, tk.END)
        self.root.review_entry.delete(0, tk.END)
        self.root.comment_entry.delete(0, tk.END)
        self.root.user_username_entry.delete(0, tk.END)

        messagebox.showinfo("Success", "Book Review added successfully.")


    def logout(self):
        # Reset the menu items and recreate the login page
        self.menu_bar.delete("Book")
        self.file_menu.delete(0, tk.END)
        self.file_menu.add_command(label="Exit", command=self.root.quit)


        # Recreate the login page
        self.login_frame = tk.Frame(self.root)
        self.username_label = tk.Label(self.login_frame, text="Username:")
        self.username_entry = tk.Entry(self.login_frame)
        self.password_label = tk.Label(self.login_frame, text="Password:")
        self.password_entry = tk.Entry(self.login_frame, show="*")
        self.login_button = tk.Button(self.login_frame, text="Login", command=self.login)

        # Position login page widgets
        self.username_label.grid(row=0, column=0, sticky="e")
        self.username_entry.grid(row=0, column=1)
        self.password_label.grid(row=1, column=0, sticky="e")
        self.password_entry.grid(row=1, column=1)
        self.login_button.grid(row=2, column=1, pady=10)
        self.login_frame.pack(pady=50)

    def run(self):
        self.root.mainloop()


app = BookManagementApp()
app.run()