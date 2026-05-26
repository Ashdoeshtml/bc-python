# Pehle hum lists initialize karte hain.
items = []
prices = []
total = 0

# Ye loop shopping items add karta hai.
while True:
    item = input("What do you want to buy? (q to quit): ")

    if item.lower() == "q":
        print("Thanks for using my program!")
        break

    else:
        price = float(input(f"What is the price of {item}?: ₹"))

        items.append(item)
        prices.append(price)

# Idhar cart ko display karte hain.
print("----- YOUR CART -----")
print()

for item in items:
    print(f"{item.upper(): ^20}", end=" ")

# Ye total ko calculate karte hain.
for price in prices:
    total += price

print()

print(f"Your total is: ₹{total}")

print()
print("---------------------")
