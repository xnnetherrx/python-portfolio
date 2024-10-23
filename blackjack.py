# "Blackjack"
# Joey Ilog
# Created: October 18, 2024
# Last Updated: October 23, 2024

# 10/23: traditional one-on-one blackjack with a realistic 52-card deck and betting system

### imports
import os
import time
import random

### global variables
choice = 0 # stores menu choice
move = '' # stores move selected
restart = '' # stores restart variable
hand = [] # holds cards drawn
player_hand = [] # saves player's hand to be shown at the end
player_sum = 0
dealer_sum = 0

difficulty = 0 # easy = $500, normal = $250, expert = $100
money = 0 # set based on chosen difficulty
bet = 0 # stores users bet for current hand

# defines card deck
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

# defines card values (ace is by default 11, will be used as 1 in certain situations)
values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}

# creates deck of cards
deck = [{'rank': rank, 'suit': suit} for rank in ranks for suit in suits]

### prompts user with menu options
def menu():
    print("How would you like to proceed?")
    print("1. Play")
    print("2. Exit")

    # exits function and returns user's input
    return(int(input("(-): ")))

### prompts user with difficulty options
def difficulty():
    print("Please select your difficulty (determines starting $$$ amount): ")
    print("1. Easy")
    print("2. Normal")
    print("3. Expert")
    x = int(input("(-): "))

    return(x)

### calculates total hand value
def total(hand):
    card = []
    value = 0
    i = 0

    # for loop to count and add each card individually
    for x in range(0, len(hand)):
        card = hand[x]
        value += values[card['rank']]
        
        # allows double-checking for aces to see if 1 or 11 is best fit
        if card['rank'] == 'A':
            i += 1
        while value > 21 and i:
            value -= 10
            i -= 1

    # exits function returning total hand value
    return value

### displays all cards in given and provides a total
def show_hand(hand):
    for x in range(0, len(hand)): # displays each card one by one
        card = hand[x]
        print("\n", f"{card['rank']} of {card['suit']}", end = " ")

    # displays total hand value
    print("\n")
    print("Total: ", total(hand), "\n")

    # exits function after displaying each card
    return()

### deal / hit, adds cards to current hand
def deal(deck):
    card = random.choice(deck)
    deck.remove(card)
    
    # exits function with chosen card from deck
    return card

### stand, stops further turns for current hand
def stand(hand):

    # displays total hand value
    print("\n")
    print("Your Total: ", total(hand), "\n")

### win calcualations and final messages
def win(money, bet):

    print("You Won!", "\n")

    # shows user how much money they have
    print("You Earned: $", bet*2)
    print("Your Balance: $", money, "\n")

    print("There are:", len(deck), "/ 52 Cards Left in this Deck", "\n")

### loss calculations and final messages
def loss(money, bet):

    print("You Lose!", "\n")

    # shows user how much money they have
    print("You Lost: $", bet)
    print("Your Balance: $", money, "\n")

    print("There are:", len(deck), "/ 52 Cards Left in this Deck", "\n")

