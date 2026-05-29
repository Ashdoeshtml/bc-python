# Import the time module.
import time

program = None

# This is the main loop that repeats the countdown.
while not program == "Q":

    # First, we take the timer duration as input.
    timer_duration = int(input("Enter the time in seconds: "))

    # This loop handles the countdown.
    for counter in range(timer_duration, -1, -1):

        # Here, we calculate seconds, minutes, and hours.
        seconds = counter % 60
        minutes = int(counter / 60) % 60
        hours = int(counter / 3600)

        # Display time based on the emoji for each time range.
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
