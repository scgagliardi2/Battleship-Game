class Ship:
    
    def __init__(self, hits, ship_type, start, finish):
        self.hits = hits
        self.ship_type = ship_type
        self.start = start
        self.finish = finish
        

    def ship_hit(self):
        self.hits -= 1
        if self.hits == 0:
            print("You sunk the enemy " + ship_type + "!")
        