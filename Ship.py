class Ship:

    def __init__(self, hits, name, start, direction):
        self.hits = hits
        self.name = name
        self.start = start
        self.direction = direction

    def ship_start(self, coordinate):
        self.start = coordinate
    
    def ship_direction(self, direc):
        self.direction = direc
 
    def ship_hit(self):
        self.hits -= 1
        if self.hits == 0:
            print("You sunk the enemy " + self.name + "!")
            return True
        else:
            return False


    def ship_coordinates(self):
        column_dictionary = {"A": 2, "B": 3, "C": 4, "D": 5,
                             "E": 6, "F": 7, "G": 8, "H": 9, "I": 10, "J": 11}
        row_dictionary = {"1": 2, "2": 3, "3": 4, "4": 5,
                          "5": 6, "6": 7, "7": 8, "8": 9, "9": 10, "10": 11}
        column = column_dictionary.get(self.start[0])
        row = row_dictionary.get(self.start[1])
        # check for row 10 input
        try:
            if self.start[2] == "0":
                row = 11
            else:
                pass
        except IndexError:
            pass
        if self.direction == "right":
            coordinates = []
            length = self.hits
            while length != 0:
                coordinates.append([row,
                                    column + self.hits - length])
                length -= 1
            return coordinates
        elif self.direction == "left":
            coordinates = []
            length = self.hits
            while length != 0:
                coordinates.append([row,
                                    column + length - self.hits])
                length -= 1
            return coordinates
        elif self.direction == "down":
            coordinates = []
            length = self.hits
            while length != 0:
                coordinates.append([row + self.hits - length,
                                    column])
                length -= 1
            return coordinates
        elif self.direction == "up":
            coordinates = []
            length = self.hits
            while length != 0:
                coordinates.append([row - self.hits + length,
                                    column])
                length -= 1
            return coordinates