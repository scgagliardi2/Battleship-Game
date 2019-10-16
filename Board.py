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
        column_dictionary = {"A": 2, "B": 3, "C": 4, "D": 5, "E": 6, "F": 7, "G": 8, "H": 9, "I": 10, "J": 11}
        return column_dictionary.get(letter)

    def find_row(self, number):
        column_dictionary = {"1": 2, "2": 3, "3": 4, "4": 5, "5": 6, "6": 7, "7": 8, "8": 9, "9": 10, "10": 11}
        return column_dictionary.get(number)

    def guess(self, guess):
        column = guess.index(0)
        row = guess.index(1)
        if self.board[column][row] == "o":
            print("Youmissed!")
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
        #l1 = self.find_column(start[0])-1
        #n1 = self.find_row(start[1])-1
        #l2 = self.find_column(finish[0])-1
        #n2 = self.find_row(finish[1])-1
        
        #self.board[l1][l2] = "<"
        #self.board[n1][n2] = "<"
        pass
                
b1 = Board()

for row in b1.board:
    print()
    for item in row:
        print(item, end=" ")

import Battleship.Ship
s1 = Battleship.Ship(5, "carrier", "A1", "A4")
b1.place_ship(s1)

for row in b1.board:
    print()
    for item in row:
        print(item, end=" ")
