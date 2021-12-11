import random
def rolling():
    diceCommand = input("Write \"roll\" to roll the dices: ")
    diceNumber = random.randint(1, 6)
    if diceCommand == "roll":
        print(diceNumber)
        ask()
def ask():
    ContinueCommand = input("Will you continue? y/n: ")
    if ContinueCommand == "y":
        rolling()
    elif ContinueCommand == "n":
        quit()
    else:
        print("The string was incorrect.")
        ask()
rolling()
