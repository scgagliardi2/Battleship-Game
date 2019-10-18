class Player:
    
    def __init__(self, ships_left):
        self.ships_left = 5

    def guess(self, coordinate, board):
        pass
    
    def check_input(self, string):
        letter_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
        number_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"] 
        for letter in letter_list:
            for number in number_list:
               coordinate = letter + number
               if coordinate == string.upper():
                   return True     
        print("Please enter a valid coordinate. For example, 'A4' or 'H8'")
        return False

    def check_direction(self, direction):
        direction = direction.lower()
        direction_list = ["right", "left", "down", "up"]
        for item in direction_list:
            if direction == item:
                return True
            else:
                pass
        print("Please enter a valid direction: right, left, up, or down.")
        return False
        pass