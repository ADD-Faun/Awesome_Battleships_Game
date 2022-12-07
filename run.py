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
numbers = [1, 2, 3, 4, 5, 6, 7]
letters = "ABCDEFGHIJKLMNOP"
grid = {}
grid_size = 6
num_ships = 5


def accept_shot_validate():
    """Take user input and check if valid"""
    valid_shot = False
    row = -1
    col = -1

    while not valid_shot:

        row = int(input(f"Choose a row from {row_num}"))
        if row not in row_num:
            print(f"Row not valid please choose a number from {row_num}")
            continue

        col = input(f"Choose a column from {col_letter}")
        col = col.upper()
        if col not in col_letter:
            print(f"Column not valid please choose a letter from {col_letter}")
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


def create_grid():
    """create gris and place ships on it"""

    for row in range(0, grid_size):
        for col in range(0, grid_size):
            x = "."
            grid.update({f"{numbers[row]}{letters[col]}": x})

    ships_placed = 0
    rows, cols = (grid_size, grid_size)

    while ships_placed != num_ships:
        random_row = random.randint(1, rows)
        random_col = random.randint(0, cols - 1)
        print(random_row)
        col = letters[random_col]
        print(col)
        if validate_place_ship(random_row, col):
            ships_placed += 1


def print_grid():
    """prints grid with symbols showing water , ships , hits and misses"""
    debug_mode = True

    for row in range(0, grid_size):
        for col in range(0, grid_size):
            x = grid[f"{numbers[row]}{letters[col]}"]
            if x == "#":
                if debug_mode:
                    print("#", end=" ")
                else:
                    print(".", end=" ")
            else:
                print(grid[f"{numbers[row]}{letters[col]}"], end=" ")
        print("")


def testing():
    """testing code"""

    for row in range(0, 6):
        for col in range(0, 6):
            x = "x"
            grid.update({f"{numbers[row]}{letters[col]}": x})


# chooses a position  to place ship
def place_ship():
    """chooses where to place ships on the grid"""


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
    end_game = input("do you wish to continue Y / N")
    end_game = end_game.upper()
    if end_game == "N":
        exit()


def play_game():
    """Runs the game using known username"""
    print_grid()
    hit_miss()
    finish_game()


create_grid()
print(grid)
print_grid()
