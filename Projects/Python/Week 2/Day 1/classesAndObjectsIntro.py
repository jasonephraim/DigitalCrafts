class Table:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.legs = ""
        self.color = ""
        self.material = ""

diningRoomTable = Table('26"', '24"')
diningRoomTable.legs = "4"
diningRoomTable.color = "black"

print(diningRoomTable.legs)