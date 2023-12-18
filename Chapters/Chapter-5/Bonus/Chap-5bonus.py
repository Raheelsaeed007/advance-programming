# importing tkinter as tk
import tkinter as tk

# defining the function Animal as required
class Animal:
    def __init__(self, Type, Name, Colour, Age, Weight, Noise):
        self.Type = Type
        self.Name = Name
        self.Colour = Colour
        self.Age = Age
        self.Weight = Weight
        self.Noise = Noise

    def sayHello(self):  # function for saying hello and the name
        print(f"Hello, I am {self.Name}!")

    def makeNoise(self):  # function for making noise
        print(f"{self.Name} says: {self.Noise}")

    def animalDetails(self): # function for animal details
        details = (f"Type: {self.Type}, Name: {self.Name}, Colour: {self.Colour}, Age: {self.Age}, Weight: {self.Weight}, "
                   f"Noise: {self.Noise}")
        print(details)


# Creating GUI(graphical user interface)
def create_animal():
    animal_type = animal_type_entry.get()
    name = name_entry.get()
    color = color_entry.get()
    age = age_entry.get()
    weight = weight_entry.get()
    noise = noise_entry.get()

    animal = Animal(animal_type, name, color, age, weight, noise)
    animal.sayHello()
    animal.makeNoise()
    animal.animalDetails()


root = tk.Tk()
root.title("Playing around in class")

# Labels
tk.Label(root, text="Animal Type:").grid(row=0, column=0)
tk.Label(root, text="Name:").grid(row=1, column=0)
tk.Label(root, text="Color:").grid(row=2, column=0)
tk.Label(root, text="Age:").grid(row=3, column=0)
tk.Label(root, text="Weight:").grid(row=4, column=0)
tk.Label(root, text="Noise:").grid(row=5, column=0)

# Entries
animal_type_entry = tk.Entry(root)
name_entry = tk.Entry(root)
color_entry = tk.Entry(root)
age_entry = tk.Entry(root)
weight_entry = tk.Entry(root)
noise_entry = tk.Entry(root)

# creating grid for the entries
animal_type_entry.grid(row=0, column=1)
name_entry.grid(row=1, column=1)
color_entry.grid(row=2, column=1)
age_entry.grid(row=3, column=1)
weight_entry.grid(row=4, column=1)
noise_entry.grid(row=5, column=1)

# Button for creating animal
tk.Button(root, text="Create Animal", command=create_animal,bg='lightblue').grid(row=6, columnspan=2)

root.mainloop()
