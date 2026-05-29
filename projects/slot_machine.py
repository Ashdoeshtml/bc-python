import random


# All symbols are spun here.
def spin_row():

    symbols = ["💀", "🎟️", "🔔", "⭐", "🎁", "👑"]

    return [random.choice(symbols) for _ in range(3)]


# Symbols are joined here.
def print_row(row):

    print("***************************")
    print(" | ".join(row))
    print("***************************")


# Money is given based on symbols here.
def get_payout(row, bet):

    if row[0] == row[1] == row[2]:

        if row[1] == "💀":
            print("You packed: THE JACKPOT OF DEATH")
            return -(bet * 2)

        elif row[1] == "🎟️":
            print("You packed: THE COUPON")
            return bet + 50

        elif row[1] == "🔔":
            print("You packed: THE FORTUNE BELL")
            return bet * 3

        elif row[1] == "⭐":
            print("You packed: THE STAR OF DESTINY")
            return bet * 5

        elif row[1] == "🎁":
            print("You packed: THE CRATE OF TREASURE")
            return bet * 10

        elif row[1] == "👑":
            print("YOU JUST HIT THE JACKPOOOOOT!!!")
            return bet * 50

    return 0


# This is the main function where calculations and bet placement happen.
def main():

    balance = 1000

    print("***************************")
    print("Welcome to the SLOT MACHINE")
    print("***************************")

    while balance > 0:

        print(f"Your balance is ₹{balance}")

        bet = input("Place your bet amount: ₹")

        if not bet.isdigit():
            print("Please enter a valid number.")
            continue

        bet = int(bet)

        if bet <= 0:
            print("Please enter a number greater than 0.")
            continue

        if bet > balance:
            print("You don't have enough balance!")
            continue

        balance -= bet

        row = spin_row()

        print("Spinning...\n")

        print_row(row)

        payout = get_payout(row, bet)

        if payout < 0:
            print(f"You just lost ₹{-payout}")

        elif payout == 0:
            print("You won nothing...")

        else:
            print(f"You just earned ₹{payout}")

        balance += payout

        play_again = input("Do you want to play agian? (Y/N)").upper()

        if play_again != "Y":
            break

    print("Game Over!")
    print(f"Your remaining balance was ₹{balance}")


if __name__ == "__main__":
    main()
