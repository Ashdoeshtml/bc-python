# First, we initialize lists.
items = []
prices = []
total = 0

# This loop adds shopping items to the cart.
while True:
    item = input("What do you want to buy? (q to quit): ")

    if item.lower() == "q":
        print("Thanks for using my program!")
        break

    else:
        price = float(input(f"What is the price of {item}?: ₹"))

        items.append(item)
        prices.append(price)

# Here, we display the cart.
print("----- YOUR CART -----")
print()

for item in items:
    print(f"{item.upper(): ^20}", end=" ")

# Calculate the total.
for price in prices:
    total += price

print()

print(f"Your total is: ₹{total}")

print()
print("---------------------")
