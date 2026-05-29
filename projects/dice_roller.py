import random

# ● ┌ ─ ┐ │ └ ┘

# This dictionary stores ASCII art for each dice number.
dice_art = {
    # fmt: off
    1: ("┌─────────┐", 
        "│         │", 
        "│    ●    │", 
        "│         │", 
        "└─────────┘"),
    
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"),
    
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"),
    
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘"),
    # fmt: on
}

# This is the main loop that keeps the program running.
is_running = "y"

while is_running == "y":

    # First, initialize the dice list.
    dice = []
    dice_number = int(input("How many dice?: "))
    total = 0

    # Here, generate random dice values.
    for die in range(dice_number):
        dice.append(random.randint(1, 6))

    # This loop prints the ASCII art for each die.
    for line in range(5):
        for die in dice:
            print(dice_art.get(die)[line], end="")
        print()

    # Calculate the total.
    for die in dice:
        total += die

    print(f"Total: {total}")

    if not input("Do you want to try again? (y or n): ").lower() == "y":
        is_running = False
        print("Thanks for using my program!")
