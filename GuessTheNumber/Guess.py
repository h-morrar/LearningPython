import random
import sys

def main():
    CPUNum = rand.randint(1, 21)
    print("Guess a number between 1 and 20: ")
    userGuess = input()
    while(userGuess != CPUNum):
        if userGuess < CPUNum:
            print("Higher!")
            userGuess = input()
        else:
            print("Lower!")
            userGuess = input()
    if userGuess == CPUNum:
        print("Correct! Want to play again? (Y/N)")
        again = input()
        playAgainCheck(again)

def playAgainCheck(userAgain):
    if playAgain == 'Y':
        main()
    elif playAgain == 'N':
        print("Thank you!")
        sys.exit()
    else:
        print("Sorry I couldn't understand. Play again? (Y/N)")
        again = input()
        playAgainCheck(again)s
