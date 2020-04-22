#Number Guessing Game written in Python by Benjamin Patrick EYOH (Bhenjameen)

import random

#Declare variables
guess = None
numOfTries = None
maxNum = None
minNum = 1
start = None
gameOver = 1

name = input('\n\nWelcome to Number Guessing Game. \nPlease enter your name:-   ')

print('\nHello', name, ', the rule of the GAME is simple. \nI will think of a number and you will guess the number. \nPlease choose your level\n')

#Highlight and explain levels of the game
print("easy:     (Guess between 1 and 10 with 6 guesses)")
print("medium:   (Guess between 1 and 20 with 4 guesses)")
print("hard:     (Guess between 1 and 50 with 3 guesses)\n")

#User is able to set the level they want to play
level = input('Type your level and press "ENTER" to continue:-   ')

if level == "easy":
    numOfTries = 6
elif level == "medium":
    numOfTries = 4
elif level == "hard":
    numOfTries = 3

if level == "easy":
    maxNum = 10
elif level == "medium":
    maxNum = 20
elif level == "hard":
    maxNum = 50

print('\nYou chose', level, 'level')
print('You have', numOfTries, 'chances\n')
start = input('Press "ENTER" to start')

magicNumber = random.randint(minNum, maxNum+1)

#Game starts
while numOfTries > 0:
    print('\nI am thinking of a number between', minNum, 'and', maxNum)
    guess = input('Guess the number:  ')
    
    #Integer input validation and win and lose declarations
    try:
        int(guess)
    
        if guess == magicNumber:
            print('You got it right!')
            break
        elif numOfTries <= gameOver:
            print('\nThat was wrong')
            print('You are out of chances')
            print("Game Over!!! You Lose.")
            break
        else: 
            numOfTries -= 1
            print('\nThat was wrong, try again.')
            print('You have', numOfTries, 'chance(s) left')
    except:
        print("\nThat is not a number. \nPlease check your input and ensure it is a number")
#End of game