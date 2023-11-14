import random
class dice:
    def __init__(self, firstFace, secondFace, thirdFace, fourthFace, fifthFace, sixthFace):
        self.faces = [firstFace, secondFace, thirdFace, fourthFace, fifthFace, sixthFace]
        self.shownFace = None
        self.setRandomFace()

    def setRandomFace(self):
        index = random.randint(0, 5)
        self.shownFace = self.faces[index]
    
    def getShownFace(self):
        return self.shownFace
