# "Calculator"
# Joey Ilog
# Created: October 18, 2024
# Last Updated: October 18, 2024

# 10/18: simple float calculator that supports addition, subtraction, multiplication, and division for two inputs

# imports
import os

# global variables
x = 0
y = 0
z = 0
choice = 0

### prompts user with welcome, and asks for their input
def prompt():
    print("How would you like to proceed?")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    # exits function and returns user's input
    return(int(input("(-): ")))

### prompts user for their x and y inputs
def numbers(x, y):
    print("Please Enter X and Y: ")
    x = float(input("(X): "))
    y = float(input("(Y): "))

    # exits function and returns x and y
    return(x, y)

### main code

# asks user for their use of the calculator
print("Welcome to NNETHERR's Calculator! (v1.0)")
choice = prompt()

# keeps the calculator running based on user's choice
while True:
    # runs calculator tools based on user's choice
    if choice == 1: # addition
        print("\n", "[1] Addition")
        print("\n", "x + y = z", "\n")

        # prompts user for x and y inputs
        x, y = numbers(x, y)

        # runs calculation, stores answer in z
        z = x + y
    if choice == 2: # subtraction
        print("\n", "[2] Subtraction")
        print("\n", "x - y = z", "\n")

        # prompts user for x and y inputs
        x, y = numbers(x, y)

        # runs calculation, stores answer in z
        z = x - y
    if choice == 3: # multiplication
        print("\n", "[3] Multiplication")
        print("\n", "x * y = z", "\n")

        # prompts user for x and y inputs
        x, y = numbers(x, y)

        # runs calculation, stores answer in z
        z = x * y
    if choice == 4: # division
        print("\n", "[4] Division]")
        print("\n", "x / y = z", "\n")

        # prompts user for x and y inputs
        x, y = numbers(x, y)

        # runs calculation, stores answer in z
        z = x / y
    if choice == 5: # exit
        break

    # prints out answer and asks user for next option
    print("Your Answer: ", z, "\n")
    choice = prompt()

# thanks the user for using the calculator
print("\n", "Thank you for using NNETHERR's Calculator! (v1.0)")
