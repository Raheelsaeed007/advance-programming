# importing tkinter
import tkinter as tk

def capital_letters():
    user_input = entry.get() # getting input from the user
    capital_text = user_input.upper()

    result_label.config(text=capital_text)

root= tk.Tk()
root.title("Capital Letters")

entry = tk.Entry(root)
entry.pack()

#creating button
capital_button = tk.Button(root, text="Capitalize", command=capital_letters, bg="skyblue")
capital_button.pack()

# creating label
result_label = tk.Label(root)
result_label.pack()

root.mainloop()