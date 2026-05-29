# This menu dictionary stores items and their prices.
menu = {
    "roll": 120,
    "burger": 90,
    "dosa": 80,
    "rice": 110,
    "fries": 70,
    "coffee": 60,
    "lassi": 50,
}

# First, we initialize the cart and total.
cart = []
total = 0

print("---------- MENU ----------")
for key, value in menu.items():
    print(f"{key:20}: ₹{value}")
print("--------------------------")

# Here, we take the user's order.
while True:
    food = input("What do you want to order? (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

# Display the cart and total.
print("------- YOUR ORDER -------")
for food in cart:
    total += menu.get(food)
    print()
    print(food, end=" ")

print()
print(f"You have to pay: ₹{total}")
print()
print("--------------------------")
