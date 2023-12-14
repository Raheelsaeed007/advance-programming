import tkinter as tk
# defining the function
def temperature():
    try:
        temperature = float(entry.get())
        converted_temperature = 0

        if temp_var.get() == "Celsius to Fahrenheit":
            converted_temperature = (temperature * 9/5) + 32
        elif temp_var.get() == "Fahrenheit to Celsius":
            converted_temperature = (temperature - 32) * 5/9

        result_label.config(text=f"Result: {converted_temperature:.2f}")
    except ValueError:
        result_label.config(text="Please enter a valid number")

root = tk.Tk()
root.title("Temperature Converter")

frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

entry = tk.Entry(frame)
entry.grid(row=0, column=0, padx=5, pady=5)

temp_var = tk.StringVar(root)
options = ["Celsius to Fahrenheit", "Fahrenheit to Celsius"]
operation_menu = tk.OptionMenu(frame, temp_var, *options)
operation_menu.grid(row=0, column=1, padx=5, pady=5)
temp_var.set(options[0])

convert_button = tk.Button(frame, text="Convert", command=temperature)
convert_button.grid(row=1, columnspan=2, padx=5, pady=10)

result_label = tk.Label(frame, text="Result: ")
result_label.grid(row=2, columnspan=2)

root.mainloop()
