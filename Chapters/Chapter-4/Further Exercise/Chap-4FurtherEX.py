# importing tkinter and regular expressions module
import tkinter as tk
import re

# defining the options
def numbers_underscore():
    pattern = r'^[a-zA-Z0-9_]+$'
    check_pattern(pattern)

def specific_number():
    pattern = r'^7\d+'
    check_pattern(pattern)

def substrings():
    pattern = r'\b\w{3}\b'
    check_pattern(pattern)

def beginning():
    pattern = r'^Hello\b'
    check_pattern(pattern)

def check_pattern(pattern):
    user_input = entry.get()
    match = re.search(pattern, user_input)
    if match:
        result_label.config(text=f"Input matches the pattern: {pattern}")
    else:
        result_label.config(text=f"Input does not match the pattern: {pattern}")

root = tk.Tk()
root.title("Regular Expression")

# creating label for the entry of data
entry_label = tk.Label(root, text="Enter Text:")
entry_label.pack()

entry = tk.Entry(root)
entry.pack()

# creating buttons for each operation
underscore_button = tk.Button(root, text="Check: Letters, Numbers, Underscores", command=numbers_underscore)
underscore_button.pack()

specific_number_button = tk.Button(root, text="Check: Starts with Specific Number", command=specific_number)
specific_number_button.pack()

substrings_button = tk.Button(root, text="Find Substrings (3 characters long)", command=substrings)
substrings_button.pack()

beginning_button = tk.Button(root, text="Match Word at Beginning (Hello)", command=beginning)
beginning_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()