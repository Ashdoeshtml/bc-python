# This function displays the user's account balance.
def show_balance(balance):
    print(f"Your balance is {balance:.2f}")


# This function takes user input for a deposit.
def deposit():
    amount = float(input("Enter amount to be deposited: "))

    # First, check if the amount is not negative.
    if amount < 0:
        print("Enter a valid amount.")
        return 0
    else:
        return amount


# This function takes user input for a withdrawal.
def withdraw(balance):
    amount = float(input("Enter amount to be withdrawn: "))

    # Here, we check if the amount is valid or not.
    if amount < 0:
        print("Enter a valid amount.")
        return 0
    elif amount > balance:
        print("You don't have enough money.")
    else:
        return amount


# This is the main function that controls the entire program.
def main():

    balance = 0
    is_running = True

    print("***********************")
    print("Welcome to ASHWIN BANK!")
    print("***********************")

    # This is the main loop that keeps the program running.
    while is_running:

        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("What do you want to do? (1-4): ")

        # This handles the menu options.
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
