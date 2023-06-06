import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("book review app")
window.geometry('640x480')
window.resizable(True, True)





test_button = ttk.Button(window, text="press", command=lambda: window.quit())
test_button.pack(ipadx=10 , ipady=15 , expand=True)
window.mainloop()
