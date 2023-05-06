# Import
import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import gen


# Function to create password
def get_password():
    password.configure(
        text=(
            "Your password is: '" +
            gen.password_gen(int(length_entry.get()), var_1.get() == 1, var_2.get() == 1, var_3.get() == 1, var_4.get() == 1)
            +
            "'"))
    password.pack(pady=15)


# Window
window = ttk.Window(themename="darkly")
window.title("Password Generator")
window.geometry('435x435')
style = ttk.Style()
style.configure("TButton", font=("Courier", 10))
style.configure("TCheckbutton", font=("Courier", 10))

# Widgets
frame = ttk.Frame(window)
frame.pack(pady=20)
title = ttk.Label(frame, text="PASSWORD GENERATOR", font=("Courier", 17))
title.pack(pady=25)
length = ttk.Frame(frame)
length_txt = ttk.Label(length, text="Length", font=("Courier", 10))
length_entry = ttk.Entry(length, font=("Courier", 10), justify=CENTER, bootstyle="dark")
var_1 = tk.IntVar()
upper = ttk.Checkbutton(frame, text="Include Uppercase", variable=var_1,  onvalue=1, offvalue=0, bootstyle="dark")
var_2 = tk.IntVar()
lower = ttk.Checkbutton(frame, text="Include Lowercase", variable=var_2, onvalue=1, offvalue=0, bootstyle="dark")
var_3 = tk.IntVar()
number = ttk.Checkbutton(frame, text="Include Integers", variable=var_3, onvalue=1, offvalue=0, bootstyle="dark")
var_4 = tk.IntVar()
symbol = ttk.Checkbutton(frame, text="Include Symbols", variable=var_4, onvalue=1, offvalue=0, bootstyle="dark")
button = ttk.Button(frame, text="Create", command=get_password, width=10, bootstyle="dark")
password = ttk.Label(frame, text="", font=("Courier", 10))

# Packing the widgets on to the screen
length.pack()
length_txt.pack(side=LEFT, padx=5)
length_entry.pack(side=LEFT, pady=7)
upper.pack(pady=7)
lower.pack(pady=7)
number.pack(pady=7)
symbol.pack(pady=7)
button.pack(pady=7)

# Mainloop
window.mainloop()
