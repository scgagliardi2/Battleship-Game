import Player
import Board
import Ship

#create players
hp = Player.Player("human") #human player
cp = Player.Player("computer") #computer player

#print intial board
print("Welcome to Battleship, here is your board!")
hp.personal_board.print_board()
print()

# generate human ships
# place carrier
while True:
    carrier_coor = hp.give_coordinate(hp.carrier) #get start coordinate
    hp.carrier.ship_start(carrier_coor) #update start coordinate
    carrier_direc = hp.give_direction() #get ship direction
    hp.carrier.ship_direction(carrier_direc) #update ship direction
    if hp.personal_board.place_ship(hp.carrier) == True:
        hp.personal_board.print_board()
        break
    else:
        pass
# place battleship
while True:
    battleship_coor = hp.give_coordinate(hp.battleship) #get start coordinate
    hp.battleship.ship_start(battleship_coor) #update start coordinate
    battleship_direc = hp.give_direction() #get ship direction
    hp.battleship.ship_direction(battleship_direc) #update ship direction
    if hp.personal_board.place_ship(hp.battleship) == True:
        hp.personal_board.print_board()
        break
    else:
        pass
# place cruiser
while True:
    cruiser_coor = hp.give_coordinate(hp.cruiser) #get start coordinate
    hp.cruiser.ship_start(cruiser_coor) #update start coordinate
    cruiser_direc = hp.give_direction() #get ship direction
    hp.cruiser.ship_direction(cruiser_direc) #update ship direction
    if hp.personal_board.place_ship(hp.cruiser) == True:
        hp.personal_board.print_board()
        break
    else:
        pass
# place submarine
while True:
    submarine_coor = hp.give_coordinate(hp.submarine) #get start coordinate
    hp.submarine.ship_start(submarine_coor) #update start coordinate
    submarine_direc = hp.give_direction() #get ship direction
    hp.submarine.ship_direction(submarine_direc) #update ship direction
    if hp.personal_board.place_ship(hp.submarine) == True:
        hp.personal_board.print_board()
        break
    else:
        pass
# place destroyer
while True:
    destroyer_coor = hp.give_coordinate(hp.destroyer) #get start coordinate
    hp.destroyer.ship_start(destroyer_coor) #update start coordinate
    destroyer_direc = hp.give_direction() #get ship direction
    hp.destroyer.ship_direction(destroyer_direc) #update ship direction
    if hp.personal_board.place_ship(hp.destroyer) == True:
        hp.personal_board.print_board()
        break
    else:
        pass

# generate computer ships
# place carrier
while True:
    carrier_coor = cp.comp_coor() #get start coordinate
    cp.carrier.ship_start(carrier_coor) #update start coordinate
    carrier_direc = cp.comp_direc() #get ship direction
    cp.carrier.ship_direction(carrier_direc) #update ship direction
    if cp.personal_board.place_comp_ship(cp.carrier) == True:
        break
    else:
        pass
# place battleship
while True:
    battleship_coor = cp.comp_coor() #get start coordinate
    cp.battleship.ship_start(battleship_coor) #update start coordinate
    battleship_direc = cp.comp_direc() #get ship direction
    cp.battleship.ship_direction(battleship_direc) #update ship direction
    if cp.personal_board.place_comp_ship(cp.battleship) == True:
        break
    else:
        pass
# place cruiser
while True:
    cruiser_coor = cp.comp_coor() #get start coordinate
    cp.cruiser.ship_start(cruiser_coor) #update start coordinate
    cruiser_direc = cp.comp_direc() #get ship direction
    cp.cruiser.ship_direction(cruiser_direc) #update ship direction
    if cp.personal_board.place_comp_ship(cp.cruiser) == True:
        break
    else:
        pass
# place submarine
while True:
    submarine_coor = cp.comp_coor() #get start coordinate
    cp.submarine.ship_start(submarine_coor) #update start coordinate
    submarine_direc = cp.comp_direc() #get ship direction
    cp.submarine.ship_direction(submarine_direc) #update ship direction
    if cp.personal_board.place_comp_ship(cp.submarine) == True:
        break
    else:
        pass
# place destroyer
while True:
    destroyer_coor = cp.comp_coor() #get start coordinate
    cp.destroyer.ship_start(destroyer_coor) #update start coordinate
    destroyer_direc = cp.comp_direc() #get ship direction
    cp.destroyer.ship_direction(destroyer_direc) #update ship direction
    if cp.personal_board.place_comp_ship(cp.destroyer) == True:
        break
    else:
        pass

# #setup complete

while True:

#human guess
    while True:
        guess = hp.guess()
        if cp.personal_board.check_guess(guess, hp.guess_board, cp):
            hp.guess_board.print_board()
            break
        else:
            pass
#computer guess:
    while True:
        guess = cp.comp_guess()
        if hp.personal_board.check_guess(guess, cp.guess_board, hp):
            break
        else:
            pass
    