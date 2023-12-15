# importing tkinter
import tkinter as tk
# define the function
def shapes():
    canvas.delete("all")
    shape = shape_var.get()
# nested if statements
    if shape== "Oval":
        canvas.create_oval(50, 50, 150, 100, outline="black", width=2)
    elif shape == "Rectangle":
        canvas.create_rectangle(50, 50, 150, 100, outline="black", width=2)
    elif shape == "Square":
        canvas.create_rectangle(50, 50, 100, 100, outline="black", width=2)
    elif shape == "Triangle":
        canvas.create_polygon(50, 100, 100, 50, 150, 100, outline="black", width=2)
def coordinates():
    canvas.delete("all")
    shape = shape_var.get()
    coordinates = coordinates_entry.get().split(',')
# nested if statements
    if shape == "Oval":
        canvas.create_oval(*coordinates, outline="black", width=2)
    elif shape == "Rectangle" or shape == "Square":
        canvas.create_rectangle(*coordinates, outline="black", width=2)
    elif shape == "Triangle":
        canvas.create_polygon(*coordinates, outline="black", width=2)

# main window
root = tk.Tk()
root.title("Making shapes wit the help of coordinates")  # title

shape_var = tk.StringVar(root)
shape_var.set("Select a shape")  # selecting a shape from the options

shape_label = tk.Label(root, text="Select a shape:", bg='orange')
shape_label.pack()

option = tk.OptionMenu(root, shape_var, "Oval", "Rectangle", "Square", "Triangle")
option.pack()

button = tk.Button(root, text="Draw Shape", command=shapes)
button.pack()

coordinates_label = tk.Label(root, text="Enter coordinates (Each comma seperated):")
coordinates_label.pack()

coordinates_entry = tk.Entry(root)
coordinates_entry.pack()

draw_coordinates_button = tk.Button(root, text="Draw with Coordinates", command=coordinates, bg='yellow')
draw_coordinates_button.pack()

canvas = tk.Canvas(root, width=100, height=100)
canvas.pack()

# running the main loop
root.mainloop()
