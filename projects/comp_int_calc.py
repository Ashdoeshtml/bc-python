# Pehle hum variables ko initialize karte hain.
program = 0
principle = 0
rate = 0
time = 0

# Ye main loop hai jo program ko run karta rahega.
while not program == "Q":

    # Idhar principle amount ke liye user input leta hun with validation.
    while True:
        principle = float(input("Enter the principle amount:  "))

        if principle <= 0:
            print("Principle amount must be greater than 0.")

        else:
            break

    # Ye loop rate of interest ke liye user input leta hai.
    while True:
        rate = float(input("Enter the annual rate of interest (e.g., 5 for 5%):  "))

        if rate <= 0:
            print("Rate of interest must be greater than 0.")

        else:
            break

    # Ye loop time period ke liye user input leta hai.
    while True:
        time = float(input("Enter the time period in years:  "))

        if time <= 0:
            print("Time period must be greater than 0.")

        else:
            break

    # Idhar hum compound interest ka calculation karte hain.
    total = principle * pow((1 + (rate / 100)), time)

    # Ye total balance aur interest ko print karte hain.
    print(f"Your total balance (Principle + Interest) is: ₹{round(total, 2)}")
    print(f"Total interest earned: ₹{round(total - principle, 2)}")

    program = input("Enter 'Q' to quit or any other key to run again: ").upper()

print("Thanks for using my program!")
