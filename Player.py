class Player:
    
    def __init__(self):
        import Ship
        import Board
        
        self.ships_left = 5
        self.carrier = Ship.Ship(5, "carrier", "A1", "A1")
        self.battleship = Ship.Ship(4, "battleship", "A1", "A1")
        self.cruiser = Ship.Ship(3, "cruiser", "A1", "A1")
        self.submarine = Ship.Ship(3, "submarine", "A1", "A1")
        self.destroyer = Ship.Ship(2, "destroyer", "A1", "A1")
        self.personal_board = Board.Board()
        self.guess_board = Board.Board()
        
    
    def give_coordinate(self, ship):
        while True:
            coordinate = input("Where do you want to start your " + ship.name + " ? " )
            print()
            letter_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
            number_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"] 
            for letter in letter_list:
                for number in number_list:
                    check = letter + number
                    if check == coordinate.upper():
                        return coordinate.upper()     
            print("Please enter a valid coordinate. For example, 'A4' or 'H8'")
            print()

    def give_direction(self):
        while True:
            direction = input("What direction is it faceing? ")
            print()
            direction_list = ["right", "left", "down", "up"]
            for item in direction_list:
                if direction == item:
                    return direction
                else:
                    pass
            print("Please enter a valid direction: right, left, up, or down.")
            print()