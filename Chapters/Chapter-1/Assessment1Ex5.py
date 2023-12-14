count = 0
# while statement
while True:
    user_input = input("Do you want to continue? (Y/N):") # user input
    if user_input.upper() == 'Y':
        count += 1
    else:
        break

# printing the statement
    print(f"The loop was executed {count} times.")