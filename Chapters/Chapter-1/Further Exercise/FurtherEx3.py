# 5 rows
rows = 5
for i in range(1, rows + 1):
    # printing the spaces
    for j in range(rows-i):
        print(" ", end="")
        # printing the asterisks
    for k in range(2 * i-1):
        print("*", end="")
    print()
