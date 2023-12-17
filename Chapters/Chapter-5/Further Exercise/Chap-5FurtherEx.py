# import tkinter
import tkinter as tk
from tkinter import messagebox
from fractions import Fraction  # importing fractions

class Operations:
    def __init__(self, root):
        self.root = root
        self.root.title("Arithmetic Operations")
        self.result = tk.StringVar()
        self.result.set("Result: ")

        self.widgets()

    def calculate(self):
        operation_type = self.operation_type.get()
        operation = self.operation.get()
        try:
            if operation_type == "Arithmetic":
                num1 = float(self.num1.get())
                num2 = float(self.num2.get())

                if operation == "Addition":
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
            elif operation_type == "Rational":
                frac1 = Fraction(self.num1.get())
                frac2 = Fraction(self.num2.get())

                if operation == "Addition":
                    self.result.set("Result: " + str(frac1 + frac2))
                elif operation == "Subtraction":
                    self.result.set("Result: " + str(frac1 - frac2))
                elif operation == "Multiplication":
                    self.result.set("Result: " + str(frac1 * frac2))
                elif operation == "Division":
                    if frac2 != 0:
                        self.result.set("Result: " + str(frac1 / frac2))
                    else:
                        self.result.set("Result: Undefined")
                        messagebox.showerror("Error", "Cannot divide by zero!")

        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers.")
        except ZeroDivisionError:
            messagebox.showerror("Error", "Cannot divide by zero in rational operations.")

# creating widgets for the user input
    def widgets(self):
        tk.Label(self.root, text="Operations", font=("Arial", 18)).pack()

        self.num1 = tk.Entry(self.root)
        self.num1.pack()

        self.num2 = tk.Entry(self.root)
        self.num2.pack()

        operation_types = ["Arithmetic", "Rational"]  # types of operations
        self.operation_type = tk.StringVar()
        self.operation_type.set(operation_types[0])

        operation_type_menu = tk.OptionMenu(self.root, self.operation_type, *operation_types)
        operation_type_menu.pack()

        arithmetic_operations = ["Addition", "Subtraction", "Multiplication", "Division"] # options for arithmetic
        rational_operations = ["Addition", "Subtraction", "Multiplication", "Division"]  # options for rational

        self.operation = tk.StringVar()
        self.operation.set(arithmetic_operations[0])

        operation_menu = tk.OptionMenu(self.root, self.operation, *arithmetic_operations)
        operation_menu.pack()

        # button for calculating
        tk.Button(self.root, text="Calculate", command=self.calculate).pack()

        # label for the result
        tk.Label(self.root, textvariable=self.result, font=("Arial", 14)).pack()

# printing the output
if __name__ == "__main__":
    root = tk.Tk()  # main window
    app = Operations(root)
    root.mainloop()  # running the main loop

