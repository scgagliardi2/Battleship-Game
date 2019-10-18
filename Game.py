import Player
import Board
import Ship
import random

# initial players and boards
human_player = Player.Player(5)
computer_player = Player.Player(5)
human_personal_board = Board.Board()
human_guess_board = Board.Board()
computer_personal_board = Board.Board()
computer_guess_board = Board.Board()

print("Welcome to Battleship, here is your board!")

human_personal_board.print_board()

# generate human ships
while True:
    carrier_coordinate = input("Where do you want to start your carrier? ")
    if human_player.check_input(carrier_coordinate):
        carrier_coordinate = carrier_coordinate.upper()
        break
while True:
    carrier_direction = input(
    "What direction is it facing? Up, down, left, or right? ")
    if human_player.check_direction(carrier_direction):
        carrier_direction = carrier_direction.casefold()
        break
human_carrier = Ship.Ship(5, "carrier", carrier_coordinate, carrier_direction)
human_personal_board.place_ship(human_carrier)

# Carrier (5), Battleship (4), Cruiser (3), Submarine (3), and Destroyer (2).
human_personal_board.print_board()
