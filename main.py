import tkinter as tk  # Εισαγωγή της βιβλιοθήκης tkinter
from tkinter import messagebox  # Κι απο την tkinter το messageBox
import sqlite3  # Εισαγωγή της SQLite χρήση ΒΔ

# Create a connection to the SQLite database
conn = sqlite3.connect(
    'bookfriends.db')  # Δημιουργώ ένα αντικείμενο connection της βάσης και συνδέομαι με την bookfriends.db
cursor = conn.cursor()  # O cursor είναι πάντα υπεύθυνος για να τρέχει τα queries


class Book:  # Δημιουργία class για το βιβλίο
    def __init__(self, isbn, title, author, category, language):  # Constructor για το Book
        self.root.isbn = isbn
        self.root.title = title
        self.root.author = author
        self.root.category = category
        self.root.language = language


class User:  # Δημιουργία class για το User
    def __init__(self, username, password, name, surname):  # Constructor για το User
        self.root.username = username
        self.root.password = password
        self.root.name = name
        self.root.surname = surname


class BookReview:  # Δημιουργία class για το Review
    def __init__(self, Book_ISBN, user_username, comment, review):  # Constructor για το Review
        self.root.Book_ISBN = Book_ISBN
        self.root.user_username = user_username
        self.root.comment = comment
        self.root.review = review


