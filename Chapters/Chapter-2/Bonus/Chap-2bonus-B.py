# importing libraries
import tkinter as tk
from datetime import datetime

# defining the function
def calculate_age():
    try:
        dob = datetime.strptime(entry.get(), "%d/%m/%Y")
        today = datetime.today()
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
        result_label.config(text=f"Your age is {age} years")
    except ValueError:
        result_label.config(text="Please enter date in DD/MM/YYYY format")

root = tk.Tk()
root.title("Age Calculator")

frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

entry = tk.Entry(frame)
entry.grid(row=0, column=0, padx=5, pady=5)

calculate_button = tk.Button(frame, text="Calculate Age", command=calculate_age, background='green')
calculate_button.grid(row=1, padx=5, pady=10)

result_label = tk.Label(frame, text="Your age is: ")
result_label.grid(row=2)
# Running the main loop
root.mainloop()