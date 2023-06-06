import tkinter as tk
from tkinter import messagebox
import sqlite3


# Function to add a book
def add_book():
    title = title_entry.get()
    author = author_entry.get()
    comment = comment_entry.get()

    if title and author:
        conn = sqlite3.connect('bookfriends.db')
        c = conn.cursor()
        c.execute("INSERT INTO Book (title, author, comment) VALUES (?, ?, ?)",
                  (title, author, comment))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Book added successfully.")
        clear_entries()
    else:
        messagebox.showerror("Error", "Title and author fields are required.")


# Function to delete a book
def delete_book():
    book_id = book_id_entry.get()

    if book_id:
        conn = sqlite3.connect('bookfriends.db')
        c = conn.cursor()
        c.execute("DELETE FROM Book WHERE id=?", (book_id,))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Book deleted successfully.")
        clear_entries()
    else:
        messagebox.showerror("Error", "Book ID field is required.")



# Function to clear entry fields
def clear_entries():
    title_entry.delete(0, tk.END)
    author_entry.delete(0, tk.END)
    book_id_entry.delete(0, tk.END)
    comment_entry.delete(0, tk.END)


# Create the main window
window = tk.Tk()
window.title("Book Manager")

# Create labels and entry fields
title_label = tk.Label(window, text="Title:")
title_label.pack()
title_entry = tk.Entry(window)
title_entry.pack()

author_label = tk.Label(window, text="Author:")
author_label.pack()
author_entry = tk.Entry(window)
author_entry.pack()

book_id_label = tk.Label(window, text="Book ID:")
book_id_label.pack()
book_id_entry = tk.Entry(window)
book_id_entry.pack()

comment_label = tk.Label(window, text="Comment:")
comment_label.pack()
comment_entry = tk.Entry(window)
comment_entry.pack()

# Create buttons
add_button = tk.Button(window, text="Add Book", command=add_book)
add_button.pack()

delete_button = tk.Button(window, text="Delete Book", command=delete_book)
delete_button.pack()




# Start the main loop
window.mainloop()