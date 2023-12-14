# Importing tkinter
import tkinter as tk
# defining the main function
def operations():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operation_var.get()
# nested statements
        if operation == "Addition":
            result = num1 + num2  # formula
        elif operation == "Subtraction":
            result = num1 - num2  # formula
        elif operation == "Multiplication":
            result = num1 * num2    # formula
        elif operation == "Division":
            if num2 == 0:   # formula
                result = "Cannot divide by zero"
            else:
                result = num1 / num2
        elif operation == "Modulo Division":
            if num2 == 0:
                result = "Cannot modulo divide by zero"
            else:
                result = num1 % num2
        else:
            result = "Select an operation"

        label.config(text=f"Result: {result}")
    except ValueError:
        label.config(text="Please enter valid numbers")

# main window
root = tk.Tk()
root.title("Basic Arithmetic Operations")

frame = tk.Frame(root)
frame.pack(padx=20, pady=20)
# frame for entry 1
entry1 = tk.Entry(frame)
entry1.grid(row=0, column=0, padx=5, pady=5)

operation_var = tk.StringVar(root)
operation = ["Addition", "Subtraction", "Multiplication", "Division", "Modulo Division"]
operation_menu = tk.OptionMenu(frame, operation_var, *operation)
operation_menu.grid(row=0, column=1, padx=5, pady=5)
operation_var.set("Addition")

# frame for entry 2
entry2 = tk.Entry(frame)
entry2.grid(row=0, column=2, padx=5, pady=5)

# button
calculate_button = tk.Button(frame, text="Calculate", command= operations)
calculate_button.grid(row=1, columnspan=3, padx=5, pady=10)

# adding label
label = tk.Label(frame, text="Result: ")
label.grid(row=2, columnspan=3)

# returning to the main loop
root.mainloop()

