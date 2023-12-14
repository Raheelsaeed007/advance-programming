# importing tkinter
import tkinter as tk
# define the function
def count():
    user_input = entry.get()
    vowels = 0
    consonants = 0
    characters = 0

# statements
    for char in user_input:
        if char.isalpha():
            if char.lower() in 'aeiou':
                vowels += 1
            else:
                consonants += 1
        else:
            characters += 1

    result_label.config(text=f"Total number of letters: {len(user_input)}\nNumber of vowels: "
                             f"{vowels}\nNumber of consonants: {consonants}\nNumber of special characters: {characters}")

root = tk.Tk()
root.title("Counter")

entry = tk.Entry(root)
entry.pack()

count_button = tk.Button(root, text="Count", command=count, bg="skyblue")
count_button.pack()

result_label = tk.Label(root)
result_label.pack()

# Run the GUI
root.mainloop()