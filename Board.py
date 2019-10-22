import Ship
import Player

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

    def check_guess(self, coordinate, guess_board, player):
        column = self.find_column(coordinate[0])
        row = self.find_row(coordinate[1])
         # check for row 10 input
        try:
            if coordinate[2] == "0":
                row = 10
            else:
                pass
        except IndexError:
            pass
        if self.board[row][column] == "o":
            if player.player_type == "computer":
                print("You missed!")
                guess_board.board[row][column] = "m"
                self.board[row][column] = "m"
            else:
                print("The enemy missed!")
                player.personal_board.board[row][column] = "m"
            return True
        elif self.board[row][column] == "<":
            if player.player_type == "computer":
                print("Hit!")
            else:
                print("The enemy hit your destroyer!")
            guess_board.board[row][column] = "H"
            self.board[row][column] = "H"
            player.ship_hit(player.destroyer)
            if player.player_type == "human":
                player.personal_board.board[row][column] = "H"
            return True
        elif self.board[row][column] == "(":
            if player.player_type == "computer":
                print("Hit!")
            else:
                print("The enemy hit your cruiser!")
            guess_board.board[row][column] = "H"
            self.board[row][column] = "H"
            player.ship_hit(player.cruiser)
            if player.player_type == "human":
                player.personal_board.board[row][column] = "H"
            return True
        elif self.board[row][column] == "=":
            if player.player_type == "computer":
                print("Hit!")
            else:
                print("The enemy hit your submarine!")
            guess_board.board[row][column] = "H"
            self.board[row][column] = "H"
            player.ship_hit(player.submarine)
            if player.player_type == "human":
                player.personal_board.board[row][column] = "H"
            return True
        elif self.board[row][column] == "{":
            if player.player_type == "computer":
                print("Hit!")
            else:
                print("The enemy hit your battleship!")
            guess_board.board[row][column] = "H"
            self.board[row][column] = "H"
            player.ship_hit(player.battleship)
            if player.player_type == "human":
                player.personal_board.board[row][column] = "H"
            return True
        elif self.board[row][column] == "[":
            if player.player_type == "computer":
                print("Hit!")
            else:
                print("The enemy hit your carrier!")
            guess_board.board[row][column] = "H"
            self.board[row][column] = "H"
            player.ship_hit(player.carrier)
            if player.player_type == "human":
                player.personal_board.board[row][column] = "H"
            return True
        else:
            if player.player_type == "computer":
                print("You already guessed there!")
                return False
            else:
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
            if ship.name == "carrier":
                self.board[item[0]-1][item[1]-1] = "["
            elif ship.name == "battleship":
                self.board[item[0]-1][item[1]-1] = "{"
            elif ship.name == "cruiser":
                self.board[item[0]-1][item[1]-1] = "("
            elif ship.name == "submarine":
                self.board[item[0]-1][item[1]-1] = "="
            elif ship.name == "destroyer":
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
            if ship.name == "carrier":
                self.board[item[0]-1][item[1]-1] = "["
            elif ship.name == "battleship":
                self.board[item[0]-1][item[1]-1] = "{"
            elif ship.name == "cruiser":
                self.board[item[0]-1][item[1]-1] = "("
            elif ship.name == "submarine":
                self.board[item[0]-1][item[1]-1] = "="
            elif ship.name == "destroyer":
                self.board[item[0]-1][item[1]-1] = "<"
        return True

    def print_board(self):
        for row in self.board:
            print()
            for item in row:
                print(item, end=" ")
        print("")
