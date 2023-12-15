# import tkinter
import tkinter as tk


def calculate():
    file_path = 'petrolPrice.txt'
    total_cost = 0
    total_liters = 0
    count_under_3_5 = 0

    with open(file_path, 'r') as file:
        next(file)  # Skip the header
        for line in file:
            liters, cost = map(float, line.split('\t'))
            total_cost += cost
            total_liters += liters
            if cost / liters < 3.5:
                count_under_3_5 += liters

    # Calculation 1: Cost of petrol per liter bought
    cost_per_liter = total_cost / total_liters if total_liters != 0 else 0

    # Calculation 2: Overall average price per liter of petrol bought
    overall_average = total_cost / total_liters if total_liters != 0 else 0

    # Calculation 3: Petrol bought at under 3.5 AED per liter
    liters_under_3_5 = count_under_3_5

    # Displaying the results in a simple GUI
    result_text = f"Cost per liter bought: {cost_per_liter:.2f} AED\n"
    result_text += f"Overall average price per liter: {overall_average:.2f} AED\n"
    result_text += f"Liters bought at under 3.5 AED per liter: {liters_under_3_5:.2f} liters"

    result_label.config(text=result_text)


# Creating the GUI
root = tk.Tk()
root.title("Petrol Price Calculator")

calculate_button = tk.Button(root, text="Calculate", command=calculate, bg='green')
calculate_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
