class player:
    def __init__(self, dices, firstHeartLocation, heartSize, firstEmptySlotLocation, firstDiceLocation, diceSize):
        self.health = 15
        self.copyDices = dices  # for resetting dices
        self.dices = dices
        self.heartLocations = []
        self.diceSize = diceSize
        self.choosenDices = [None, None, None, None, None, None]
        y = firstHeartLocation[1]
        #set heart locations
        for i in range(3):
            x = firstHeartLocation[0]
            for j in range(5):
                self.heartLocations.append((x, y))
                x += heartSize[0]
            y += heartSize[1]
        self.emptySlots = []
        #set slot locations
        for i in range(6):
            self.emptySlots.append((firstEmptySlotLocation[0] + (diceSize[0] + 10) * i, firstEmptySlotLocation[1]))
        
        self.diceLocations = []

        #set dice locations

        for i in range(6):
            self.diceLocations.append((firstDiceLocation[0] + (diceSize[0] + 5) * i, firstDiceLocation[1]))
    
    def rollDices(self):
        for i in range(len(self.dices)):
            if self.dices[i] != None:
                self.dices[i].setRandomFace()
    
    def chooseDice(self, i):
        self.dices[i] = None

    def resetDices(self):
        self.dices = self.copyDices

    def getClickedDice(self, x, y):
        clickedDice = -1
        for j in range(len(self.diceLocations)):
            i = self.diceLocations[j]
            if i[0] <= x <= i[0] + self.diceSize[0] and i[1] <= y <= i[1] + self.diceSize[1]:
                if self.dices[j] != None:
                    clickedDice = j
        return clickedDice
    
    def removeDice(self, i):
        dice = self.dices[i]
        self.dices[i] = None
        return dice

