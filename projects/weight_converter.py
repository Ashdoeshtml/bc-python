# pehle mein user input mangvata hun.
unit = str(input("Enter an unit (kgs or lbs): "))
weight = float(input("Enter the weight: "))

# Idhar value calculate karta hun (based on unit).
if unit == "kg":
    result = weight * 2.205
    print(f"Your result after converting {weight}kgs to Pounds is {result}lb.")

elif unit == "lb":
    result = weight / 2.205
    print(f"Your result after converting {weight}lbs to Pounds is {result}kgs.")

# Ye sab jisse koi galat unit daal de to.
else:
    print("Invalid unit used")
    result = None

print(f"Your result after converting is {round(result, 2)}")
