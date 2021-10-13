import random 

userInput = input("Write start : ")
while True:
    if userInput.lower() == "start":

        number = random.randint(1,6)
        print("The Dice is rolling.....")

        if number == 1:
            print("|     |")
            print("|  0  |")
            print("|     |")
        elif number == 2:
            print("|0    |")
            print("|     |")
            print("|    0|")
        elif number == 3:
            print("|0    |")
            print("|  0  |")
            print("|    0|")
        elif number == 4:
            print("|0   0|")
            print("|     |")
            print("|0   0|")
        elif number == 5:
            print("|0   0|")
            print("|  0  |")
            print("|0   0|")
        else:
            print("|0   0|")
            print("|0   0|")
            print("|0   0|")
    else:
        print("Sorry!")
        break
    playAgain = input(" Play again (y / n): ")
    if playAgain != "y":
        print("Rolling End!")
        break
