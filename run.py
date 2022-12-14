"""
    -------BATTLESHIPS-------
    How it will work:
    Takes user name and has them play battleships against a computer
    Prints the game board with symbols in legend
    Keeps score and informs player
    Tells player when they have won/lost
    Asks if they want to play again

    Legend:
    1. "." = water or empty space
    2. "#" = part of ship
    3. "X" = part of ship that was hit with bullet
    4. "O" = water that was shot with bullet, a miss because it hit no ship
"""
import random

# Constants
NUM = [x for x in range(1, 27)]
LET = [chr(x) for x in range(65, 91)]
board = {"ships": 5, "shots": 0, "hits": 0, "size": 0}
LINE = "--------------------------------"
BAD = ("", " ", "[", "]", ",")

# Global variables
game_over = False


class User:
    """users"""

    def __init__(self, board, ships):
        self.board = {}
        self.ships = 0

    def create_grid(self):
        """Creates grid and places ships on it"""
        grid_size = board["size"]

        for row in range(0, grid_size):
            for col in range(0, grid_size):
                tar = target(row, col)
                self.board.update({tar: "."})

        ships_placed = 0

        while ships_placed != board["ships"]:
            tar = random_tar()
            if User.validate_place_ship(self, tar):
                ships_placed += 1

    def validate_place_ship(self, tar):
        """Checks if ship can be placed at location"""
        valid = True
        if self.board[tar] != ".":
            valid = False
        else:
            self.board.update({tar: "#"})
        return valid

    def print_grid(self):
        """prints grid with symbols showing water, ships, hits and misses
        does not show enemy ships unless debug mode is True"""
        debug_mode = False
        grid_size = board["size"]

        print_col_letters(grid_size)

        for row in range(0, grid_size):
            print_row_number(row)
            for col in range(0, grid_size):
                tar = target(row, col)
                if self.board[tar] == "#":
                    if debug_mode or self == player:
                        print("#", end=" ")
                    else:
                        print(".", end=" ")
                else:
                    print(self.board[tar], end=" ")
            print_row_number(row)
            print(" ")

        print_col_letters(grid_size)

    def hit_miss(self):
        """checks if shot hit or miss. updates board and player"""
        # User shoots, defender variable used to update data
        # Possiblity to add more players using defender variable
        if self == comp:
            defender = player.board
            tar = random_tar()
        else:
            defender = comp.board
            tar = accept_shot_validate(defender)

        if defender[tar] == "#":
            info = "X"
            defender.update({tar: info})
            if self == player:
                comp.ships -= 1
                score(1, 1, tar)
            else:
                player.ships -= 1
        else:
            info = "O"
            defender.update({tar: info})
            if self == player:
                score(1, 0, tar)


def change_grid_size():
    """lets the player change the grid size and choose number of ships"""

    size = input("Choose a Grid size from 2-7 to play on\n")
    while size in BAD or size not in str(NUM[1:7]):
        print(f"'{size}' is invalid")
        size = input("Choose a Grid size from 2-7 to play on\n")

    board["size"] = int(size)
    max_ships = min(int(size)**2 - 1, 26)

    ships = input(f"Choose number of ships from 1-{max_ships}\n")
    while ships in BAD or ships not in str(NUM[0: max_ships]):
        if int(ships) > max_ships:
            ships = input(f"Thats too many ships choose from 1-{max_ships}\n")
            continue
        print(f"'{ships}' is invalid")
        ships = input(f"Choose number of ships from 1-{max_ships}\n")

    ships = int(ships)
    board["ships"], comp.ships, player.ships = ships, ships, ships


# These next three defs make code much more readable, dont try not using them
def print_col_letters(grid_size):
    """prints out the column letters. Used at top & bottom of grid"""
    print(" ", end=" ")
    for row in range(0, grid_size):
        print(LET[row], end=" ")
    print("")


def print_row_number(row):
    """prints out row number for the side of the grid"""
    print(f"{NUM[row]}", end=" ")


def target(row, col):
    """takes row and column and returns dictionary key. makes
    future code smaller"""
    return f"{NUM[row]}{LET[col]}"


def random_tar():
    """Selects target for ship placement or comp shot"""
    grid_size = board["size"]
    row = random.randint(0, grid_size - 1)
    col = random.randint(0, grid_size - 1)
    tar = target(row, col)
    return tar


