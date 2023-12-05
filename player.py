class player:
    def __init__(self, number, dices, firstHeartLocation, heartSize, firstEmptySlotLocation, firstDiceLocation, diceSize):
        self.number = number
        self.money = 0
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
        
        #set slot locations
        self.emptySlots = []
        for i in range(6):
            self.emptySlots.append((firstEmptySlotLocation[0] + (diceSize[0] + 10) * i, firstEmptySlotLocation[1]))
        

        #set dice locations
        self.diceLocations = []
        for i in range(6):
            self.diceLocations.append((firstDiceLocation[0] + (diceSize[0] + 5) * i, firstDiceLocation[1]))
    
    def rollDices(self):
        for i in range(len(self.dices)):
            if self.dices[i] != None:
                self.dices[i].setRandomFace()

    def getClickedDice(self, x, y):
        clickedDice = -1
        for j in range(len(self.diceLocations)):
            i = self.diceLocations[j]
            if i[0] <= x <= i[0] + self.diceSize[0] and i[1] <= y <= i[1] + self.diceSize[1]:
                if self.dices[j] != None:
                    clickedDice = j
        return clickedDice
    
    def getClickedEmptySlot(self, x, y):
        clickedEmptySlot = -1
        for i in range(len(self.emptySlots)):
            e = self.emptySlots[i]
            if e[0] <= x <= e[0] + self.diceSize[0] and e[1] <= y <= e[1] + self.diceSize[1]:
                if self.choosenDices[i] != None:
                    clickedEmptySlot = i
        return clickedEmptySlot
    
    def moveDiceToSlot(self, i):
        dice = self.dices[i]
        self.choosenDices[i] = dice
        self.dices[i] = None
    
    def returnDiceFromSlot(self, i):
        dice = self.choosenDices[i]
        self.dices[i] = dice
        self.choosenDices[i] = None
    
    def removeChoosenDiceByName(self,name):
        for i in range(len(self.choosenDices)):
            dice = self.choosenDices[i]
            if dice is not None and dice.shownFace.name == name:
                self.dices[i] = self.choosenDices[i]
                self.choosenDices[i] = None
                break

    def removeHeart(self, t):
        self.health -= t

    def removeMoney(self, t):
        if self.money != 0:
            self.money -= t


