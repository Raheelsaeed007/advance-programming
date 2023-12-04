count = 0
while True:
    user_input = input("Do you want to continue? (Y/N):")
    if user_input.upper() == 'Y':
        count += 1
    else:
        break

    print(f"The loop was executed{count} times.")