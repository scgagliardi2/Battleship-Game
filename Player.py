class New_Player:

    def __init__(self, player):
        pass


player = New_Player("one")

player.place_ships()

for row in player.board:
    print()
    for item in row:
        print(item, end=" ")
