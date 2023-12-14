# asking for input from user
num=input("Enter a number: ")

sum = 0

for digit in num:
    sum += int(digit)

# printing the statement
print(f"The sum of digits in the number {num} is: {sum}")