import random
import string
import tkinter as tk
from tkinter import messagebox

#define password generator function.
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

#define 
def generate_button_clicked():
    try:
        desired_length = int(length_entry.get())
        if desired_length <= 0:
            raise ValueError("Entered password length must be a positive integer.")
        
        password = generate_password(desired_length)
        generated_password.set(password)
    except ValueError as ve:
        messagebox.showerror("Error!!!", ve)

def accept_button_clicked():
    user_name = name_entry.get()
    password = generated_password.get()

    if user_name.strip() == "":
        messagebox.showerror("Error", "Please enter your name first.")
    elif password.strip() == "":
        messagebox.showerror("Error", "Please generate a password first.")
    else:
        messagebox.showinfo("Success!!!", f"Hello, {user_name}! The generated password is accepted.Thanks for your patience :)\n{password}")

# Create the main application window(a is reffered as application window)
a = tk.Tk()
a.title("Password Generator")
a.geometry("400x250")

# Heading
heading_label = tk.Label(a, text="Password Generator", font=("Arial", 20, "bold"))
heading_label.grid(row=0, column=0, columnspan=2, pady=10)

# Create the widgets
name_label = tk.Label(a, text="Enter username:")
name_label.grid(row=1, column=0, padx=10, sticky=tk.E)

name_entry = tk.Entry(a)
name_entry.grid(row=1, column=1, padx=10, pady=5, sticky=tk.W)

length_label = tk.Label(a, text="Enter password length:")
length_label.grid(row=2, column=0, padx=10, sticky=tk.E)

length_entry = tk.Entry(a)
length_entry.grid(row=2, column=1, padx=10, pady=5, sticky=tk.W)

generate_button = tk.Button(a, text="Generate Password", command=generate_button_clicked)
generate_button.grid(row=3, column=0, columnspan=2, pady=10)

generated_password = tk.StringVar()
password_label = tk.Entry(a, textvariable=generated_password)
password_label.grid(row=4, column=0, columnspan=2, pady=5)

accept_button = tk.Button(a, text="Accept Password", command=accept_button_clicked)
accept_button.grid(row=5, column=0, columnspan=2, pady=10)

# Adjust column widths to center the widgets
a.grid_columnconfigure(0, weight=1)
a.grid_columnconfigure(1, weight=1)

# Run the application
a.mainloop()
