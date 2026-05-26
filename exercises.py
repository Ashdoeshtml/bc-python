## Exercise 1: Rectangle Area Calc

program = None
length = None
width = None

while not program == "Q":

    length = float(input("Enter the length of the rectangle(cm): "))
    width = float(input("Enter the width of the rectangle(cm): "))

    area = length * width
    print(f"The area of the rectangle is: {area}cm²")

    program = input("Q to quit or any other key to run again: ")

print("Thanks for using my program!")

######################################################################################

## Exercise 2: Shopping Cart Program

program = None
item = None
price = None
quantity = None

while not program == "Q":

    item = input("What item would you like to buy?: ")
    price = float(input("What is the price?:₹ "))
    quantity = int(input(f"How many {item} would you like to buy?: "))

    total = price * quantity

    print(f"You have bought {quantity} x {item}/s")
    print(f"Your total is ₹{total}")

    program = input("Q to quit or any other key to run again: ")

print("Thanks for using my program!")

######################################################################################

## Exercise 3: Circumference Calc

import math

r = None
program = None

while not program == "Q":

    r = float(input("Enter the radius of the circle in cm:  "))

    c = 2 * math.pi * r

    print(f"The circumference of a circle with {r}cm radius is {round(c, 3)}cm")

    program = input("Q to quit or any other key to run again: ")

print("Thanks for using my program!")

######################################################################################

## Exercise 4: Circle Area Calc

import math

r = None
program = None

while not program == "Q":

    r = float(input("Enter the radius of the circle in cm:  "))

    area = math.pi * pow(r, 2)

    print(f"The area of the circle with {r}cm radius is {round(area, 3)}cm²")

    program = input("Q to quit or any other key to run again: ")

print("Thanks for using my program!")

######################################################################################

## Exercise 5: Hypotenuse of Right-Angled Triangle Calc

import math

program = None
a = None
b = None

while not program == "Q":

    a = float(input("Enter the length of side A in cm: "))
    b = float(input("Enter the length of side B in cm: "))

    c = math.sqrt(pow(a, 2) + pow(b, 2))

    print(f"The Hypotenuse: {round(c, 3)}cm")

    program = input("Q to quit or any other key to run again: ")

print("Thanks for using my program!")

######################################################################################

## Exercise 6: Validate User Input

program = None
username = None

while not program == "Q":

    username = input("Enter your username: ")

    if len(username) > 12:
        print("Username should not contain more than 12 characters")

    elif not username.find(" ") == -1:
        print("Username cannot contain spaces.")

    elif not username.isalpha():
        print("Username should not contain any numbers.")

    else:
        print(f"Welcome, {username}")

    program = input("Q to quit or any other key to run again: ")

print("Thanks for using my program!")

######################################################################################

## Exercise 7: Making Rectangle with Nested Loops

program = None
rows = None
columns = None
symbol = None

while not program == "Q":

    rows = int(input("Enter the number of rows: "))
    columns = int(input("Enter the number of columns: "))
    symbol = input("Enter a symbol to use: ")

    for x in range(rows):
        for y in range(columns):
            print(symbol, end="")
        print()

    program = input("Q to quit or any other key to run again: ")

print("Thanks for using my program!")

######################################################################################

## Exercise 8: Number-Pad

num_pad = ((1, 2, 3), (4, 5, 6), (7, 8, 9), ("*", 0, "#"))

for row in num_pad:

    for number in row:
        print(number, end="   ")

    print()

######################################################################################

## Exercise 9: Count-up Timer

import time


def count_up(end, start=0):
    for counter in range(start, end + 1):
        print(counter)
        time.sleep(1)
    print("DONE!")


count_up(20)

######################################################################################

# Exercise 10: Smart Blender


def make_smoothie(size, *ingredients, **customizations):
    print(f"Making a {size} smoothie with: {ingredients}")

    if customizations:
        print("Customizations:")

        for key, value in customizations.items():
            print(f"- {key}: {value}")


def delivery(address, *ingredients, **customizations):
    print(f"Delivering to: {address}.")
    make_smoothie(*ingredients, **customizations)


delivery(
    "123 Python Way",
    "Medium",
    "Mango",
    "Pineapple",
    liquid="Coconut Water",
    sugar_level="None",
    protein=True,
)

######################################################################################
