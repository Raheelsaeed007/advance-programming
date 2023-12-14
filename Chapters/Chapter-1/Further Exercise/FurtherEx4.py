# Assigning the variable to the names
names = ["Arshiya", "Usman",
         "Iftikhar", "Usman", "Rafia",
         "Mary", "Anmol", "Zainab", "Iftikhar",
         "Arshiya", "Rafia", "Jake"
        ]

names_counts = {}

# Count occurrences of each item in the list
for item in names:
    if item in names_counts:
        names_counts[item] += 1
    else:
        names_counts[item] = 1

# Display the number of times each item appears
for key, value in names_counts.items():
    print(f"{key}: {value} times")
