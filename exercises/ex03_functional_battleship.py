"""EX03 - Functional Battleship"""

__author__ = "730664337"

def input_guess(board_size: int,type_of_guess: str) -> int:
    assert type_of_guess == "row" or type_of_guess == "column"
    player_input: int = int(input(f"Guess a {type_of_guess}: "))
    while (player_input < 1 or player_input > board_size):
        player_input: int = int(input(f"The grid is only {board_size} by {board_size}. Try again: "))
    return player_input

def print_grid


