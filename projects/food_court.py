# Ye menu dictionary hai jo items aur unke prices rakhti hai.
menu = {
    "roll": 120,
    "burger": 90,
    "dosa": 80,
    "rice": 110,
    "fries": 70,
    "coffee": 60,
    "lassi": 50,
}

# Pehle hum cart aur total ko initialize karte hain.
cart = []
total = 0

print("---------- MENU ----------")
for key, value in menu.items():
    print(f"{key:20}: ₹{value}")
print("--------------------------")

# Idhar user order liya jata hai.
while True:
    food = input("What do you want to order? (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

# Ye cart aur total ko display karte hain.
print("------- YOUR ORDER -------")
for food in cart:
    total += menu.get(food)
    print()
    print(food, end=" ")

print()
print(f"You have to pay: ₹{total}")
print()
print("--------------------------")