def accept_shot_validate(defender):
    """Take user input and check if valid"""
    valid_shot = False
    grid_size = board["size"]

    # Choices and range to keep code short & readable
    row_choices = f"Choose a row between {NUM[0]}-{NUM[grid_size - 1]}\n"
    col_choices = f"Choose a column between {LET[0]}-{LET[grid_size - 1]}\n"
    row_range = str(NUM[0:grid_size])

    while not valid_shot:
        row = input(row_choices)
        while row in BAD or row not in row_range:
            print(f"'{row}' is invalid")
            row = input(row_choices)

        col = input(col_choices)
        col = col.upper()
        while col not in LET[0:grid_size]:
            print(f"'{col}'is invalid")
            col = input(col_choices)
            col = col.upper()

        row = int(row) - 1
        col = ord(col) - 65
        tar = target(row, col)

        if defender[tar] == "X" or defender[tar] == "O":
            print(f"You have already shot '{tar}'")
            continue

        valid_shot = True
    return tar


def score(shot, hit, tar):
    """updates and prints score"""
    board["shots"] += shot
    board["hits"] += hit
    shots = board["shots"]

    word = "shot"
    if board["shots"] > 1:
        word = "shots"

    if hit:
        print(
            f"{LINE}"
            f"\nWeldone you've hit an enemy ship on {tar}"
             )
    else:
        print(
            f"{LINE}"
            f"\nToo bad no enemy ship on {tar}"
             )
    print(
        f"After {shots} {word} you have {player.ships} left floating"
        f"\nYour enemy has {comp.ships} left for you to sink."
        f"\n{LINE}"
         )


def finish_game():
    """Checks if game is over and if user wants to continue"""
    global game_over
    game_over = False
    ships = board["ships"]

    if comp.ships == 0 or player.ships == 0:
        game_over = True

        if comp.ships == 0:
            print(
                f"{LINE}"
                f"\nWeldone {player_name} you sunk all the enemy ships"
                 )
        else:
            print(
                f"{LINE}"
                f"\nToo bad {player_name} they sunk all your ships"
                 )
        print(
            f"you had {player.ships} ships left floating of {ships}"
            f"\nYour enemy had {comp.ships} left floating of {ships}"
            f"\n{LINE}"
            )

    else:
        end_game = input("Press anykey to continue or N to quit game\n")
        end_game = end_game.upper()
        if end_game == "N":
            game_over = True

            print(
                f"{LINE}"
                f"\nyou had {player.ships} ships left floating of {ships}"
                f"\nYour enemy had {comp.ships} left floating of {ships}"
                f"\n{LINE}"
                 )


def new_game():
    """prpares a new game with same player name"""
    change_grid_size()
    set_board()
    player.create_grid()
    comp.create_grid()
    print(f"Ok {player_name} let's play")


def set_board():
    """Sets global varibles needed for game to 0"""
    board["shots"] = 0
    board["hits"] = 0

    global game_over
    game_over = False

    player.board.clear()
    comp.board.clear()


def display():
    """prints both grids with labels"""
    comp.print_grid()
    print("^^Enemy Grid^^\nYour Grid below")
    player.print_grid()


def how_to_play():
    """Tells player how to play, what symbols mean, what they'll be asked
    and asks if they are ready"""
    print(
        f"Welcome {player_name} to this Awesome Battleships Game"
        f"\n{LINE}"
        "\nYou and you opponent each have ships on a square grid"
        "\nSelect a square where you think a ship is on the enemy grid"
        "\nEnter the row number then column letter to select & fire"
        "\nFirst to hit & sink all the opponents ships wins"
        f"\n{LINE}"
        "\n    Legend"
        "\n1. '.' = water or empty space"
        "\n2. '#' = A ship\n3. 'X' = A ship that was hit with bullet"
        "\n4. 'O' = water you have already shot at"
        f"\n{LINE}"
        f"\nAre you ready to play {player_name}"
         )
    keep_going = input("Press anykey to continue\n")
    if keep_going:
        pass


def play_game():
    """Runs the game using known username"""
    new_game()

    while not game_over:
        display()
        comp.hit_miss()
        player.hit_miss()
        finish_game()
    again = input("Press anykey to play again or N to end\n")
    again = again.upper()
    if again == "N":
        print(f"Goodbye {player_name}, it was fun playing")
    else:
        play_game()


comp = User("grid_c", 5)
player = User("grid_u", 5)

player_name = input("what is your name?\n")
how_to_play()
play_game()
