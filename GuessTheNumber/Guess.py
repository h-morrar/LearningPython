import random as rand
import sys

def main():
    CPUNum = rand.randint(1, 21)
    print("Guess a number between 1 and 20: ")
    userGuess = int(input())
    while(userGuess != CPUNum):
        if userGuess < CPUNum:
            print("Higher!")
            userGuess = int(input())
        else:
            print("Lower!")
            userGuess = int(input())
    if userGuess == CPUNum:
        print("Correct! Want to play again? (Y/N)")
        again = input()
        playAgainCheck(again)

def playAgainCheck(userAgain):
    if userAgain == 'Y' or userAgain == 'y':
        main()
    elif (userAgain == 'N') or (userAgain == 'n'):
        print("Thank you!")
        sys.exit()
    else:
        print("Sorry I couldn't understand. Play again? (Y/N)")
        userAgain = input()
        playAgainCheck(user)

main()
