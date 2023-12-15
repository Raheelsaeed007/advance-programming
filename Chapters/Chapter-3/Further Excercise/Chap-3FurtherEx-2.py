# importing tkinter and random
import tkinter as tk
import random

# List of words for the game
words = ["Python", "Computer", "Program", "Variable", "Interface"]


# Function to shuffle a word
def shuffle_word(word):
    return ''.join(random.sample(word, len(word)))


# Function to start the game
def start_game():
    global score, time_left, current_word

    # Reset variables for a new game
    score = 0
    time_left = 60
    current_word = ""
    update_score()
    next_word()


# Function to update the score label
def update_score():
    score_label.config(text=f"Score: {score}")


# Function to display the next word
def next_word():
    global current_word, time_left
    if time_left > 0:
        current_word = random.choice(words)
        shuffled_word = shuffle_word(current_word)
        word_label.config(text=shuffled_word)
        input_entry.delete(0, tk.END)
        input_entry.focus()
        countdown()
    else:
        word_label.config(text="Time's up! Game Over.")


# Function to check the guess
def check_guess():
    global score
    guess = input_entry.get().lower()
    if guess == current_word:
        score += 1
        update_score()
    next_word()


# Function to handle the countdown timer
def countdown():
    global time_left
    if time_left > 0:
        time_left -= 1
        time_label.config(text=f"Time left: {time_left} sec")
        word_label.after(1000, countdown)
    else:
        time_label.config(text="Time's up!")


# Create Tkinter window
root = tk.Tk()
root.title("Word Guessing Game")

# Score label
score = 0
score_label = tk.Label(root, text="Score: 0")
score_label.pack()

# Timer label
time_left = 60
time_label = tk.Label(root, text="Time left: 60 sec")
time_label.pack()

# Word label
current_word = ""
word_label = tk.Label(root, text="")
word_label.pack()

# Entry for user input
input_entry = tk.Entry(root)
input_entry.pack()

# Button to check the guess
check_button = tk.Button(root, text="Check", command=check_guess)
check_button.pack()

# Start button
start_button = tk.Button(root, text="Start Game", command=start_game, bg='blue')
start_button.pack()

# Run Tkinter main loop
root.mainloop()

