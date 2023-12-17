# importing operator
import operator

# defining function to perform addition
def add(x, y):
    return operator.add(x, y)

# defining function to perform subtraction
def subtract(x, y):
    return operator.sub(x, y)

# defining function to perform multiplication
def multiply(x, y):
    return operator.mul(x, y)

# defining function to perform division
def divide(x, y):
    return operator.truediv(x, y)

# defining function to perform modulos calculation
def modulus(x, y):
    return operator.mod(x, y)

# defining function to check greater number
def check_greater(x, y):
    return operator.gt(x, y)

# The menu which will bw displayed to the user to choose from
def menu():
    print("Calculator Menu:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Modulus")
    print("6. Check greater number")
    print("Q. Quit")

# nested if statements to check whether the input is valid or not
def calculate(choice):
    if choice == '1':
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))
        print("Result:", add(x, y))
    elif choice == '2':
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))
        print("Result:", subtract(x, y))
    elif choice == '3':
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))
        print("Result:", multiply(x, y))
    elif choice == '4':
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))
        if y != 0:
            print("Result:", divide(x, y))
        else:
            print("Error! Division by zero.")
    elif choice == '5':
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))
        print("Result:", modulus(x, y))
    elif choice == '6':
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))
        print("Greater number:", check_greater(x, y))
    elif choice.upper() == 'Q':
        print("Exiting the calculator.")
    else:
        print("Invalid input.")

def main():
    while True:
        menu()
        user_choice = input("Enter your choice: ")
        if user_choice.upper() == 'Q':
            break
        else:
            calculate(user_choice)

if __name__ == "__main__":
    main()

