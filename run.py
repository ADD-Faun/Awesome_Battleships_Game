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

# Global variables
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
LET = "ABCDEFGHIJKLMNOP"
grid = {}
grid_size = 6
num_ships = 2
game_over = False
ships_sunk = 0
shots = 0
hits = 0
misses = 0
player_name = ""


def accept_shot_validate():
    """Take user input and check if valid"""
    valid_shot = False

    while not valid_shot:

        row = int(input(f"Choose a row from {num[0]}-{num[grid_size]}\n"))
        if row not in num:
            print(f"Invalid choose a row from {num[0]}-{num[grid_size]}\n")
            continue

        col = input(f"Choose a column from {LET[0]}-{LET[grid_size]}\n")
        col = col.upper()
        if col not in LET:
            print(f"Invalid choose a column from {LET[0]}-{LET[grid_size]}\n")
            continue

        row = row - 1
        col = ord(col) - 65
        if grid_dict(row, col) == "X" or grid_dict(row, col) == "O":
            print(f"You have already shot {row + 1}{LET[col]}")
            continue

        valid_shot = True
    return row, col


def grid_dict(row, col):
    """grid referencing """
    return grid[f"{num[row]}{LET[col]}"]


def hit_miss():
    """checks if shot hit or miss. updates board and player"""
    global ships_sunk

    row, col = accept_shot_validate()
    if grid_dict(row, col) == "#":
        print("hit")
        grid.update({f"{num[row]}{LET[col]}": "X"})
        ships_sunk += 1
        score(1, 1, 0)
    else:
        print("miss")
        grid.update({f"{num[row]}{LET[col]}": "O"})
        score(1, 0, 1)


def create_grid():
    """create gris and place ships on it"""

    for row in range(0, grid_size):
        for col in range(0, grid_size):
            x = "."
            grid.update({f"{num[row]}{LET[col]}": x})

    ships_placed = 0
    rows, cols = (grid_size, grid_size)

    while ships_placed != num_ships:
        random_row = random.randint(1, rows)
        random_col = random.randint(0, cols - 1)
        col = LET[random_col]
        if validate_place_ship(random_row, col):
            ships_placed += 1


def print_grid():
    """prints grid with symbols showing water , ships , hits and misses"""
    debug_mode = True

    print_col_letters()

    for row in range(0, grid_size):
        print(f"{num[row]}", end=" ")
        for col in range(0, grid_size):
            x = grid_dict(row, col)
            if x == "#":
                if debug_mode:
                    print("#", end=" ")
                else:
                    print(".", end=" ")
            else:
                print(grid[f"{num[row]}{LET[col]}"], end=" ")
        print(f"{num[row]}", end=" ")
        print(" ")

    print_col_letters()


def testing():
    """testing code"""


# chooses a position  to place ship
def score(shot, hit, miss):
    """keeps and prints score"""
    global shots
    global hits
    global misses

    shots += shot
    hits += hit
    misses += miss


# checks ship placement is avalible
def validate_place_ship(row, col):
    """checks if ship placement is valid"""
    valid = True
    if grid[f"{row}{col}"] != ".":
        valid = False
    elif grid[f"{row}{col}"] == ".":
        grid.update({f"{row}{col}": "#"})

    return valid


# checks if either side has lost all their ships
def finish_game():
    """checks if game is won or if it should continue"""
    global game_over
    game_over = False

    if ships_sunk == num_ships:
        game_over = True
        print(f"weldone {player_name} you sunk all the ships")
        score(0, 0, 0)

    else:
        end_game = input("do you wish to continue Y / N\n")
        end_game = end_game.upper()
        if end_game == "N":
            game_over = True
            score(0, 0, 0)


def play_game():
    """Runs the game using known username"""
    create_grid()
    print_grid()
    print(f"Welcome {player_name}")

    while not game_over:
        print_grid()
        hit_miss()
        finish_game()
    again = input("play again Y/N")
    again = again.upper()
    if again == "N":
        print("bye")
    else:
        set_board()
        play_game()


def set_board():
    """puts score and ships used back to 0"""
    global ships_sunk
    ships_sunk = 0
    global shots
    shots = 0
    global hits
    hits = 0
    global misses
    misses = 0
    global game_over
    game_over = False


def print_col_letters():
    """prints out the column letters at top and bottom of grid to read easy"""
    print(" ", end=" ")
    for row in range(0, grid_size):
        print(LET[row], end=" ")
    print("")


player_name = input("what is your name?\n")
play_game()
