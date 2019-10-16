class Board:

    def __init__(self):
        self.board = [["  ", "A", "B", "C", "D", "F", "G", "H", "I", "J", "K"],
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

    def place_ship(self, ship, start, finish):
