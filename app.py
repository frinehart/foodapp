# Name: Francis Rinehart
# Purpose: Food App
# Language: Python
# Last Update: 11/23/2022 at 10:00 AM

# import files from classes
from burger import burger
from pizza import pizza
from sandwich import sandwich

# Welcome menu
print("Hello welcome to our app\n")
print("Which type of fast food would you like to select? ")
print("(1). Burger\n(2). Pizza\n(3). Sandwich\n(4). Exit menu")

# menu option and user selection
menu1 = 1
menu2 = 2
menu3 = 3
menu_exit = 4

myBurger = burger()
myPizza = pizza()
mySandwich = sandwich()

menu = int(input("Please select menu of your choice: "))

# menu 1 option
if menu == 1:
    print("You have selected burger menu")
    print("Which type of burger or drink do you want? ")
    print("Select the following numbers\n\n1. Burger\n2. Soda\n3. Coffee")
    user = int(input("Select one of these choice: "))
    if user == 1:
        myBurger.make_burger()
    elif user == 2:
        myBurger.add_soda()
    elif user == 3:
        myBurger.add_coffee()
    else:
        print("You did not pick a number, enjoy your day")

# menu 2 option
if menu == 2:
    print("You have selected pizza menu")
    print("Which type of burger or drink do you want? ")
    print("Select the following numbers\n\n1. Pizza\n2. Soda\n3. Bread sticks")
    user = int(input("Select one of these choice: "))
    if user == 1:
        myPizza.make_pizza()
    elif user == 2:
        myPizza.add_soda()
    elif user == 3:
        myPizza.make_bread()
    else:
        print("You did not pick a number, enjoy your day")

# menu 3 option
if menu == 3:
    print("You have selected sandwich menu")
    print("Which type of burger or drink do you want? ")
    print("Select the following numbers\n\n1. Chicken Sandwich\n2. Soda\n3. Turkey Sandwich")
    user = int(input("Select one of these choice: "))
    if user == 1:
        mySandwich.make_chicken_sandwich()
    elif user == 2:
        myBurger.add_soda()
    elif user == 3:
        mySandwich.make_turkey_sandwich()
    elif user == 4:
        mySandwich.add_coffee()
    else:
        print("You did not pick a number, enjoy your day")

# exit menu
if menu == 4:
    print("You are exiting the app, goodbye ")
else:
    print("Enjoy your day, goodbye ")

# exit function
exit()
