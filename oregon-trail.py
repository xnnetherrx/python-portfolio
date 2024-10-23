# "Oregon Trail"
# Joey Ilog
# Created: October 21, 2024
# Last Updated: October 23, 2024

# 10/23: traditional oregon trail, user must travel and survive across a set number of miles

# imports
import os
import time
import random

# global variables
route = 0 # distance in miles
daily_distance = 0 # randomized number of miles travelled in a day (15 - 25)
days = 0 # number of days travelled

health = 100
food = 100
supplies = 100
money = 100
name = "" # used for user's name
difficulty = 0 # (1 = easy, 2 = normal, 3 = expert)
decision = 0 # used for user's option menu
rate = 1.0 # used to calculate health drainage

r = random.SystemRandom()

### screen clearing
def clear():
    os.system('clear')
    return()

### start menu
def start_menu():
    clear()

    # prompts user with start menu, asks for their options to continue
    print("Welcome to NNETHERR's Oregon Trail! (v1.0)")
    print("How would you like to proceed? ")
    print("1. Start my Journey")
    print("2. Exit")
    x = int(input("(-): "))

    # proceeds based on selected option
    if x == 1:
        y = select_diff()
    if x == 2:
        goodbye()

    return(y)

### difficulty selection
def select_diff():
    clear()

    # prompts user with difficulty selection menu
    print("Please select a Difficulty: ")
    print("1. Quick")
    print("2. Normal")
    print("3. Expert")
    x = int(input("(-): "))

    # returns difficulty selected by user
    return(x)

### player customization
def player():
    y = 'N'

    while y == 'N':
        clear()

        # prompts user with option to enter their name
        print("What is your name?")
        x = str(input("(-): "))

        clear()

        # double-checks the user wants to continue with the name
        print("Is your name:", x, "?")
        print("(Y)es, or (N)o?")
        z = str(input("(-): "))

        if x == 'Y':
            break

        return(x)

### player status menu
def status(name, health, food, supplies, money, daily_distance, difficulty, days):
    clear()

    # calculates distance left
    if difficulty == 1:
        x = 500 - daily_distance
    if difficulty == 2:
        x = 1000 - daily_distance
    if difficulty == 3:
        x = 2000 - daily_distance
    
    # separator
    print("*********************************")

    # displays the user's basic stats
    print("Name:", name)
    print("Health:", health)
    print("Food:", food)
    print("Supplies:", supplies)
    print("Money:", money)

    # separator
    print("*********************************")

    # displays travel statistics
    print("Time Elapsed (in days):", days)
    print("Distance Traveled (mi):", daily_distance)
    print("Distance Left (mi):", x)

    # separator
    print("*********************************")

    return()

### in-game player options menu
def menu(daily_distance, difficulty):

    # prompts user with options
    print("How would you like to proceed?")
    print("1. Travel")
    print("2. Hunt / Forage")
    print("3. Rest")
    print("4. Forfeit")

    x = int(input("(-): "))

    # returns user's decision to main code
    return(x)

### travelling mechanics
def travel():
    x = random.randint(15, 25)
    return(x)

### loss mechanics
def loss():
    clear()

    print("You failed to cross the Oregon Trail and passed away!", "\n")
    goodbye(days, daily_distance, route)

### win mechanics
def win():
    clear()

    print("You have successfully crossed the Oregon Trail! Congratulations!", "\n")
    goodbye(days, daily_distance, route)

### goodbye, and lists all stats
def goodbye(days, daily_distance, route):
    print("You Traveled:", days, "Days!")
    print("You Made it:", daily_distance, "mi", "/", route, "mi", "\n")
    
    print("Thank you for playing NNETHERR's Oregon Trail! (v1.0)")
    quit()

### main code
difficulty = start_menu()

# asks for and stores the user's name
name = player()

if difficulty == 1:
    route = 500
if difficulty == 2:
    route = 1000
if difficulty == 3:
    route = 2000

# keeps game running
while True:

    # ensures user's health doesn't go above 100 or below 0
    if health > 100:
        health = 100
    if health <= 0:
        health = 0

        # triggers loss
        loss()

    # starts the game
    status(name, health, food, supplies, money, daily_distance, difficulty, days)

    # prompts user with options
    decision = menu(daily_distance, difficulty)

    # proceeds based on player's decision
    if decision == 1: # travelling
        daily_distance += travel()

        # takes resources at random
        health -= random.randint(0, 20)
        supplies -= random.randint(5, 15)
        food -= random.randint(5, 7)
        
        # increases number of days travelled    
        days += 1
    if decision == 2: # hunting / foraging
        health -= random.randint(0, 5)
        food += random.randint(0, 10) # hunting yield
        supplies += random.randint(3, 15) # foraging yield

        # increases number of days travelled    
        days += 1
    if decision == 3: # resting
        health += random.randint(5, 20)
        supplies -= random.randint(2, 8)
        food -= random.randint(3, 6)

        # increases number of days travelled    
        days += 1
    if decision == 4: # forfeit
        goodbye(days, daily_distance, route)
    
    # ensures user's supplies doesn't go above 100 or below 0
    if supplies > 100:
        supplies = 100
    if supplies <= 0:
        supplies = 0

        # increased health drainage
        health -= random.randint(5, 10)

    # ensures user's food suplies doesn't go above 100 or below 0
    if food > 100:
        food = 100
    if supplies <= 0:
        food = 0

        # increased health drainage
        health -= random.randint(8, 15)

    # checks if user made it across Oregon Trail
    if daily_distance >= route:
        win()