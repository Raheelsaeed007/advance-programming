# Open the file in read mode
# file name with the name of numbers.txt and open it in the read mode
with open('numbers.txt', 'r') as file:
    # Read all lines from the file and convert each line to an integer
    numbers = [int(line.strip()) for line in file]

# Get the output in integer format
for number in numbers:
    print(number) # printing the numbers