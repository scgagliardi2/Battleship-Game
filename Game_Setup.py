import Player
import Board
import Ship

# initial players and boards
human_player = Player.Player(5)
computer_player = Player.Player(5)
human_personal_board = Board.Board()
human_guess_board = Board.Board()
computer_personal_board = Board.Board()
computer_guess_board = Board.Board()

# print("Welcome to Battleship, here is your board!")

# human_personal_board.print_board()

# generate human ships
# place carrier
while True:
    while True:
        carrier_coordinate = input("Where do you want to start your carrier? ")
        print()
        if human_player.check_input(carrier_coordinate):
            carrier_coordinate = carrier_coordinate.upper()
            break
    while True:
        carrier_direction = input(
            "What direction is it facing? Up, down, left, or right? ")
        print()
        if human_player.check_direction(carrier_direction):
            carrier_direction = carrier_direction.casefold()
            break
    human_carrier = Ship.Ship(
        5, "carrier", carrier_coordinate, carrier_direction)
    if human_personal_board.place_ship(human_carrier) == True:
        break
    else:
        pass
human_personal_board.print_board()

#place battleship
while True:
    while True:
        battleship_coordinate = input(
            "Where do you want to start your battleship? ")
        print()
        if human_player.check_input(battleship_coordinate):
            battleship_coordinate = battleship_coordinate.upper()
            break
    while True:
        battleship_direction = input(
            "What direction is it facing? Up, down, left, or right? ")
        print()
        if human_player.check_direction(battleship_direction):
            battleship_direction = battleship_direction.casefold()
            break
    human_battleship = Ship.Ship(
        4, "battleship", battleship_coordinate, battleship_direction)
    if human_personal_board.place_ship(human_battleship) == True:
        break
    else:
        pass
human_personal_board.print_board()

#place submarine
while True:
    while True:
        submarine_coordinate = input(
            "Where do you want to start your submarine? ")
        print()
        if human_player.check_input(submarine_coordinate):
            submarine_coordinate = submarine_coordinate.upper()
            break
    while True:
        submarine_direction = input(
            "What direction is it facing? Up, down, left, or right? ")
        print()
        if human_player.check_direction(submarine_direction):
            submarine_direction = submarine_direction.casefold()
            break
    human_submarine = Ship.Ship(
        3, "submarine", submarine_coordinate, submarine_direction)
    if human_personal_board.place_ship(human_submarine) == True:
        break
    else:
        pass
human_personal_board.print_board()

#place cruiser
while True:
    while True:
        cruiser_coordinate = input("Where do you want to start your cruiser? ")
        print()
        if human_player.check_input(cruiser_coordinate):
            cruiser_coordinate = cruiser_coordinate.upper()
            break
    while True:
        cruiser_direction = input(
            "What direction is it facing? Up, down, left, or right? ")
        print()
        if human_player.check_direction(cruiser_direction):
            cruiser_direction = cruiser_direction.casefold()
            break
    human_cruiser = Ship.Ship(
        3, "cruiser", cruiser_coordinate, cruiser_direction)
    if human_personal_board.place_ship(human_cruiser) == True:
        break
    else:
        pass
human_personal_board.print_board()

#place destroyer
while True:
    while True:
        destroyer_coordinate = input(
            "Where do you want to start your destroyer? ")
        print()
        if human_player.check_input(destroyer_coordinate):
            destroyer_coordinate = destroyer_coordinate.upper()
            break
    while True:
        destroyer_direction = input(
            "What direction is it facing? Up, down, left, or right? ")
        print()
        if human_player.check_direction(destroyer_direction):
            destroyer_direction = destroyer_direction.casefold()
            break
    human_destroyer = Ship.Ship(
        2, "destroyer", destroyer_coordinate, destroyer_direction)
    if human_personal_board.place_ship(human_destroyer) == True:
        break
    else:
        pass
human_personal_board.print_board()

# generate computer ships
def computer_coordinates():
        import random
        column_dictionary = {1: "A", 2: "B", 3: "C", 4: "D",
                             5: "E", 6: "F", 7: "G", 8: "H", 9: "I", 10: "J"}
        column = column_dictionary.get(random.randint(1,10))
        row = str(random.randint(1,10))
        return column + row
        
def computer_direction():
    import random
    direction_dictionary = {1: "right", 2: "left", 3: "up", 4: "down"}
    direction = direction_dictionary.get(random.randint(1,4))
    return direction

#place carrier
while True:
    carrier_start = computer_coordinates()
    carrier_direction = computer_direction()
    computer_carrier = Ship.Ship(5, "carrier", carrier_start, carrier_direction)
    if computer_personal_board.place_comp_ship(computer_carrier) == True:
        break
    else:
        pass

#place battleship
while True:
    battleship_start = computer_coordinates()
    battleship_direction = computer_direction()
    computer_battleship = Ship.Ship(4, "battleship", battleship_start, battleship_direction)
    if computer_personal_board.place_comp_ship(computer_battleship) == True:
        break
    else:
        pass

#place submarine
while True:
    submarine_start = computer_coordinates()
    submarine_direction = computer_direction()
    computer_submarine = Ship.Ship(3, "submarine", submarine_start, submarine_direction)
    if computer_personal_board.place_comp_ship(computer_submarine) == True:
        break
    else:
        pass

#place cruiser
while True:
    cruiser_start = computer_coordinates()
    cruiser_direction = computer_direction()
    computer_cruiser = Ship.Ship(3, "cruiser", cruiser_start, cruiser_direction)
    if computer_personal_board.place_comp_ship(computer_cruiser) == True:
        break
    else:
        pass

#place destroyer
while True:
    destroyer_start = computer_coordinates()
    destroyer_direction = computer_direction()
    computer_destroyer = Ship.Ship(2, "destroyer", destroyer_start, destroyer_direction)
    if computer_personal_board.place_comp_ship(computer_destroyer) == True:
        break
    else:
        pass

