"""EX01 - Simple Battleship - A cute step toward Battleship."""

__author__ = "730664337"

# Initalize variables

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"
battleShipBoard: str = ""

# Record player 1 input and check it
Player1Input: int = int(input("Pick a secret boat location between 1 and 4: "))

if Player1Input < 1:
    print("Error! " + str(Player1Input) + " too low!")
    exit()
elif Player1Input > 4:
    print("Error! " + str(Player1Input) + " too high!")
    exit()

# Record player 2 input and check it
Player2Guess: int = int(input("Guess a number between 1 and 4: "))

if Player2Guess < 1:
    print("Error! " + str(Player2Guess) + " too low!")
    exit()

if Player2Guess > 4:
    print("Error! " + str(Player2Guess) + " too high!")
    exit()

# Compare player 1 input and player 2 input and print result
if Player2Guess == Player1Input:
    if Player2Guess == 1:
        battleShipBoard += RED_BOX
    else:
        battleShipBoard += BLUE_BOX
    if Player2Guess == 2:
        battleShipBoard += RED_BOX
    else:
        battleShipBoard += BLUE_BOX
    if Player2Guess == 3:
        battleShipBoard += RED_BOX
    else:
        battleShipBoard += BLUE_BOX
    if Player2Guess == 4:
        battleShipBoard += RED_BOX
    else:
        battleShipBoard += BLUE_BOX
    print(battleShipBoard)
    print("Correct! You hit the ship.")
    
else:
    if Player2Guess == 1:
        battleShipBoard += WHITE_BOX
    else:
        battleShipBoard += BLUE_BOX
    if Player2Guess == 2:
        battleShipBoard += WHITE_BOX
    else:
        battleShipBoard += BLUE_BOX
    if Player2Guess == 3:
        battleShipBoard += WHITE_BOX
    else:
        battleShipBoard += BLUE_BOX
    if Player2Guess == 4:
        battleShipBoard += WHITE_BOX
    else:
        battleShipBoard += BLUE_BOX
    print(battleShipBoard)
    print("Incorrect! You missed the ship.")