import Player
import Board
import Ship

#create players
hp = Player.Player() #human player
cp = Player.Player() #computer player

print("Welcome to Battleship, here is your board!")
hp.personal_board.print_board() #print intial board

# generate human ships
# place carrier
while True:
    carrier_coor = hp.give_coordinate(hp.carrier) #get start coordinate
    hp.carrier.ship_start(carrier_coor) #update start coordinate
    carrier_direc = hp.give_direction() #get ship direction
    hp.carrier.ship_direction(carrier_direc) #update ship direction
    if hp.personal_board.place_ship(hp.carrier) == True:
        break
    else:
        pass
hp.personal_board.print_board()

# # generate computer ships
# def computer_coordinates():
#         import random
#         column_dictionary = {1: "A", 2: "B", 3: "C", 4: "D",
#                              5: "E", 6: "F", 7: "G", 8: "H", 9: "I", 10: "J"}
#         column = column_dictionary.get(random.randint(1,10))
#         row = str(random.randint(1,10))
#         return column + row
        
# def computer_direction():
#     import random
#     direction_dictionary = {1: "right", 2: "left", 3: "up", 4: "down"}
#     direction = direction_dictionary.get(random.randint(1,4))
#     return direction

# #place carrier
# while True:
#     carrier_start = computer_coordinates()
#     carrier_direction = computer_direction()
#     computer_carrier = Ship.Ship(5, "carrier", carrier_start, carrier_direction)
#     if computer_personal_board.place_comp_ship(computer_carrier) == True:
#         break
#     else:
#         pass

# #place battleship
# while True:
#     battleship_start = computer_coordinates()
#     battleship_direction = computer_direction()
#     computer_battleship = Ship.Ship(4, "battleship", battleship_start, battleship_direction)
#     if computer_personal_board.place_comp_ship(computer_battleship) == True:
#         break
#     else:
#         pass

# #place submarine
# while True:
#     submarine_start = computer_coordinates()
#     submarine_direction = computer_direction()
#     computer_submarine = Ship.Ship(3, "submarine", submarine_start, submarine_direction)
#     if computer_personal_board.place_comp_ship(computer_submarine) == True:
#         break
#     else:
#         pass

# #place cruiser
# while True:
#     cruiser_start = computer_coordinates()
#     cruiser_direction = computer_direction()
#     computer_cruiser = Ship.Ship(3, "cruiser", cruiser_start, cruiser_direction)
#     if computer_personal_board.place_comp_ship(computer_cruiser) == True:
#         break
#     else:
#         pass

# #place destroyer
# while True:
#     destroyer_start = computer_coordinates()
#     destroyer_direction = computer_direction()
#     computer_destroyer = Ship.Ship(2, "destroyer", destroyer_start, destroyer_direction)
#     if computer_personal_board.place_comp_ship(computer_destroyer) == True:
#         break
#     else:
#         pass

# #setup complete

# while True:

#     #human guess
#     while True:
#         guess = input("Where would you like to guess? ")
#         if human_player.check_input(guess):
#             guess = guess.upper()
#             if computer_personal_board.check_guess(guess, human_guess_board):
#                 human_guess_board.print_board()
#                 break
#             else:
#                 pass
    