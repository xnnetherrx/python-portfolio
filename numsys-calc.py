# "Number System Calculator"
# Joey Ilog
# Created: August 8, 2025
# Last Updated: August 19, 2025

# simple calculator for converting Decimal, Hexidecimal, and Binary between each other

# imports
import os
import re

# global variables
x = ""
y = ""
z = []
n = 0
m = 0
p = ""
value = ""
repeat = ""
resultNum = 0
resultChar = ""

### prompts user with welcome, and asks for their input
def prompt():
    print("What will you be converting? (Decimal, Binary, Hexadecimal)")

    # collects and saves 1st conversion unit
    x = input("(x): ")
    
    # collects and saves 2nd conversion unit
    print("To? (Decimal, Binary, Hexadecimal)")
    y = input("(y): ")

    z = [x, y]

    return(z)

### compares answers given and determines conversion
def compare(z):

    # selecting the 1st conversion unit
    if z[0][0] == 'D' or z[0][0] == 'd': # if decimal
        n = 1
    elif z[0][0] == 'B' or z[0][0] == 'b': # if binary
        n = 2
    elif z[0][0] == 'H' or z[0][0] == 'h': # if hexadecimal
        n = 3
    else:
        n = 99

    # selecting the 2nd conversion unit
    if z[1][0] == 'D' or z[1][0] == 'd': # if decimal
        n += 10
    elif z[1][0] == 'B' or z[1][0] == 'b': # if binary
        n += 20
    elif z[1][0] == 'H' or z[1][0] == 'h': # if hexadecimal

        n += 30
    else:
        n = 99

    return(n)

### asks users for value to convert
def cvalue():

    # asks for value to convert
    print("\nPlease enter value you wish to convert...")
    value = input("(-): ")

    return(value)


### converts input to decimal
def decimal(value):

    # detects binary or hex input to complete conversion
    if n == 13:
        resultNum = int(value, 16)
    else:
        resultNum = int(value, 2)

    print("\nYour Converted Value is:", resultNum)
    return()

### converts input to binary
def binary(value):

    # detects decimal or hex input to complete conversion
    if n == 23:
        value = int(value, 16)
        resultChar = bin(value)
    else:
        value = int(value)
        resultChar = bin(value)

    print("\nYour Converted Value is:", resultChar[2:])
    return()

### converts input to hexadecimal
def hexadecimal(value):

    # detects decimal or binary input to complete conversion
    if n == 32:
        value = int(value, 2)
        resultChar = hex(value)
    else:
        value = int(value)
        resultChar = hex(value)
    

    print("\nYour Converted Value is:", resultChar[2:])
    return()

### main code

# asks user for their use of the calculator
print("Welcome to NNETHERR's Number System Calculator! (v1.0)\n")
z = prompt()

while True:

    # compares the answers and determines what is being converted to what
    n = compare(z)

    # calls appropriate conversion function, if inputs are same, will be voided
    if n == 21: # decimal to binary

        # calls function to input X and Y
        value = cvalue()

        # calls respective function to convert X and Y
        binary(value)

    elif n == 31: # decimal to hexadecimal

        # calls function to input X and Y
        value = cvalue()

        # calls respective function to convert X and Y
        hexadecimal(value)

    elif n == 12: # binary to decimal

        # calls function to input X and Y
        value = cvalue()

        # calls respective function to convert X and Y
        decimal(value)

    elif n == 32: # binary to hexadecimal

        # calls function to input X and Y
        value = cvalue()

        # calls respective function to convert X and Y
        hexadecimal(value)

    elif n == 13: # hexadecimal to decimal

        # calls function to input X and Y
        value = cvalue()

        # calls respective function to convert X and Y
        decimal(value)

    elif n == 23: # hexadecimal to binary

        # calls function to input X and Y
        value = cvalue()

        # calls respective function to convert X and Y
        binary(value)

    else:
        print("\nError in your conversion unit inputs.")
        
    # re-prompts the user if they want to continue
    print("\nWould you like to restart? (y, n)")
    repeat = input("(-): ")

    # checks if user wants to continue
    if repeat == 'y' or repeat == 'Y':
        os.system('clear')
        z = prompt()
    else:
        break

# thanks the user for using the calculator
print("\nThank you for using NNETHERR's Calculator! (v1.0)")
    