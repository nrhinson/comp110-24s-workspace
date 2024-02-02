"""EX02 - One Shot Battleship"""

__author__ = "730664337"

# Initalize variables

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"
battle_ship_board: str = ""
secret_row: int = 3
secret_column: int = 2
player_row_input: int = 0
player_column_input: int = 0
grid_size: int = 4

# Prompt and record player inputs
player_row_input: int = int(input("Guess a row: "))
if(player_row_input > grid_size or player_row_input < 1):
    while (player_row_input > grid_size or player_row_input < 1):
        player_row_input: int = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))

player_column_input: int = int(input("Guess a column: "))
if(player_column_input > grid_size or player_column_input < 1):
    while (player_column_input > grid_size or player_column_input < 1):
        player_column_input: int = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))

# Anyalize numbers given and print appropriate board
row_counter: int = 1
column_counter: int = 1
while(row_counter < grid_size+1):
    while(column_counter < grid_size+1):
        if row_counter == player_row_input and column_counter == player_column_input:
            if player_row_input == secret_row and player_column_input == secret_column:
                battle_ship_board += RED_BOX
            else:
                battle_ship_board += WHITE_BOX
        else:
            battle_ship_board += BLUE_BOX
        column_counter += 1
    print(battle_ship_board)
    battle_ship_board: str = ""
    column_counter: int = 1
    row_counter += 1

# Print results and clue if needed
if player_row_input == secret_row and player_column_input == secret_column:
    print("Hit!")
else:
    if player_row_input == secret_row:
        print("Close! Correct row, wrong column.")
    elif player_column_input == secret_column:
        print("Close! Correct column, wrong row.")
    else:
        print("Miss!")