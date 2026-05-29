# First, get user input.
unit = input("Enter an unit (C/F): ")
temp = float(input("Enter the temperature: "))

# Calculate based on the unit.
if unit == "C":
    result = (temp * 9 / 5) + 32
    print(f"The temperature in Fahrenheit is: {round(result, 2)}°F")

elif unit == "F":
    result = (temp - 32) * 5 / 9
    print(f"The temperature in Celsius is: {round(result, 2)}°C")

# If an invalid unit is entered, show this message.
else:
    print("Invalid unit entered.")
