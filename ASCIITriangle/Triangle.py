def main():
    height = input("Input a number greater than 0: ")
    while height <= 0:
        print("Invalid Input.")
        height = input("Input a number greater than 0: ")
    makeTriangle(height)

def makeTriangle(height):
    i = 1
    while (i <= height-1):
        print(chr(9))
        i++
    rowCounter = 1
    