class BookManagementApp():  # Δημιουργία της class για να δουλέψουν όλα μαζί.
    def __init__(self):
        self.root = tk.Tk()  # To κύριο παράθυρο του γραφικού
        self.root.title("Book Management")
        self.root.geometry("400x300")
        nameOfUser = ""

        # Create menu bar
        self.menu_bar = tk.Menu(self.root)  # H μπάρα του menu

        # Create File menu
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)  # Δημιουργία File tab στην μπάρα
        self.file_menu.add_command(label="Exit", command=self.root.quit)  # Η λειτουργία του (Έξοδος)

        # Add menus to the menu bar
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)  # Προσθήκη στην μπάρα του tab

        # Set the default menu bar
        self.root.config(menu=self.menu_bar)

        self.login_frame = tk.Frame(self.root)  # Δημιουργία login φόρμας
        message = "Welcome to the Book Review App. Please login!"
        self.message_label = tk.Label(self.login_frame, text=message)
        self.username_label = tk.Label(self.login_frame, text="Username:")
        self.username_entry = tk.Entry(self.login_frame)
        self.password_label = tk.Label(self.login_frame, text="Password:")
        self.password_entry = tk.Entry(self.login_frame, show="*")
        self.login_button = tk.Button(self.login_frame, text="Login", command=self.login)

        # Positioning στοιχείων login φόρμας  σε πλέγμα (grid)
        self.message_label.grid(row=0, column=2, sticky="e")
        self.username_label.grid(row=2, column=1, sticky="e")
        self.username_entry.grid(row=2, column=2)
        self.password_label.grid(row=3, column=1, sticky="e")
        self.password_entry.grid(row=3, column=2)
        self.login_button.grid(row=4, column=2, pady=10)
        self.login_frame.pack(pady=50)

    def login(self):  # Διαδικασία Login
        username = self.username_entry.get()  # Πάρε το value απο το πεδίο
        password = self.password_entry.get()  # Πάρε το value απο το πεδίο

        # Ερώτημα στην database if the user exists
        cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        user = cursor.fetchone()

        if user:  # Αφού έχουμε επιτυχές login
            self.nameOfUser = username  # Μετέφερε το username του χρήστη όσο είναι μέσα
            self.login_frame.destroy()  # Εξαφάνισε τα πεδία του login
            self.file_menu.delete(0, tk.END)  # Διέγραψε το menu προ login έποχής
            self.file_menu.add_command(label="Logout", command=self.logout)  # Πρόσθεσε την επιλογή logout
            self.file_menu.add_separator()
            self.file_menu.add_command(label="Exit", command=self.root.quit)  # και την επιλογή εξόδου απο το πρόγραμμα

            # Δημιουργία Book menu
            self.book_menu = tk.Menu(self.menu_bar, tearoff=0)
            self.book_menu.add_command(label="Add Book", command=self.show_add_book)  # Προσθήκη Βιβλίου
            self.book_menu.add_command(label="Review Book", command=self.show_add_bookReview)  # Review Βιβλίου
            self.book_menu.add_command(label="View All Books",
                                       command=self.show_view_all_books)  # Προβολή όλων τψν βιβλίων
            self.menu_bar.add_cascade(label="Book", menu=self.book_menu)  # προσθεσέ τα όλα στο μενού.

            self.main_frame = tk.Frame(self.root)
            message = "Welcome " + self.nameOfUser + " ! Please Select from the menu bar your choice"  # Καλωσορίζουμε τον χρήστη
            self.message_label = tk.Label(self.main_frame, text=message)
            self.message_label.grid(row=3, column=2)
            self.main_frame.pack(pady=50)
            return self.nameOfUser  # Επιστρέφω το username για να μπορεί να το χρησιμοποιήσει οποιαδήποτε function της class μου.

        else:  # Αν τα credentials είναι λάθος τότε:
            messagebox.showerror("Login Error", "Invalid username or password.")

    def show_add_book(self):  # Δημιουργία γραφικού για Προσθήκη βιβλίου
        add_book_window = tk.Toplevel(self.root)
        add_book_window.title("Add Book")
        add_book_window.geometry("500x300")

        # Δημιουργία πεδίων και ετικετών
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

        # Δημιουργία κουμπιού και ανάθεση στην function add_book()
        self.root.add_book_button = tk.Button(add_book_window, text="Add Book", command=self.add_book)
        self.root.add_book_button.pack()

    def show_add_bookReview(self):  # Δημιουργία γραφικού για Προσθήκη Κριτικής
        add_bookReview_window = tk.Toplevel(self.root)
        add_bookReview_window.title("Add Book Review")
        add_bookReview_window.geometry("500x300")

        # Δημιουργία πεδίων και ετικετών
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

        # Δημιουργία κουμπιού και ανάθεση στην function add_book_review()
        self.root.add_book_review_button = tk.Button(add_bookReview_window, text="Add Review",
                                                     command=self.add_book_review)
        self.root.add_book_review_button.pack()

    def show_view_all_books(self):  # Δημιουργία γραφικού για Προσθήκη βιβλίου
        view_all_books_window = tk.Toplevel(self.root)
        view_all_books_window.title("View All Books")
        view_all_books_window.geometry("640x480")
        text_widget = tk.Text(view_all_books_window)
        text_widget.pack()
        #Φέρε απο την Βάση όλα τα βιβλία
        cursor.execute("SELECT ISBN, title, author, category, language FROM Book")
        books = cursor.fetchall()
        # Εκτύπωσέ μου τα σε readable μορφή. Και σε ξεχωριστό text.widget για να μπορεί ο χρήστης εύκολα
        # να πάρει copy-paste το ISBN αν θέλει να προσθέσει review.
        for book in books:
            text_widget.insert(tk.END, f"ISBN: {book[0]}\n")
            text_widget.insert(tk.END, f"Title: {book[1]}\n")
            text_widget.insert(tk.END, f"Author: {book[2]}\n")
            text_widget.insert(tk.END, f"Category: {book[3]}\n")
            text_widget.insert(tk.END, f"Language: {book[4]}\n\n")


    def add_book(self): #Προσθήκη βιβλίου
        #Πάρε τις τιμές απο τα πεδία
        isbn = self.root.isbn_entry.get()
        title = self.root.title_entry.get()
        author = self.root.author_entry.get()
        language = self.root.language_entry.get()
        category = self.root.category_entry.get()

        # Κάνε Insert στον πίνακα ένα νέο βιβλίο με τις τιμές απο τα πεδία που πήρες.
        cursor.execute("INSERT INTO book VALUES (?, ?, ?, ?, ?)", (isbn, title, author, language, category))
        conn.commit()

        #Αδειάζεις τη φόρμα για να είναι έτοιμη για νέα προσθήκη.
        self.root.isbn_entry.delete(0, tk.END)
        self.root.title_entry.delete(0, tk.END)
        self.root.author_entry.delete(0, tk.END)
        self.root.language_entry.delete(0, tk.END)
        self.root.category_entry.delete(0, tk.END)

        #Ενημερωτικό μήνυμα στο χρήστη για επιτυχή καταχώρηση
        messagebox.showinfo("Success", "Book added successfully.")

    def add_book_review(self): #Προσθήκη κριτικής Βιβλίου

        book_isbn = self.root.book_isbn_entry.get()
        review = self.root.review_entry.get()
        comment = self.root.comment_entry.get()
        #Πάρε το username του χρήστη που είναι logged in.
        user_username = self.nameOfUser

        # Κάνε insert μια νέα κριτική με τιμές των ανωτέρω πεδίων.
        cursor.execute("INSERT INTO BookReviews VALUES (?, ?, ?, ?)", (book_isbn, review, comment, user_username))
        conn.commit()

        # Αδειάζεις τη φόρμα για να είναι έτοιμη για νέα προσθήκη.
        self.root.book_isbn_entry.delete(0, tk.END)
        self.root.review_entry.delete(0, tk.END)
        self.root.comment_entry.delete(0, tk.END)

        messagebox.showinfo("Success", "Book Review added successfully.")

    def logout(self): #Logout Function
        # Επαναφορά όλου του μενού και δημιουργία ξανά login φόμρας
        self.menu_bar.delete("Book") #Διαγραφή των επιλογών για βιβλία-Αποκλεισμός του χρήστη απο λειτουργίες βιβλίων.
        self.file_menu.delete(0, tk.END)
        self.file_menu.add_command(label="Exit", command=self.root.quit)

        # δημιουργία ξανά login φόμρας
        self.login_frame = tk.Frame(self.root)
        self.username_label = tk.Label(self.login_frame, text="Username:")
        self.username_entry = tk.Entry(self.login_frame)
        self.password_label = tk.Label(self.login_frame, text="Password:")
        self.password_entry = tk.Entry(self.login_frame, show="*")
        self.login_button = tk.Button(self.login_frame, text="Login", command=self.login)

        # Positioning στοιχείων login φόρμας  σε πλέγμα (grid)
        self.message_label.grid(row=0, column=2, sticky="e")
        self.username_label.grid(row=2, column=1, sticky="e")
        self.username_entry.grid(row=2, column=2)
        self.password_label.grid(row=3, column=1, sticky="e")
        self.password_entry.grid(row=3, column=2)
        self.login_button.grid(row=4, column=2, pady=10)
        self.login_frame.pack(pady=50)

    def run(self): #Δημιοργία της run για έναρξη όλων
        self.root.mainloop()


app = BookManagementApp() #το app ένα νέο αντικείμενο BookManagementApp
app.run() #Αpp Ξεκίνα!
