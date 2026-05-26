# Ye tuple questions rakhti hai.
questions = (
    "1. What has to be broken before you can use it?",
    "2. Which month of the year has 28 days?",
    "3. What is full of holes but still holds water?",
    '4. What question can you never answer "yes" to?',
    "5. You will find me in Mercury, Earth, Mars and Jupiter, but not in Venus or Neptune. ",
    "6. What goes up but never comes down?",
    "7. A man dies of old age on his 25th birthday. How is this possible?",
    "8. What gets wet while drying?",
    "9. What can you break, even if you never pick it up or touch it?",
    "10. I have a tail and a head, but no body.",
)

# Ye tuple har question ke options rakhti hai.
options = (
    ("A. A promise", "B. An egg", "C. A record", "D. A glow stick"),
    ("A. Only February", "B. Every other month", "C. All of them", "D. None of them"),
    ("A. A net", "B. A sieve", "C. A sponge", "D. A colander"),
    (
        "A. Are you awake?",
        "B. Can you hear me?",
        "C. Are you asleep?",
        "D. Is it raining?",
    ),
    ("A. Water", "B. The letter 'R'", "C. A solid core", "D. Dust"),
    ("A. A balloon", "B. Your age", "C. Smoke", "D. An airplane"),
    (
        "A. He was born on Feb 29th",
        "B. He lives on another planet",
        "C. He counts differently",
        "D. He was born in a leap year",
    ),
    ("A. The floor", "B. Rain", "C. A towel", "D. The sun"),
    ("A. A window", "B. Silence", "C. A fast", "D. Your reputation"),
    ("A. A snake", "B. A coin", "C. A kite", "D. A shadow"),
)

# Pehle hum user ke guesses ko store karte hain.
guesses = []

# Ye tuple sahi answers rakhti hai.
answers = ("B", "C", "C", "C", "B", "B", "A", "C", "B", "B")

# Score aur question number ko initialize karte hain.
score = 0

ques_num = 0


# Ye loop har question ko display karta hai.
for question in questions:

    print()
    print("-------------------------------")
    print(question)

    for option in options[ques_num]:
        print(option)

    guess = input("Enter option (A, B, C, D): ").upper()
    guesses.append(guess)

    if guess == answers[ques_num]:
        score += 1
        print("CORRECT!")

    else:
        print("INCORRECT!")
        print(f"{answers[ques_num]} is the correct answer.")

    ques_num += 1


# Ye results ko display karta hai.
print("------------RESULTS------------")

print("AMSWERS: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("GUESSES: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)

print(f"Your score: {score}%")

print("-------------------------------")
