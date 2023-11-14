class Game:
    def __init__(self, turn):
        self.turn = turn  # if 1 -> player1 else -> player2 comes first in this round
        self.phase = None
        if turn == 1:
            self.phase = (1, 1)
        else:
            self.phase = (2, 1)
    def update(self):  # to change between phases
        (x, y) = self.phase
        if y <= 3: # if is throwing phase
            if self.turn == x:
                self.phase = (3 - x, y)
            else:
                self.phase = (3 - x, y + 1)
        else: # if last throwing or next round
            if self.turn == x:
                self.phase = (3 - x, y)
            else:
                # next round
                turn = 3 - x
                self.phase = (3 - x, 1)


