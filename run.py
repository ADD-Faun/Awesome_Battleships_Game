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

num = [x for x in range(1, 27)]
LET = [chr(x) for x in range(65, 91)]
grid = {}
grid_c = {}
grid_size = 5
num_ships = 5
game_over = False
comp_ships = num_ships
user_ships = num_ships
shots = 0
hits = 0
player_name = ""
LINE = "--------------------------------"


def accept_shot_validate(use):
    """Take user input and check if valid"""
    valid_shot = False
    row_choices = f"Choose a row between {num[0]}-{num[grid_size - 1]}\n"
    col_choices = f"Choose a column between {LET[0]}-{LET[grid_size - 1]}\n"
    bad = ("", " ", "[", "]", ",")

    while not valid_shot:
        row = "-1"
        while row in bad or row not in str(num[0:grid_size - 1]):
            row = input(row_choices)
            if row in bad or row not in str(num[0:grid_size - 1]):
                print(f"{row} is invalid")

        col = "-1"
        while col not in LET:
            col = input(f"{col_choices}")
            col = col.upper()
            if col not in LET:
                print(f"{col} is invalid")

        row = int(row) - 1
        col = ord(col) - 65

        if grid_dict(row, col, use) == "X" or grid_dict(row, col, use) == "O":
            print(f"You have already shot {row + 1}{LET[col]}")
            continue

        valid_shot = True
    return row, col


def grid_dict(row, col, user):
    """grid referencing either computer or player based on input"""
    if user:
        return grid[f"{num[row]}{LET[col]}"]
    else:
        return grid_c[f"{num[row]}{LET[col]}"]


def grid_update(row, col, user):
    "update computers grid or players grid based on input"
    if user:
        grid.update({f"{num[row]}{LET[col]}": "X"})
    else:
        grid_c.update({f"{num[row]}{LET[col]}": "X"})


def print_col_letters():
    """prints out the column letters at top and bottom of grid to read easy"""
    print(" ", end=" ")
    for row in range(0, grid_size):
        print(LET[row], end=" ")
    print("")


def hit_miss(user):
    """checks if shot hit or miss. updates board and player"""
    global comp_ships
    global user_ships

    if not user:
        row = random.randint(0, grid_size - 1)
        col = random.randint(0, grid_size - 1)
    else:
        row, col = accept_shot_validate(user)

    target = f"{num[row]}{LET[col]}"

    if grid_dict(row, col, user) == "#":
        if not user:
            grid_c.update({f"{num[row]}{LET[col]}": "X"})
            user_ships -= 1
        else:
            grid.update({f"{num[row]}{LET[col]}": "X"})
            comp_ships -= 1
            score(1, 1, target)

    else:
        if not user:
            grid_c.update({f"{num[row]}{LET[col]}": "O"})
        else:
            grid.update({f"{num[row]}{LET[col]}": "O"})
            score(1, 0, target)


def create_grid(user):
    """create gris and place ships on it"""

    for row in range(0, grid_size):
        for col in range(0, grid_size):
            if not user:
                grid_c.update({f"{num[row]}{LET[col]}": "."})
            else:
                grid.update({f"{num[row]}{LET[col]}": "."})

    ships_placed = 0

    while ships_placed != num_ships:
        random_row = random.randint(0, grid_size - 1)
        random_col = random.randint(0, grid_size - 1)
        if validate_place_ship(random_row, random_col, user):
            ships_placed += 1


def print_grid(user):
    """prints grid with symbols showing water , ships , hits and misses"""
    debug_mode = False

    print_col_letters()

    for row in range(0, grid_size):
        print(f"{num[row]}", end=" ")
        for col in range(0, grid_size):
            position = grid_dict(row, col, user)
            if position == "#":
                if debug_mode or not user:
                    print("#", end=" ")
                else:
                    print(".", end=" ")
            else:
                print(grid_dict(row, col, user), end=" ")
        print(f"{num[row]}", end=" ")
        print(" ")

    print_col_letters()


def testing():
    """testing code"""


# chooses a position  to place ship
def score(shot, hit, target):
    """keeps and prints score"""
    global shots
    global hits
    word = "shot"

    shots += shot
    hits += hit

    if shots > 1:
        word = "shots"
    print(LINE)
    if hit:
        print(f"Weldone you've hit an ememy ship on {target}")
    else:
        print(f"Too bad no enemy ship on {target}")
    print(f"After {shots} {word} you have {user_ships} left floating")
    print(f"Your enemy has {comp_ships} left for you to sink.")
    print(LINE)


# checks ship placement is avalible
def validate_place_ship(row, col, user):
    """checks if ship placement is valid for user or comp"""
    valid = True
    if grid_dict(row, col, user) != ".":
        valid = False
    elif grid_dict(row, col, user) == ".":
        row = num[row]
        col = LET[col]
        if not user:
            grid_c.update({f"{row}{col}": "#"})
        else:
            grid.update({f"{row}{col}": "#"})

    return valid


# checks if either side has lost all their ships
# or asks if user wants to continue
def finish_game():
    """checks if game is won or if it should continue"""
    global game_over
    game_over = False

    if comp_ships == 0 or user_ships == 0:
        game_over = True
        print(LINE)
        if comp_ships == 0:
            print(f"weldone {player_name} you sunk all the enemy ships")
        else:
            print(f"Too bad {player_name} they sunk all your ships")
        print(f"you had {user_ships} ships left floating of {num_ships}")
        print(f"Your enemy had {comp_ships} left floating of {num_ships}")
        print(LINE)

    else:
        end_game = input("Press anykey to continue or N to quit game\n")
        end_game = end_game.upper()
        if end_game == "N":
            game_over = True
            print(LINE)
            print(f"you had {user_ships} ships left floating of {num_ships}")
            print(f"Your enemy had {comp_ships} left floating of {num_ships}")
            print(LINE)


def play_game():
    """Runs the game using known username"""
    create_grid(True)
    create_grid(False)
    print(f"Welcome {player_name}")

    while not game_over:
        print_grid(True)
        print("^^Enemy Grid^^")
        print("Your Grid below")
        print_grid(False)
        hit_miss(False)
        hit_miss(True)
        finish_game()
    again = input("Press anykey to play again or N to end\n")
    again = again.upper()
    if again == "N":
        print("Goodbye it was fun playing")
    else:
        set_board()
        play_game()


def set_board():
    """puts score and ships used back to 0"""
    global shots
    shots = 0
    global hits
    hits = 0
    global comp_ships
    comp_ships = num_ships
    global user_ships
    user_ships = num_ships
    global grid
    grid = {}
    global grid_c
    grid_c = {}
    global game_over
    game_over = False


def change_grid_size():
    """lets the player change the grid size"""
# currently unused as players could make the grid too big for screen
    global grid_size
    global num_ships
    size = input("choose a size between 4-26 for the square grids")
    while not size > 4 and not size < 27:
        size = input("Grid size must be between 4-26")
    grid_size = size
    ships = input(f"choose number of ships between 1-{grid_size**-1}")
    num_ships = ships


player_name = input("what is your name?\n")
print(num)
play_game()
