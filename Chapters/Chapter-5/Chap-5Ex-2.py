# importing tkinter
import tkinter as tk

# creating main class called students
class Students:
    def __init__(self, name, mark1, mark2, mark3):
        self.name = name
        self.mark1 = mark1
        self.mark2 = mark2
        self.mark3 = mark3
# calculated grade to calculate the average combining marks
    def calcGrade(self):
        average = (self.mark1 + self.mark2 + self.mark3) / 3
        return average
# display function
    def display(self):
        grade = self.calcGrade()
        return f"Student Name: {self.name}\nAverage Grade: {grade:.2f}"

# getting the entry from the user
def student():
    name = name_entry.get()
    mark1 = int(mark1_entry.get())
    mark2 = int(mark2_entry.get())
    mark3 = int(mark3_entry.get())

    student = Students(name, mark1, mark2, mark3)
    result_label.config(text=student.display())

# tkinter
root = tk.Tk()
root.title("Students")

# creating label
name_label = tk.Label(root, text="Enter Name:")
name_label.pack()

# name and marks entry
name_entry = tk.Entry(root)
name_entry.pack() # using pack

mark1_label = tk.Label(root, text="Enter Mark 1:")
mark1_label.pack() # using pack

mark1_entry = tk.Entry(root)
mark1_entry.pack() # using pack

mark2_label = tk.Label(root, text="Enter Mark 2:")
mark2_label.pack() # using pack

mark2_entry = tk.Entry(root)
mark2_entry.pack() # using pack

mark3_label = tk.Label(root, text="Enter Mark 3:")
mark3_label.pack() # using pack

mark3_entry = tk.Entry(root)
mark3_entry.pack() # using pack

# creating button and giving command
student_button = tk.Button(root, text="Create Student", command=student)
student_button.pack() # using pack

result_label = tk.Label(root, text="")
result_label.pack() # using pack

# run the main loop
root.mainloop()