### dealer turn behavior
def dealer(hand):

    # gives dealer two new cards
    hand.append(deal(deck))
    hand.append(deal(deck))

    # let's the dealer proceed based on suggestions
    print("Dealer's Hand: ")

    # "fake" shows dealer's cards similar to real blackjack
    card = hand[1]
    print("\n", f"{card['rank']} of {card['suit']}", end = " ")
    time.sleep(1)
    print("\n", "Hidden", end = " ")
    time.sleep(1)
    print("\n", "Hidden", end = " ")
    time.sleep(1)

    while total(hand) < 16:
        
        # hits card while dealer's total is under threshold
        hand.append(deal(deck))

        # presents dealer's cards hidden as if they're actually playing
        print("\n", "Hidden", end = " ")
        time.sleep(1)

    # checks to see if the dealer busted
    if total(hand) > 21:

        # clears the output screen
        os.system('clear')

        # dealer busts and player wins
        print("Dealer's Hand: ")
        for x in range(0, len(hand)): # displays each card one by one
            card = hand[x]
            print("\n", f"{card['rank']} of {card['suit']}", end = " ")

        # display's player's hand and totals
        print("\n")
        print("Player's Hand: ")
        for x in range(0, len(player_hand)): # displays each card one by one
            card = player_hand[x]
            print("\n", f"{card['rank']} of {card['suit']}", end = " ")
        print("\n")
        print("Your Total: ", player_sum, "\n")
        print("Dealer's Total: ", total(hand), "\n")
        print("Dealer has busted!")
        
    if total(hand) <= 21:
        # clears the output screen
        os.system('clear')

        # "flips" the dealer's cards
        print("Dealer's Hand: ")
        for x in range(0, len(hand)): # displays each card one by one
            card = hand[x]
            print("\n", f"{card['rank']} of {card['suit']}", end = " ")
        
        # display's player's hand and totals
        print("\n")
        print("Player's Hand: ")
        for x in range(0, len(player_hand)): # displays each card one by one
            card = player_hand[x]
            print("\n", f"{card['rank']} of {card['suit']}", end = " ")
        print("\n")
        print("Your Total: ", player_sum, "\n")
        print("Dealer's Total: ", total(hand), "\n")

    # exits function and returns to main code
    return()

### betting function
def user_bet(money):
    
    # shows user how much money they have
    print("Your Balance: $", money, "\n")

    # asks user for bet
    print("How much would you like to bet?")
    x = int(input("(-): $ "))

    return(x)

### main code

# clears the output screen
os.system('clear')

# welcomes user and prompts them with the menu
print("Welcome to NNETHERR's Blackjack! (v1.0)")
choice = menu()

# clears the output screen
os.system('clear')

# prompts the user for difficulty selection and saves their option
difficulty = difficulty()

# loads user balance based on decision
if difficulty == 1:
    money = 500
if difficulty == 2:
    money = 250
if difficulty == 3:
    money = 100

# clears the output screen
os.system('clear')

# keeps blackjack running if user specifies so
while True:
    if choice == 1: # keeps blackjack running
        move = 'H'

        # prompts user for betting before cards are drawn
        bet = user_bet(money)

        # clears the output screen
        os.system('clear')

        # deals user first card
        hand.append(deal(deck))

        # hits or stands based on user's input
        while move == 'H':
            hand.append(deal(deck))

            # prints out the user's current hand
            print("Your Current Hand: ")
            show_hand(hand)

            # double checks user hasn't busted
            if total(hand) > 21:
                print("You have busted!")
                loss(money, bet)
                break
            else:

                # asks user for their next move and stores their input
                print("How would you like to proceed?")
                print("(H)it? or (S)tand?")
                move = str(input("(-): "))

                # clears the output screen
                os.system('clear')

        if move == 'S':
            player_sum = total(hand) # saves player's hand total
            player_hand = hand
            stand(hand) # prints move, and calculates total

            # initiates dealer turn
            hand = []
            dealer(hand)
            
            # double checks if dealer busted
            if total(hand) > 21:
                dealer_sum = 0
            else:
                dealer_sum = total(hand)

            # compares who won and who lost
            if player_sum > dealer_sum:
                money += bet*2
                win(money, bet)
            if player_sum < dealer_sum:
                money = money - bet
                loss(money, bet)
            if player_sum == dealer_sum:
                print("It's a Tie!")
                print("Your Balance: $", money, "\n")

                print("There are:", len(deck), "/ 52 Cards Left in this Deck")

        # ensures user doesn't go below $0
        if money <= 0:
            print("You ran out of money!")
            break

        # reshuffles deck if close to empty
        if len(deck) <= 10:
            deck = [{'rank': rank, 'suit': suit} for rank in ranks for suit in suits]
            print("Deck has been reshuffled!")

        # asks if the user would like to play again
        print("\n", "Would you like to play again?", "\n")
        print("(Y)es or (N)o?")
        restart = str(input("(-): "))

        # continues based on the user's input
        if restart == 'Y':
            hand = []

            # clears the output screen
            os.system('clear')
        if restart == 'N':
            break

    if choice == 2: # exits if user chooses so
        break

# thanks the user for playing blackjack
print("Thank you for playing NNETHERR's Blackjack! (v1.0)")
