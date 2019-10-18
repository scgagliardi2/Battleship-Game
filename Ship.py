class Ship:

    def __init__(self, hits, ship_type, start, direction):
        self.hits = hits
        self.ship_type = ship_type
        self.start = start
        self.direction = direction

    def ship_hit(self):
        self.hits -= 1
        if self.hits == 0:
            print("You sunk the enemy " + self.ship_type + "!")

    def ship_coordinates(self):
        column_dictionary = {"A": 2, "B": 3, "C": 4, "D": 5,
                             "E": 6, "F": 7, "G": 8, "H": 9, "I": 10, "J": 11}
        row_dictionary = {"1": 2, "2": 3, "3": 4, "4": 5,
                          "5": 6, "6": 7, "7": 8, "8": 9, "9": 10, "10": 11}
        if self.direction == "right":
            coordinates = []
            length = self.hits
            while length != 0:
                coordinates.append([row_dictionary.get(self.start[1]),
                                    column_dictionary.get(self.start[0]) + self.hits - length])
                length -= 1
            return coordinates
        elif self.direction == "left":
            coordinates = []
            length = self.hits
            while length != 0:
                coordinates.append([row_dictionary.get(self.start[1]),
                                    column_dictionary.get(self.start[0]) + length - self.hits])
                length -= 1
            return coordinates
        elif self.direction == "down":
            coordinates = []
            length = self.hits
            while length != 0:
                coordinates.append([row_dictionary.get(self.start[1]) + self.hits - length,
                                    column_dictionary.get(self.start[0])])
                length -= 1
            return coordinates
        elif self.direction == "up":
            coordinates = []
            length = self.hits
            while length != 0:
                coordinates.append([row_dictionary.get(self.start[1]) - self.hits + length,
                                    column_dictionary.get(self.start[0])])
                length -= 1
            return coordinates
