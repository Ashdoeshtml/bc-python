# Pehle main operator ke liye user input leta hun.
operator = input("Enter an operator (+, -, *, /): ")

# Phir dono value/number bhi mangvata hun.
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Idhar sabse pehle maine check karvaya ki ye dono number 0 to nahi hain na?
if num1 == 0 and num2 == 0:
    print("You have entered 0 for both.")
    print("The result will be zero in every case.")

# Ye sab operator ke hisaab se calculate krne ke liye.
elif operator == "+":
    result = num1 + num2

elif operator == "-":
    result = num1 - num2

elif operator == "*":
    result = num1 * num2

elif operator == "/":
    result = num1 / num2

# Idhar ye `else` check karta hain ki kisine koi operator nahi dala kya.
else:
    result = None
    print("You didn't enter an operator.")
    print("Please enter an operator.")

# Ye result print karta based on previous calculations.
print(f"The result is: {round(result, 3)}")
