def calculator_menu():
    while True:
        print("Calculator Menu:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Modulus")

        choice = int(input("Enter operation choice: "))

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        result = 0

        def add(x, y):
            return x + y

        def subtract(x, y):
            return x - y

        def multiply(x, y):
            return x * y

        def divide(x, y):
            if y == 0:
                return "Cannot divide by zero!"
            else:
                return x / y

        def modulus(x, y):
            if y == 0:
                return "Cannot find modulus by zero!"
            else:
                return x % y

        if choice == 1:
            result = add(num1, num2)
        elif choice == 2:
            result = subtract(num1, num2)
        elif choice == 3:
            result = multiply(num1, num2)
        elif choice == 4:
            result = divide(num1, num2)
        elif choice == 5:
            result = modulus(num1, num2)
        else:
            print("Invalid choice!")

        print("Result:", result)

        repeat = input("Do you want to perform another calculation? (yes/no): ")
        if repeat.lower() != "yes":
            break

calculator_menu()
