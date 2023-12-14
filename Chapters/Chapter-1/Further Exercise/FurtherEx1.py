# Asking user to enter the number of days
days = int(input("Enter the number of days:"))
# converting days into hours and hours into minutes and seconds
seconds = days * 24 * 60 * 60

print(f"There are {seconds} seconds in {days} days")