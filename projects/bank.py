# Ye function user ka balance display karta hai.
def show_balance(balance):
    print(f"Your balance is {balance:.2f}")


# Ye function deposit ke liye user input leta hai.
def deposit():
    amount = float(input("Enter amount to be deposited: "))

    # Pehle check karte hain ki amount negative to nahi hai.
    if amount < 0:
        print("Enter a valid amount.")
        return 0
    else:
        return amount


# Ye function withdrawal ke liye user input leta hai.
def withdraw(balance):
    amount = float(input("Enter amount to be withdrawn: "))

    # Idhar check karte hain ki amount valid hai ya nahi.
    if amount < 0:
        print("Enter a valid amount.")
        return 0
    elif amount > balance:
        print("You don't have enough money.")
    else:
        return amount


# Ye main function hai jo pura program ko control karta hai.
def main():

    balance = 0
    is_running = True

    print("***********************")
    print("Welcome to ASHWIN BANK!")
    print("***********************")

    # Ye main loop hai jo program ko chal raha rehta hai.
    while is_running:

        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("What do you want to do? (1-4): ")

        # Ye menu options ko handle karte hain.
        if choice == "1":
            show_balance(balance)
        elif choice == "2":
            balance += deposit()
        elif choice == "3":
            balance -= withdraw(balance)
        elif choice == "4":
            is_running = False

    print("Thanks for using my program!")


if __name__ == "__main__":
    main()
