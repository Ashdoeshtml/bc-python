import random

# ● ┌ ─ ┐ │ └ ┘

# Ye dictionary har dice number ka ASCII art rakhti hai.
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

# Ye main loop hai jo program ko chal raha rehta hai.
is_running = "y"

while is_running == "y":

    # Pehle dice list ko initialize karte hain.
    dice = []
    dice_number = int(input("How many dice?: "))
    total = 0

    # Idhar random dice values generate karte hain.
    for die in range(dice_number):
        dice.append(random.randint(1, 6))

    # Ye loop har dice ka ASCII art ko print karta hai.
    for line in range(5):
        for die in dice:
            print(dice_art.get(die)[line], end="")
        print()

    # Ye total ko calculate karte hain.
    for die in dice:
        total += die

    print(f"Total: {total}")

    if not input("Do you want to try again? (y or n): ").lower() == "y":
        is_running = False
        print("Thanks for using my program!")
