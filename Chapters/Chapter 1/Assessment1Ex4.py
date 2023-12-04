# Asking user to input 3 numbers
num1 = int(input("Enter your first number:"))
num2 = int(input("Enter your Second number:"))
num3 = int(input("Enter your third number:"))
# Multiple if else statements
if num1>= num2 and num1>=num3:
    largest = num1
elif num2>= num1 and num2>=num3:
    largest = num2
else:
    largest = num3
# Printing the output
print("The largest number is:",largest)