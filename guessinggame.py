#made by Hanfei Chen
#the guessing game
#2023-09-21

import random

def guessing_game():
    game = True
    number = random.randint(1, 100) # choose a random number between 1 and 100
    while game: #sets a loop
        try:  # incase there is a error in the next block
          guess = int(input("enter random number between 1 and 100:\n"))
        except ValueError: # if the error is guess isnt a number return "only enter number"
            print("only enter numbers")
        if guess == number: # if player guess equal to the number chosen by the random.randint will break the loop
            print("Correct!")
            game = False #break the loop

guessing_game()  # start the game