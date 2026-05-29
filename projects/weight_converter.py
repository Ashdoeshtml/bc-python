# First, I ask for user input.
unit = str(input("Enter an unit (kgs or lbs): "))
weight = float(input("Enter the weight: "))

# Calculate the value here (based on the unit).
if unit == "kg":
    result = weight * 2.205
    print(f"Your result after converting {weight}kgs to Pounds is {result}lb.")

elif unit == "lb":
    result = weight / 2.205
    print(f"Your result after converting {weight}lbs to Pounds is {result}kgs.")

# This is for when an invalid unit is entered.
else:
    print("Invalid unit used")
    result = None

print(f"Your result after converting is {round(result, 2)}")
