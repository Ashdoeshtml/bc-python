# First, get age as input.
age = int(input("Enter your age: "))

# Decide the league based on age.
if age < 10:
    print("You should join the Junior League.")

elif age >= 10 and age <= 15:

    # Get goals input for this age group.
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
