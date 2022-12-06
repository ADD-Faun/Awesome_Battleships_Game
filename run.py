# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
"""
    Legend:
    1. "." = water or empty space
    2. "#" = part of ship
    3. "X" = part of ship that was hit with bullet
    4. "O" = water that was shot with bullet, a miss because it hit no ship
"""
import random

rows = [1, 2, 3, 4, 5, 6]
columns = ['A', 'B', 'C', 'D', 'E', 'F']


def accept_shot_validate():
    """Take user input and check if valid"""
    valid_shot = False
    row = -1
    col = -1

    while not valid_shot:

        row = int(input(f"Choose a row from {rows}"))
        if row not in rows:
            print(f"Row not valid please choose a number from {rows}")
            continue

        col = input(f"Choose a column from {columns}")
        col = col.upper()
        if col not in columns:
            print(f"Column not valid please choose a letter from {columns}")
            continue
        print(row)
        print(col)
        if grid[row][col] == "X" or grid[row][col] == "O":
            break

        valid_shot = True
    return row, col


def hit_miss():
    """checks if shot hit or miss. updates board and player"""
    row, col = accept_shot_validate()
    if row == 4:
        print(row)
    else:
        print(row, col)


def print_grid():
    """prints grid with symbols showing water , ships , hits and misses"""
    for row in range(len(rows)):
        for col in range(len(columns)):
            print(".", end=" ")
        print("")


# chooses a position  to place ship
def place_ship():
    """chooses where to place ships on the grid"""


# checks ship placement is avalible
def validate_place_ship():
    """checks if ship placement is valid"""


# checks if either side has lost all their ships
def finish_game():
    """checks if game is won or if it should continue"""


def play_game():
    print_grid()
    hit_miss()

play_game()
