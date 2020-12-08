"""
This program will roll a pair of dice and ask the user to guess the sum.
If the user's guess is equal to the total value of the dice roll, the user wins.
If not the computer wins.
The program will do the following:
1. Roll a pair of dice
2. Add the values of the roll
3. Ask the user for sides on a dice
4. Ask the user to guess a number
5. Compare user's guess with total value
6. Determine the winner
"""

from random import randint #simulates randomness
from time import sleep #simulates waiting

# get_dice_sides function will prompt the user to enter the number of sides on the dice  
def get_dice_sides():
    dice_sides = int(input("How many sides will the dice have? "))
    sleep(1)
    return(dice_sides)

# get_user_guess will prompt the user to guess a number
def get_user_guess():
    guess = int(input("Guess a number: "))
    print("")
    return guess

# determine_winner function will compare user's guess to the dice total to see who won
def determine_winner(total_roll, guess):
    print("Calculating results...")
    sleep(3)
    print("The total is: %d" %total_roll)
    sleep(2)

    if total_roll == guess:
        print("WINNER! WINNER!")
    else:
        print("...You LOST...")

# this function will begin the game and call for the other function needed to properly play the game
def roll_dice(number_of_sides):
    first_roll = randint(1, number_of_sides)
    second_roll = randint(1, number_of_sides)
    max_val = number_of_sides * 2
    print("The largst guessable number is %d" %max_val)
    print("")
    sleep(1)
    guess = get_user_guess()
    if guess > max_val:
        print("You are guess too high")
    else :
        print("Rolling....")
        sleep(2)
    
    print("The 1st roll is: %d" %first_roll)
    print("")
    sleep(1)
    print("Rolling....")
    sleep(2)
    print("The 2nd roll is: %d" %second_roll)
    print("")

    total_roll = first_roll + second_roll
    
    determine_winner(total_roll, guess)

# call to function to begin the game
roll_dice(get_dice_sides())






    
