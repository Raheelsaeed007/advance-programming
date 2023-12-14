import tkinter as tk

# defining the function
def login():
    username = username_entry.get()
    password = password_entry.get()
    print(f"Username: {username}, Password:{password}")

root=tk.Tk()
root.title("Login Page")
# Creating labels for the username and password
username_label = tk.Label(root, text="Username:")
password_label = tk.Label(root, text="Password:")
username_entry = tk.Entry(root)
password_entry = tk.Entry(root, show="*") # astersick for passsword

# username and password label and entry
username_label.grid(row=0, column=0)
username_entry.grid(row=0, column=1)
password_label.grid(row=1, column=0)
password_entry.grid(row=1, column=1)

# creating button 
button = tk.Button(root, text="Login", command=login)
button.grid(row=2, columnspan=2)
root.mainloop()