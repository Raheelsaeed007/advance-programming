
import matplotlib.pyplot as plt

# Data
categories = ['Game', 'Commercials', "Won't watch"]
male = [279, 81, 132]
female = [200, 156, 160]

# Plotting
fig, ax = plt.subplots(figsize=(8, 6))
bar1 = ax.bar(categories, male, label='Male')
bar2 = ax.bar(categories, female, bottom=male, label='Female')

# Adding labels, title, and legend
ax.set_xlabel('Categories')   # label for categories
ax.set_ylabel('Number of People')   # number of people
ax.set_title('Super Bowl Viewing Preferences by Gender')   # title naming
ax.legend()

# Show plot
plt.tight_layout()
plt.show()

