# creating an integer list with 10 values
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("List using a for loop:")
for number in list:
    print(number,end="")
# printing the max and min values
print("\nHighest value:",max(list))
print("Lowest value:",min(list))

# Sorting the values
list.sort()
print("Sorted in ascending order:", list)

# descending order
list.sort(reverse=True)
print("Sorted in descending order:", list)

# Appending the list
list.append(11)
list.append(12)

print("List after appending:", list)