# Time module import karte hain.
import time

program = None

# Ye main loop hai jo countdown ko repeat karta hai.
while not program == "Q":

    # Pehle hum timer duration input leta hun.
    timer_duration = int(input("Enter the time in seconds: "))

    # Ye loop countdown ko dekh raha hai.
    for counter in range(timer_duration, -1, -1):

        # Idhar seconds, minutes, aur hours ko calculate karte hain.
        seconds = counter % 60
        minutes = int(counter / 60) % 60
        hours = int(counter / 3600)

        # Ye emoji ke hisaab se time ko display karta hai.
        if counter >= 500:
            print(f"{hours:02}:{minutes:02}:{seconds:02} 🤣🤣🤣 ")

        elif counter >= 250:
            print(f"{hours:02}:{minutes:02}:{seconds:02} 😂😂😂 ")

        elif counter >= 100:
            print(f"{hours:02}:{minutes:02}:{seconds:02} 😁😁😁 ")

        elif counter >= 50:
            print(f"{hours:02}:{minutes:02}:{seconds:02} 🙂🙂🙂 ")

        elif counter >= 25:
            print(f"{hours:02}:{minutes:02}:{seconds:02} 😐😐😐 ")

        elif counter >= 10:
            print(f"{hours:02}:{minutes:02}:{seconds:02} 😟😟😟 ")

        elif counter >= 5:
            print(f"{hours:02}:{minutes:02}:{seconds:02} 😨😨😨 ")

        elif counter >= 1:
            print(f"{hours:02}:{minutes:02}:{seconds:02} 😭😭😭 ")

        else:
            print(f"{hours:02}:{minutes:02}:{seconds:02} 💀💀💀 ")

        time.sleep(1)

    print("Time's up! ⏰")

    program = input("Q to quit or any other key to run again: ").upper()

print("Thanks for using my program.")
