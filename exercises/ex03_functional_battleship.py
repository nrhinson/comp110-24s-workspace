"""EX03 - Functional Battleship"""

__author__ = "730664337"

import random

def main(grid_size: int, secret_row: int, secret_column: int) -> None:
    turn_count: int = 1
    win_check: bool = False
    while turn_count < 6 and win_check == False:
        print(f"=== Turn {turn_count}/5 ===")
        row_guess: int = input_guess(grid_size, "row")
        column_guess: int = input_guess(grid_size, "column")
        correct_check: int = correct_guess(secret_column, secret_column, row_guess, column_guess)
        print_grid(grid_size, row_guess, column_guess, correct_check)
        if correct_check:
            print(f"Hit!")
            print(f"You won in {turn_count}/5 turns!")
            win_check = True
        else:
            print("Miss!")
        turn_count += 1
    if correct_check == False:
        print("X/5 - Better luck next time!")
    


def input_guess(board_size: int,type_of_guess: str) -> int:
    assert type_of_guess == "row" or type_of_guess == "column"
    player_input: int = int(input(f"Guess a {type_of_guess}: "))
    while (player_input < 1 or player_input > board_size):
        player_input: int = int(input(f"The grid is only {board_size} by {board_size}. Try again: "))
    return player_input

def print_grid (board_size: int, row_guess: int, column_guess: int, correct_check: bool) -> None:
    # Initalize variables
    BLUE_BOX: str = "\U0001F7E6"
    RED_BOX: str = "\U0001F7E5"
    WHITE_BOX: str = "\U00002B1C"
    battle_ship_board: str = ""
    row_counter: int = 1
    column_counter: int = 1
    while (row_counter < board_size + 1):
        while (column_counter < board_size + 1):
            if row_counter == row_guess and column_counter == column_guess:
                if correct_check == True:
                    battle_ship_board += RED_BOX
                else:
                    battle_ship_board += WHITE_BOX
            else:
                battle_ship_board += BLUE_BOX
            column_counter += 1
        print(battle_ship_board)
        battle_ship_board = ""
        column_counter = 1
        row_counter += 1


def correct_guess(secret_row: int, secret_column: int, guessed_row: int, guessed_column: int) -> bool:
    if(secret_row == guessed_row and secret_column == guessed_column):
        return True
    return False

if __name__ == "__main__":
        grid_size: int = random.randint(3, 5)
        main(grid_size, random.randint(1, grid_size), random.randint(1, grid_size))

