import random

# Set the range in which the number should be.
lowest = 1
highest = 100

# Generate a random number.
answer = random.randint(lowest, highest)
guesses = 0
is_running = True

# This is the main game loop.
while is_running:
    guess = input("Enter your guess: ")

    # First, check if the input is a digit or not.
    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < lowest or guess > highest:
            print("This number is out of bounds.")

        elif guess == answer:
            print(f"Congrats! {answer} was the correct answer!")
            print(f"It took you {guesses} to guess {answer}.")
            is_running = input("Do you want to play again?(Y or N): ").upper()

            if is_running == "Y":
                is_running = True
                answer = random.randint(lowest, highest)

            elif is_running == "N":
                is_running = False
                print("Thanks for using my program!")

            else:
                print("Invalid input entered.")

        elif guess > answer:
            print("Too high!")

        elif guess < answer:
            print("Too low!")

        else:
            print("Guess something else!")

    else:
        print("Please enter a number.")
