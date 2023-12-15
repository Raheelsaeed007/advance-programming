# importing tkinter and math library
import tkinter as tk
from math import pi
# creating a main class in which many subclasses are added
class Shape:
    def __init__(self):
        self.sides = []

    def inputSides(self):
        pass  # subclass

    def area(self):
        pass  # subclass

class Circle(Shape):
    def inputSides(self):
        radius = float(radius_entry.get())
        self.sides.append(radius)

    def area(self):
        radius = self.sides[0]
        return pi * radius**2

class Rectangle(Shape):
    def inputSides(self):
        length = float(length_entry.get())
        width = float(width_entry.get())
        self.sides.extend([length, width])

    def area(self):
        length, width = self.sides
        return length * width  # formula for calculating

class Triangle(Shape):
    def inputSides(self):
        base = float(base_entry.get())
        height = float(height_entry.get())
        self.sides.extend([base, height])

    def area(self):
        base, height = self.sides
        return 0.5 * base * height

def calculate_area(shape):
    shape.inputSides()
    result_label.config(text=f"Area: {shape.area()}")

root = tk.Tk()
root.title("Shapes")

radius_label = tk.Label(root, text="Enter Radius (for Circle):")
radius_label.pack()

radius_entry = tk.Entry(root)
radius_entry.pack()

length_label = tk.Label(root, text="Enter Length (for Rectangle):")
length_label.pack()

length_entry = tk.Entry(root)
length_entry.pack()

width_label = tk.Label(root, text="Enter Width (for Rectangle):")
width_label.pack()

width_entry = tk.Entry(root)
width_entry.pack()

base_label = tk.Label(root, text="Enter Base (for Triangle):")
base_label.pack()

base_entry = tk.Entry(root)
base_entry.pack()

height_label = tk.Label(root, text="Enter Height (for Triangle):")
height_label.pack()

height_entry = tk.Entry(root)
height_entry.pack()

# buttons for every shape
circle_button = tk.Button(root, text="Calculate Circle Area",
                          command=lambda: calculate_area(Circle()))
circle_button.pack()

rectangle_button = tk.Button(root, text="Calculate Rectangle Area",
                             command=lambda: calculate_area(Rectangle()))
rectangle_button.pack()

triangle_button = tk.Button(root, text="Calculate Triangle Area",
                            command=lambda: calculate_area(Triangle()))
triangle_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

# running the program
root.mainloop()

