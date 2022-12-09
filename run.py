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

NUM = [x for x in range(1, 81)]
LET = [chr(x) for x in range(65, 91)]
player_name = ""
LINE = "--------------------------------"
BAD = ("", " ", "[", "]", ",")


def set_board():
    """Sets global varibles needed for game to 0"""
    global shots
    shots = 0
    global hits
    hits = 0
    global grid
    grid = {}
    global grid_c
    grid_c = {}
    global game_over
    game_over = False


def change_grid_size():
    """lets the player change the grid size and choose number of ships"""
    global grid_size
    global num_ships
    global comp_ships
    global user_ships

    size = input("Choose a Grid size between 4-7\n")
    while size in BAD or size not in str(NUM[3:8]):
        print(f"'{size}' is invalid")
        size = input("choose a Grid size between 4-7\n")

    grid_size = int(size)

    ships = input(f"choose number of ships between 1-{grid_size**2 - 1}\n")
    while ships in BAD or ships not in str(NUM[0: grid_size**2 - 1]):
        print(f"'{ships}' is invalid")
        ships = input(f"choose number of ships between 1-{grid_size**2 - 1}\n")

    num_ships = int(ships)
    comp_ships = num_ships
    user_ships = num_ships


def accept_shot_validate(user):
    """Take user input and check if valid"""
    valid_shot = False
    row_choices = f"Choose a row between {NUM[0]}-{NUM[grid_size - 1]}\n"
    col_choices = f"Choose a column between {LET[0]}-{LET[grid_size - 1]}\n"
    row_range = str(NUM[0:grid_size])

    while not valid_shot:
        row = input(row_choices)
        while row in BAD or row not in row_range:
            print(f"'{row}' is invalid")
            row = input(row_choices)
                
        col = input(f"{col_choices}")
        col = col.upper()
        while col not in LET:
            print(f"'{col}'is invalid")
            col = input(f"{col_choices}")
            col = col.upper()

        row = int(row) - 1
        col = ord(col) - 65
        tar = target(row, col)

        if user[tar] == "X" or user[tar] == "O":
            print(f"You have already shot '{tar}'")
            continue

        valid_shot = True
    return row, col


def print_col_letters():
    """prints out the column letters at top and bottom of grid to read easy"""
    print(" ", end=" ")
    for row in range(0, grid_size):
        print(LET[row], end=" ")
    print("")


def print_row_numbers(row):
    """prints out row numbers for the side of the grid"""
    print(f"{NUM[row]}", end=" ")


def target(row, col):
    """takes row and column and returns dictionary key. makes
    future code smaller"""
    return f"{NUM[row]}{LET[col]}"


def hit_miss(user):
    """checks if shot hit or miss. updates board and player"""
    global comp_ships
    global user_ships

    if user == grid_c:
        row = random.randint(0, grid_size - 1)
        col = random.randint(0, grid_size - 1)
    else:
        row, col = accept_shot_validate(user)
    tar = target(row, col)

    if user[tar] == "#":
        info = "X"
        user[tar] = info
        if user == grid:
            comp_ships -= 1
            score(1, 1, tar)
        else:
            user_ships -= 1

    else:
        info = "O"
        user.update({tar: info})
        if user == grid:
            score(1, 0, tar)


def create_grid(user):
    """create gris and place ships on it"""

    for row in range(0, grid_size):
        for col in range(0, grid_size):
            tar = target(row, col)
            user.update({tar: "."})

    ships_placed = 0

    while ships_placed != num_ships:
        row = random.randint(0, grid_size - 1)
        col = random.randint(0, grid_size - 1)
        tar = target(row, col)
        if validate_place_ship(tar, user):
            ships_placed += 1


def print_grid(user):
    """prints grid with symbols showing water , ships , hits and misses
    does not show enemy ships unless debug mode is True"""
    debug_mode = True

    print_col_letters()

    for row in range(0, grid_size):
        print_row_numbers(row)
        for col in range(0, grid_size):
            tar = target(row, col)
            if user[tar] == "#":
                if debug_mode or user == grid:
                    print("#", end=" ")
                else:
                    print(".", end=" ")
            else:
                print(user[tar], end=" ")
        print_row_numbers(row)
        print(" ")

    print_col_letters()


# chooses a position  to place ship
def score(shot, hit, tar):
    """keeps and prints score"""
    global shots
    global hits

    shots += shot
    hits += hit

    word = "shot"
    if shots > 1:
        word = "shots"
    print(LINE)
    if hit:
        print(f"Weldone you've hit an ememy ship on {tar}")
    else:
        print(f"Too bad no enemy ship on {tar}")
    print(f"After {shots} {word} you have {user_ships} left floating")
    print(f"Your enemy has {comp_ships} left for you to sink.")
    print(LINE)


# checks ship placement is avalible
def validate_place_ship(tar, user):
    """checks if ship placement is valid for user or comp"""
    valid = True
    if user[tar] != ".":
        valid = False
    elif user[tar] == ".":
        user.update({tar: "#"})
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
            print(f"Weldone {player_name} you sunk all the enemy ships")
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


def new_game():
    """prpares a new game with same player name"""
    change_grid_size()
    set_board()
    create_grid(grid)
    create_grid(grid_c)
    print(f"Ok {player_name} let's play")


def display():
    """displays the grids at the begining of each turn"""
    print_grid(grid)
    print("^^Enemy Grid^^")
    print("Your Grid below")
    print_grid(grid_c)


def play_game():
    """Runs the game using known username"""
    new_game()

    while not game_over:
        display()
        hit_miss(grid_c)
        hit_miss(grid)
        finish_game()
    again = input("Press anykey to play again or N to end\n")
    again = again.upper()
    if again == "N":
        print(f"Goodbye {player_name}, it was fun playing")
    else:
        play_game()


player_name = input("what is your name?\n")
play_game()
