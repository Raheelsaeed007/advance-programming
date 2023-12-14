# importing tkinkter
import tkinter as tk

def font():
    label.config(font='Arial') # changing font

root=tk.Tk()
root.title("GUI")

# creating a label with welcome message
label=tk.Label(root, text="Welcome to GUI")
label.pack()

# button
button=tk.Button(root, text="Change Font", command=font)
button.pack()

root.geometry("400x300")
# Disable the resizeable option
root.resizable(False, False)

# bg color
root.config(background='Blue')

root.mainloop()