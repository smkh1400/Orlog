import random
class dice:
    def __init__(self, firstFace, secondFace, thirdFace, fourthFace, fifthFace, sixthFace):
        self.faces = [firstFace, secondFace, thirdFace, fourthFace, fifthFace, sixthFace]

    def getRandomFace(self):
        index = random.randint(0, 5)
        return self.faces[index]
