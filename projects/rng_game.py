import random

# Ye range set karte hain jo number mein hona chahiye.
lowest = 1
highest = 100

# Ek random number generate karte hain.
answer = random.randint(lowest, highest)
guesses = 0
is_running = True

# Ye main game loop hai.
while is_running:
    guess = input("Enter your guess: ")

    # Pehle check karte hain ki input digit hai ya nahi.
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
