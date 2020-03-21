import random
import sys

def main():
    CPUNum = rand.randint(1, 21)
    print("Guess a number between 1 and 20: ")
    userGuess = input()
    if userGuess == CPUNum:
        print("Correct! Want to play again? (Y/N)")
        playAgain = input();
        if playAgain == 'Y':
            main()
        elif playAgain == 'N':
            print("Thank you!")
