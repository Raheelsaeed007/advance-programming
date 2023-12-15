# importing libraries
import tkinter as tk
from tkinter import messagebox

# the menu or order that will be displayed
def order():
    message = f"You've selected {coffee_var.get()} with {sugar_var.get()} sugar and {milk_var.get()} milk."
    messagebox.showinfo("Order Summary", message)

# Create main window
root = tk.Tk()
root.title("Coffee Vending Machine")

# Load and set background image
bg_image = tk.PhotoImage(file="coffee3.png")  # An image displayed
bg_label = tk.Label(root, image=bg_image)
bg_label.place(relwidth=1, relheight=1)

# Coffee selection
coffee_var = tk.StringVar()
coffee_var.set("Espresso")  # Default selection
coffee_label = tk.Label(root, text="Select Coffee:")
coffee_label.pack()
coffee_menu = tk.OptionMenu(root, coffee_var, "Espresso", "Latte", "Cappuccino") # values
coffee_menu.pack()

# Sugar selection
sugar_var = tk.StringVar()
sugar_var.set("No")  # Default selection
sugar_label = tk.Label(root, text="Add Sugar?")
sugar_label.pack()
sugar_menu = tk.OptionMenu(root, sugar_var, "No", "Yes")
sugar_menu.pack()

# Milk selection
milk_var = tk.StringVar()
milk_var.set("No")  # Default selection
milk_label = tk.Label(root, text="Add Milk?")
milk_label.pack()
milk_menu = tk.OptionMenu(root, milk_var, "No", "Yes")
milk_menu.pack()

# Submit with the button
submit_button = tk.Button(root, text="Place Order", command=order)
submit_button.pack()

# running the main loop
root.mainloop()

