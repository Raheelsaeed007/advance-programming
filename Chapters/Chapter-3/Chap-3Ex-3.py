# import tkinter
import tkinter as tk
from tkinter import ttk
# import math library
import math

# defining the functions
def circle():
    radius = float(circle_radius_entry.get())
    area = math.pi * radius**2
    circle_result_label.config(text=f"Area of Circle: {area:.2f} sq units")

def square():
    side_length = float(square_side_entry.get())
    area = side_length**2
    square_result_label.config(text=f"Area of Square: {area:.2f} sq units")

def rectangle():
    length = float(rectangle_length_entry.get())
    width = float(rectangle_width_entry.get())
    area = length * width
    rectangle_result_label.config(text=f"Area of Rectangle: {area:.2f} sq units")

root = tk.Tk()
root.title("Shapes")

# Creating Tabbed Interface
notebook = ttk.Notebook(root)
notebook.pack(padx=10, pady=10)

# Circle Tab
circle_tab = ttk.Frame(notebook)
notebook.add(circle_tab, text='Circle')

circle_radius_label = tk.Label(circle_tab, text="Enter radius:")
circle_radius_label.pack()

circle_radius_entry = tk.Entry(circle_tab)
circle_radius_entry.pack()

circle_calculate_button = tk.Button(circle_tab, text="Calculate", command=circle, bg="green")
circle_calculate_button.pack()

circle_result_label = tk.Label(circle_tab, text="")
circle_result_label.pack()

# Square Tab
square_tab = ttk.Frame(notebook)
notebook.add(square_tab, text='Square')

square_side_label = tk.Label(square_tab, text="Enter side length:")
square_side_label.pack()

square_side_entry = tk.Entry(square_tab)
square_side_entry.pack()

square_calculate_button = tk.Button(square_tab, text="Calculate", command=square, bg="green")
square_calculate_button.pack()

square_result_label = tk.Label(square_tab, text="")
square_result_label.pack()

# Rectangle Tab
rectangle_tab = ttk.Frame(notebook)
notebook.add(rectangle_tab, text='Rectangle')

rectangle_length_label = tk.Label(rectangle_tab, text="Enter length:")
rectangle_length_label.pack()

rectangle_length_entry = tk.Entry(rectangle_tab)
rectangle_length_entry.pack()

rectangle_width_label = tk.Label(rectangle_tab, text="Enter width:")
rectangle_width_label.pack()

rectangle_width_entry = tk.Entry(rectangle_tab)
rectangle_width_entry.pack() # using pack

rectangle_calculate_button = tk.Button(rectangle_tab, text="Calculate", command=rectangle,bg="green") # button
rectangle_calculate_button.pack()

rectangle_result_label = tk.Label(rectangle_tab, text="")
rectangle_result_label.pack() # using pack

# running the main loop
root.mainloop()

