import random

# These are the available options that the player and computer can choose.
options = ("rock", "paper", "scissors")
is_running = True

# This is the main game loop.
while is_running:

    player = None
    # First, generate the computer's choice.
    computer = random.choice(options)

    # This loop gets valid input from the user.
    while player not in options:
        player = input("What are you choosing? (rock, paper, or scissors): ").lower()

    print(f"Player's Choice: {player}")
    print(f"Computer's Choice: {computer}")

    # Check all winning conditions.
    if player == "rock" and computer == "scissors":
        print("Congrats! You win!")
    elif player == "paper" and computer == "rock":
        print("Congrats! You win!")
    elif player == "scissors" and computer == "paper":
        print("Congrats! You win!")
    elif player == computer:
        print("It's a tie!")
    else:
        print("Better luck next time!")

    if not input("Want to play again? (y or n): ").lower() == "y":
        is_running = False

print("Thanks for using my program!")
