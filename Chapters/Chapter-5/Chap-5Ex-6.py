# importing tkinter and messagebox
import tkinter as tk
from tkinter import messagebox
# creating a main class for the operations
class Arithmetic:
    def __init__(self, root):
        self.root = root
        self.root.title("Arithmetic Operations")

        self.result = tk.StringVar()
        self.result.set("Result: ")

        self.widgets()

   # getting the input from the user
    def calculate(self):
        operation = self.operation.get()
        try:
            num1 = float(self.num1.get())
            num2 = float(self.num2.get())

            # nested if statements
            if operation == "Addition":  # if statement
                self.result.set("Result: " + str(num1 + num2))
            elif operation == "Subtraction":
                self.result.set("Result: " + str(num1 - num2))
            elif operation == "Multiplication":
                self.result.set("Result: " + str(num1 * num2))
            elif operation == "Division":
                if num2 != 0:
                    self.result.set("Result: " + str(num1 / num2))
                else:
                    self.result.set("Result: Undefined")
                    messagebox.showerror("Error", "Cannot divide by zero!")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers.")

    def widgets(self):
        tk.Label(self.root, text="Arithmetic Operations", font=("Arial", 18)).pack()

        self.num1 = tk.Entry(self.root)
        self.num1.pack()  # using pack

        self.num2 = tk.Entry(self.root)
        self.num2.pack() # using pack

        operations = ["Addition", "Subtraction", "Multiplication", "Division"] # the operations available
        self.operation = tk.StringVar()
        self.operation.set(operations[0])

        operation_menu = tk.OptionMenu(self.root, self.operation, *operations)
        operation_menu.pack()

        # creating a button for calculating
        tk.Button(self.root, text="Calculate", bg='lightcyan', command=self.calculate).pack()

        # creating a label for the text size and font style
        tk.Label(self.root, textvariable=self.result, font=("Arial", 14)).pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = Arithmetic(root)
    root.mainloop()
