import random

def run():
    computer = random.randint(1,3)

    userChoice = int(input("Input a number 1 - 3 (1 is rock, 2 is paper, and 3 is scissors): "))

    if 4 > userChoice > 0:
        if computer == userChoice:
            print("Its A Tie!")
        elif computer > userChoice or computer == 1 and userChoice == 3:
            print("Computer Wins!")
        elif userChoice > computer or userChoice == 1 and computer == 3:
            print("You Win!")
    else:
        try_again = input("Invalid number would you like to try again? ")
        if try_again.capitalize == "Yes":
            run()
        else:
            pass
run()