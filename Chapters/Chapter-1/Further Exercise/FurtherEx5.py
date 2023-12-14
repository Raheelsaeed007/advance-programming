marks = [("CodeLab I", 67), ("web Development", 75),
         ("CodeLabII", 74), ("Smartphone Apps", 68),
         ("Games Development", 70), ("Responsive web", 65)]

#  (low to high)
sorted_high = sorted(marks, key=lambda x: x[1])
print("Sorted by marks (low to high):", sorted_high)

# (high to low)
sorted_low = sorted(marks, key=lambda x: x[1], reverse=True)
print("Sorted by marks (high to low):", sorted_low)
