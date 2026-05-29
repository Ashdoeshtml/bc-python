# First, we initialize variables.
program = 0
principle = 0
rate = 0
time = 0

# This is the main loop that runs the program.
while not program == "Q":

    # Here, get user input for the principle amount with validation.
    while True:
        principle = float(input("Enter the principle amount:  "))

        if principle <= 0:
            print("Principle amount must be greater than 0.")

        else:
            break

    # This loop gets user input for the rate of interest.
    while True:
        rate = float(input("Enter the annual rate of interest (e.g., 5 for 5%):  "))

        if rate <= 0:
            print("Rate of interest must be greater than 0.")

        else:
            break

    # This loop gets user input for the time period.
    while True:
        time = float(input("Enter the time period in years:  "))

        if time <= 0:
            print("Time period must be greater than 0.")

        else:
            break

    # Here, we calculate the compound interest.
    total = principle * pow((1 + (rate / 100)), time)

    # Print the total balance and interest.
    print(f"Your total balance (Principle + Interest) is: ₹{round(total, 2)}")
    print(f"Total interest earned: ₹{round(total - principle, 2)}")

    program = input("Enter 'Q' to quit or any other key to run again: ").upper()

print("Thanks for using my program!")
