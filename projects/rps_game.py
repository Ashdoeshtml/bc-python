import random

# Ye available options hain jo player aur computer choose kar sakte hain.
options = ("rock", "paper", "scissors")
is_running = True

# Ye main game loop hai.
while is_running:

    player = None
    # Pehle computer ka choice generate karte hain.
    computer = random.choice(options)

    # Ye loop user se valid input leta hai.
    while player not in options:
        player = input("What are you choosing? (rock, paper, or scissors): ").lower()

    print(f"Player's Choice: {player}")
    print(f"Computer's Choice: {computer}")

    # Ye sab winning conditions check karte hain.
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
