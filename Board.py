import Ship

class Board:

    def __init__(self):
        self.board = [["  ", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J"],
                      [" 1", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o"],
                      [" 2", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o"],
                      [" 3", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o"],
                      [" 4", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o"],
                      [" 5", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o"],
                      [" 6", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o"],
                      [" 7", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o"],
                      [" 8", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o"],
                      [" 9", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o"],
                      ["10", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o"]]

    def find_column(self, letter):
        column_dictionary = {"A": 1, "B": 2, "C": 3, "D": 4,
                             "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10}
        return column_dictionary.get(letter)

    def find_row(self, number):
        column_dictionary = {"1": 1, "2": 2, "3": 3, "4": 4,
                             "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10}
        return column_dictionary.get(number)

    def check_guess(self, coordinate, board_in):
        column = self.find_column(coordinate[0])
        row = self.find_row(coordinate[1])
         # check for row 10 input
        try:
            if coordinate[2] == "0":
                row = 11
            else:
                pass
        except IndexError:
            pass
        if self.board[row][column] == "o":
            print("You missed!")
            board_in.board[row][column] = "M"
            return True
        elif self.board[row][column] == "<":
            print("Hit!")
            board_in.board[row][column] = "H"
            return True
        else:
            print("You already guessed there!")
            return False

    def place_ship(self, ship):
        coordinates = Ship.Ship.ship_coordinates(ship)        
        try:
            for item in coordinates:
                if self.board[item[0]-1][item[1]-1] != "o":
                    print("You cannot place your ship there. Please pick a new location.")
                    return False
                else:
                    pass
        except IndexError:
            print("You cannot place your ship there. Please pick a new location.")
            return False
        for item in coordinates:
            self.board[item[0]-1][item[1]-1] = "<"
        return True           

    def place_comp_ship(self, ship):
        coordinates = Ship.Ship.ship_coordinates(ship)        
        try:
            for item in coordinates:
                if self.board[item[0]-1][item[1]-1] != "o":
                    return False
                else:
                    pass
        except IndexError:
            return False
        for item in coordinates:
            self.board[item[0]-1][item[1]-1] = "<"
        return True

    def print_board(self):
        for row in self.board:
            print()
            for item in row:
                print(item, end=" ")
        print()
