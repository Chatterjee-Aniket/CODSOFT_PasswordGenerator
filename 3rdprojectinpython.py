# Task 3:-
# Password Generator Tool:-
# Program Implementation:-
import tkinter as tk
import random
import string

# Exception Handling syntax would be introduced & within this if-else Syntax would be used below:-

def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            result_label.config(text="Password length should be a positive integer.")
            return
        else:
            characters = string.ascii_letters + string.digits + string.punctuation
            password = ''.join(random.choice(characters) for _ in range(length))
            result_label.config(text=f"Generated Password: {password}")
    except ValueError:
        result_label.config(text="Invalid input. Please enter a valid integer for password length.")

# Create the main window
root = tk.Tk()
root.title("PASSWORD GENERATOR TOOL")

# Create and configure widgets
length_label = tk.Label(root, text="Enter the Password Length:")
length_label.pack()

length_entry = tk.Entry(root)
length_entry.pack()

generate_button = tk.Button(root, text="Generate Password BUTTON", command=generate_password)
generate_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
