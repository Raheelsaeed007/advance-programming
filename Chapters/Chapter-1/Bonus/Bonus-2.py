# list for locations
list =['dubai','paris', 'switzerland', 'London', 'amsterdam', 'New York']
# Printing the locations and it' length
print("list:", list)
print("Length of list:",len(list))

# Use sorted() to print the list in alphabetical order without modifying the actual list
print("Sorted list (alphabetical order):", sorted(list))


print("Original list:", list)

# Use sorted() to print the list in reverse alphabetical order without modifying the actual list
print("Sorted list (reverse alphabetical order):", sorted(list, reverse=True))

print("Original list:", list)

# Use reverse() to change the order of the list
list.reverse()
print("Reversed list:", list)

list.sort()
print("Sorted list (alphabetical order):", list)

# Use sort() to change the list so it’s stored in reverse alphabetical order
list.sort(reverse=True)
print("Sorted list (reverse alphabetical order):", list)

