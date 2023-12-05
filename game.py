class Game:
    def __init__(self, turn):
        self.turn = turn  # if 1 -> player1 else -> player2 comes first in this round
        self.phase = None

        if turn == 1:
            self.phase = (1, 1)
        else:
            self.phase = (2, 1)
        
        self.player1dic = dict()
        self.player2dic = dict()

        self.allDiceFaceName = ["axe", "arrow", "helmet", "shield", "hand", "goldenArrow", "goldenHelmet", "goldenShield", "goldenHand"]
    
    def update(self):  # to change between phases
        (x, y) = self.phase # person x throw his y's dice
        if y <= 3: # if is throwing phase
            if self.turn == x:
                self.phase = (3 - x, y)
            else:
                self.phase = (3 - x, y + 1)
        else: # after resolution phase
            self.turn = 3 - x
            self.phase = (3 - x, 1)

    def initAnalyze(self, player1, player2):
        for i in self.allDiceFaceName:
            self.player1dic[i] = 0
            self.player2dic[i] = 0
        
        for dice in player1.choosenDices:
            if "golden" in dice.shownFace.name:
                player1.money += 1
            self.player1dic[dice.shownFace.name] += 1
        for dice in player2.choosenDices:
            if "golden" in dice.shownFace.name:
                player2.money += 1
            self.player2dic[dice.shownFace.name] += 1
        

    def golden(self, string):
        x = string[0].upper()
        return "golden" + x + string[1:]
    
    def fightWithDice(self, attacker, defender, weapon, defence):
        attackerDic = (self.player1dic if attacker.number == 1 else self.player2dic)
        defenderDic = (self.player2dic if defender.number == 2 else self.player1dic)
        if attackerDic[weapon] > 0:
            attackerDic[weapon] -= 1
            attacker.removeChoosenDiceByName(weapon)
            if defenderDic[defence] > 0:
                defenderDic[defence] -= 1
                defender.removeChoosenDiceByName(defence)
            elif defenderDic[self.golden(defence)]:
                defenderDic[self.golden(defence)] -= 1
                defender.removeChoosenDiceByName(self.golden(defence))
            else:
                defender.removeHeart(1)
            return True
        return False
    
    def takeMoney(self, stealer, stealee):
        stealerDic = (self.player1dic if stealer.number == 1 else self.player2dic)
        if stealerDic["hand"] > 0:
            stealerDic["hand"] -= 1
            stealer.removeChoosenDiceByName("hand")
            stealee.removeMoney(1)
            stealer.money += 1
            return True
        elif stealerDic["goldenHand"] > 0:
            stealerDic["goldenHand"] -= 1
            stealer.removeChoosenDiceByName("goldenHand")
            stealee.removeMoney(1)
            stealer.money += 1
            return True
        return False
    
    def removeUselessDice(self, player, dice):
        playerDic = (self.player1dic if player.number == 1 else self.player2dic)
        if playerDic[dice] > 0:
            playerDic[dice] -= 1
            player.removeChoosenDiceByName(dice)
            return True
        return False



