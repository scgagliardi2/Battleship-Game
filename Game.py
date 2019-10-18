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
carrier_coordinate = input("Where do you want to start your carrier? ")
carrier_direction = input(
    "What direction is it facing? Up, down, left, or right? ")
human_carrier = Ship.Ship(5, "carrier", carrier_coordinate, carrier_direction)
human_personal_board.place_ship(human_carrier)

human_personal_board.print_board()
