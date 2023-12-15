# importing tkinter
import tkinter as tk

def greeting():
    name = name_entry.get() # getting input from the user
    selected_color = color_var.get()
    greeting_label.config(text=f"Hello, {name}!", fg=selected_color)

root = tk.Tk()
root.title("Greeting App")  # title for the main window

# InputFrame as per the requirement
input_frame = tk.Frame(root, bg="blue", padx=10, pady=10)
input_frame.pack(padx=10, pady=10, side=tk.LEFT)

title_label = tk.Label(input_frame, text="Greeting App", fg="orange", font=("Arial", 16), pady=10)
title_label.pack()

name_label = tk.Label(input_frame, text="Enter your name:")
name_label.pack()

name_entry = tk.Entry(input_frame)
name_entry.pack()

color_label = tk.Label(input_frame, text="Select text color:")
color_label.pack()

colors = ['black', 'red', 'green', 'blue', 'purple']  # Option for colors
color_var = tk.StringVar(root)
color_var.set(colors[0])  # Set default color(black)

dropdown = tk.OptionMenu(input_frame, color_var, *colors)
dropdown.pack()

update_button = tk.Button(input_frame, text="Update Greeting", command=greeting)
update_button.pack()

# DisplayFrame as per the requirement
display_frame = tk.Frame(root, bg="orange", padx=20, pady=20)
display_frame.pack(padx=10, pady=10, side=tk.RIGHT)

greeting_label = tk.Label(display_frame, text="", font=("Arial", 12))
greeting_label.pack()

# Run the GUI
root.mainloop()