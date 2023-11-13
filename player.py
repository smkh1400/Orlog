class player:
    def __init__(self, dices, firstHeartLocation, heartSize, firstEmptySlotLocation, emptySlotSize):
        self.health = 15
        self.dices = dices
        self.heartLocations = []
        y = firstHeartLocation[1]
        for i in range(3):
            x = firstHeartLocation[0]
            for j in range(5):
                self.heartLocations.append((x, y))
                x += heartSize[0]
            y += heartSize[1]
        self.emptySlots = []
        for i in range(6):
            self.emptySlots.append((firstEmptySlotLocation[0] + (emptySlotSize[0] + 10) * i, firstEmptySlotLocation[1]))
