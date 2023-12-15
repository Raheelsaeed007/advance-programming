# *********************************************VENDING MACHINE***********************************************************
# ***********************************************************************************************************************
import time

print("\033[1;33;40m WELCOME TO THE VENDING MACHINE")  # adding yellow color
# input
number_of_dirhams = int(input("How many  dirhams would you like to insert? "))

# money inserted
change = round(number_of_dirhams)

print("\nYou have entered dirhams", change)
time.sleep(2)
# items with prices.

item_1 = "Coffee"
price_1 = 4
item_2 = "biscuits"
price_2 = 3.50
item_3 = "mango juice"
price_3 = 3
item_4 = "cup cake"
price_4 = 2.50
item_5 = "chips"
price_5 = 1.75
item_6 = "chocolate"
price_6 = 2.15

# item purchased
coffee_purchased = 0
biscuits_purchased = 0
mango_juice_purchased = 0
cup_cake_purchased = 0
chips_purchased = 0
chocolate_purchased = 0

print("There are 6 items available to pick from;\n")
time.sleep(2)
print(" Item                   Prices")
print(" ----                   -----")
print(" {}         ----->  {} ".format(item_1, price_1))
print(" {}  ----->  {} ".format(item_2, price_2))
print(" {}     ----->  {} ".format(item_3, price_3))
print(" {}       ----->  {} ".format(item_4, price_4))
print(" {}    ----->  {} ".format(item_5, price_5))
print(" {}          ----->  {} ".format(item_6, price_6))
print("")

while change > 0:
    customers_selection = input("What would you like to buy? Type N when you are finished \n")
    if customers_selection == "Coffee" or customers_selection == "coffee" and change >= price_1:
        print("You have selected a", item_1, "these cost", price_1, "each,")
        change = round((change - price_1), 2)
        coffee_purchased = (coffee_purchased + 1)

        print("Your balance remaining : dirhams", change)


    elif customers_selection == "biscuits" or customers_selection == "biscuits" and change >= price_2:
        print("You have selected a", item_2, "these cost", price_2, "each,")
        change = round((change - price_2), 2)
        biscuits_purchased = (biscuits_purchased + 1)

        print("Your balance remaining : dirhams", change)


    elif customers_selection == "mango juice" or customers_selection == "mango juice" and change >= price_3:
        print("You have selected a", item_3, "these cost", price_3, "each,")
        change = round((change - price_3), 2)
        mango_juice_purchased = (mango_juice_purchased + 1)

        print("Your balance remaining : dirhams", change)


    elif customers_selection == "cup cake" or customers_selection == "cup cake" and change >= price_4:
        print("You have selected a", item_4, "these cost", price_4, "each,")
        change = round((change - price_4), 2)
        cup_cake_purchased = (cup_cake_purchased + 1)

        print("Your balance remaining ", change)


    elif customers_selection == "Chips" or customers_selection == "chips" and change >= price_5:
        print("You have selected a", item_5, "these cost", price_5, "each,")
        change = round((change - price_5), 2)
        chips_purchased = (chips_purchased + 1)

        print("Your balance remaining ", change)


    elif customers_selection == "chocolate" or customers_selection == "chocolate" and change >= price_6:
        print("You have selected a", item_6, "these cost", price_6, "each,")
        change = round((change - price_6), 2)
        chocolate_purchased = (chocolate_purchased + 1)

        print("Your balance remaining ", change)


    elif customers_selection == "N" or customers_selection == "n":

        break

    elif change <= 0:
        print("You have insufficient balance.")

        break
    else:
        print("There has been an error or you may not have enough credit.")

print("\nYou have dirhams", change, "remaining.")
time.sleep(2)
# receipt
print("\nHere is your receipt;")
time.sleep(2)
if coffee_purchased > 0:
    print("You purchased", coffee_purchased, item_1, "at dirhams", (price_1 * coffee_purchased))
if biscuits_purchased > 0:
    print("You purchased", biscuits_purchased, item_2, "at dirhams", (price_2 * biscuits_purchased))
if mango_juice_purchased > 0:
    print("You purchased", mango_juice_purchased, item_3, "at dirhams", (price_3 * mango_juice_purchased))
if cup_cake_purchased > 0:
    print("You purchased", cup_cake_purchased, item_4, "at dirhams", (price_4 * cup_cake_purchased))
if chips_purchased > 0:
    print("You purchased", chips_purchased, item_5, "at dirhams", (price_5 * chips_purchased))
if chocolate_purchased > 0:
    print("You purchased", chocolate_purchased, item_6, "at dirhams", (price_6 * chocolate_purchased))
print("\033[1;33;40m")  # adding yellow color
print("\033[1;33;40m THANKS FOR USING THE VENDING MACHINE")