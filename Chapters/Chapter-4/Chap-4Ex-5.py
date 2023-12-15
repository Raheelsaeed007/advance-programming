# import tkinter
import tkinter as tk
from tkinter import messagebox

def password():
    password = password_entry.get()

    # Password criteria as given in the excercise
    lowercase = any(c.islower() for c in password)
    uppercase = any(c.isupper() for c in password)
    digits = any(c.isdigit() for c in password)
    special_char = any(c in '$#@' for c in password)
    length = 6 <= len(password) <= 12

    # nested if statements to check whether all criteria are fulfilled
    if lowercase and uppercase and digits and special_char and length:
        messagebox.showinfo("Success", "Password is valid!")
        root.destroy()
    else:
        attempts_left[0] -= 1
        if attempts_left[0] > 0:
            messagebox.showwarning("Invalid Password",
                                   f"Invalid password. Attempts left: {attempts_left[0]}")
        else:
            messagebox.showerror("Alert!", "Authorities have been alerted!")
            root.destroy()


# The password attempts details
attempts_left = [5]

root = tk.Tk()
root.title("Password Validator")

# Creating the label for the password
password_label = tk.Label(root, text="Enter Password:")
password_label.pack()

# creating asterisk for hiding the input from the user
password_entry = tk.Entry(root, show='*')
password_entry.pack()

# button and command
validate_button = tk.Button(root, text="Validate", command=password)
validate_button.pack()

root.mainloop()