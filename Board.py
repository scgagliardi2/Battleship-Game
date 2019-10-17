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

    def check_guess(self, coordinate):
        column = self.find_column(coordinate[0])
        row = self.find_row(coordinate[1])
        if self.board[column][row] == "o":
            print("You missed!")
            self.board[column][row] = "M"
            return 1
        elif self.board[column][row] == "<":
            print("Hit!")
            self.board[column][row] = "H"
            return 1
        else:
            print("You already guessed there!")
            return 0

    def place_ship(self, ship):
        coordinates = Ship.Ship.ship_coordinates(ship)
        for item in coordinates:
            for place in item:
                self.board[item[0]-1][place-1] = "<"

    def print_board(self):
        for row in self.board:
            print()
            for item in row:
                print(item, end=" ")
        print()

b1 = Board()

b1.print_board()

s1 = Ship.Ship(5, "carrier", "A1", "A2")
b1.place_ship(s1)

b1.print_board()



