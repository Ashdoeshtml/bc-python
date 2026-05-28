import random

from wordslist import words

hangman_art = {
    0: ("   ", "   ", "   "),
    1: (" ° ", "   ", "   "),
    2: (" ° ", " | ", "   "),
    3: (" ° ", "/| ", "   "),
    4: (" ° ", "/|\\", "   "),
    5: (" ° ", "/|\\", "/  "),
    6: (" ° ", "/|\\", "/ \\"),
}


def display_man(wrong_guesses):

    print("*****")
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("*****")


def display_hint(hint):
    print(" ".join(hint))


def display_answer(answer):
    print(" ".join(answer))


def main():

    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True

    while is_running:

        display_man(wrong_guesses)
        display_hint(hint)

        guess = input("Enter your guess: ").lower()

        if len(guess) != 1:
            print("invaid input")
            continue

        if guess in guessed_letters:
            print(f"You have already guessed {guess}.")
            continue

        guessed_letters.add(guess)

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            wrong_guesses += 1

        if "_" not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print("👑 YOU WIN! 👑")
            is_running = False

        elif wrong_guesses >= 6:
            display_man(wrong_guesses)
            display_answer(answer)
            print("💀 YOU LOSE! 💀")
            is_running = False


if __name__ == "__main__":
    main()
