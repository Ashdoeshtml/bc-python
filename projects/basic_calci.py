# First, I get user input for the operator.
operator = input("Enter an operator (+, -, *, /): ")

# Then, I ask for both numbers.
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Here, first I check if both numbers are zero or not.
if num1 == 0 and num2 == 0:
    print("You have entered 0 for both.")
    print("The result will be zero in every case.")

# Calculate based on the operator entered.
elif operator == "+":
    result = num1 + num2

elif operator == "-":
    result = num1 - num2

elif operator == "*":
    result = num1 * num2

elif operator == "/":
    result = num1 / num2

# Here, the else clause checks if no valid operator was entered.
else:
    result = None
    print("You didn't enter an operator.")
    print("Please enter an operator.")

# Print the result based on previous calculations.
print(f"The result is: {round(result, 3)}")
