# Pehle hum age input leta hun.
age = int(input("Enter your age: "))

# Age ke hisaab se league decide karte hain.
if age < 10:
    print("You should join the Junior League.")

elif age >= 10 and age <= 15:

    # Ye group mein goals ke liye input leta hai.
    Goals = int(input("How many goals did you score last season?: "))

    if Goals < 0:
        print("Goals cannot be negative.")
    elif Goals >= 5:
        print("You're in the A-Team!")
    else:
        print("Keep Trying!")
        print("You're in the B-Team.")

elif age >= 16:
    print("You should join the Senior League.")

else:
    print("Please enter an appropriate age.")
