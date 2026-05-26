# Pehle user input liya.
unit = input("Enter an unit (C/F): ")
temp = float(input("Enter the temperature: "))

# Idhar unit ke hisab se calculations hoti hai.
if unit == "C":
    result = (temp * 9 / 5) + 32
    print(f"The temperature in Fahrenheit is: {round(result, 2)}°F")

elif unit == "F":
    result = (temp - 32) * 5 / 9
    print(f"The temperature in Celsius is: {round(result, 2)}°C")

# Agar koi aur unit dala toh idhar ye baatadega.
else:
    print("Invalid unit entered.")
