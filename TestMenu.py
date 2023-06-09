import tkinter as tk
from tkinter import messagebox

# Function to handle button clicks
def add_book():
    messagebox.showinfo("Add Book", "Add Book functionality will be implemented here.")

def delete_book():
    messagebox.showinfo("Delete Book", "Delete Book functionality will be implemented here.")

def view_books():
    messagebox.showinfo("View Books", "View Books functionality will be implemented here.")

# Create main window
window = tk.Tk()
window.title("Book Management")

# Create menu bar
menu_bar = tk.Menu(window)

# Create file menu
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Exit", command=window.quit)
menu_bar.add_cascade(label="File", menu=file_menu)

# Create book menu
book_menu = tk.Menu(menu_bar, tearoff=0)
book_menu.add_command(label="Add Book", command=add_book)
book_menu.add_command(label="Delete Book", command=delete_book)
book_menu.add_command(label="View Books", command=view_books)
menu_bar.add_cascade(label="Books", menu=book_menu)

# Add menu bar to the window
window.config(menu=menu_bar)

# Start the main event loop
window.mainloop()
