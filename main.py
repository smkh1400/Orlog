import pygame as pg
import Dice, player, game, button, diceFace
import random
import time

def main():

    pg.init()
    WINDOW_SIZE = [800, 800]
    screen = pg.display.set_mode(WINDOW_SIZE)

    pg.display.set_caption("Orlog")

    DEFAULT_DICE_FACE_SIZE = (50, 50)
    DEFAULT_HEART_SIZE = (30, 30)

    #dice faces
    arrowTexture = pg.transform.scale(pg.image.load("orlog pictures/arrow.png"), DEFAULT_DICE_FACE_SIZE)
    axeTexture = pg.transform.scale(pg.image.load("orlog pictures/axe.png"), DEFAULT_DICE_FACE_SIZE)
    handTexture = pg.transform.scale(pg.image.load("orlog pictures/hand.png"), DEFAULT_DICE_FACE_SIZE)
    helmetTexture = pg.transform.scale(pg.image.load("orlog pictures/helmet.png"), DEFAULT_DICE_FACE_SIZE)
    shieldTexture = pg.transform.scale(pg.image.load("orlog pictures/shield.png"), DEFAULT_DICE_FACE_SIZE)
    goldenArrowTexture = pg.transform.scale(pg.image.load("orlog pictures/goldenArrow.png"), DEFAULT_DICE_FACE_SIZE)
    goldenHandTexture = pg.transform.scale(pg.image.load("orlog pictures/goldenHand.png"), DEFAULT_DICE_FACE_SIZE)
    goldenHelmetTexture = pg.transform.scale(pg.image.load("orlog pictures/goldenHelmet.png"), DEFAULT_DICE_FACE_SIZE)
    goldenShieldTexture = pg.transform.scale(pg.image.load("orlog pictures/goldenShield.png"), DEFAULT_DICE_FACE_SIZE)

    axe = diceFace.diceFace(axeTexture, "axe")
    arrow = diceFace.diceFace(arrowTexture, "arrow")
    helmet = diceFace.diceFace(helmetTexture, "helmet")
    shield = diceFace.diceFace(shieldTexture, "shield")
    hand = diceFace.diceFace(handTexture, "hand")
    goldenArrow = diceFace.diceFace(goldenArrowTexture, "goldenArrow")
    goldenHelmet = diceFace.diceFace(goldenHelmetTexture, "goldenHelmet")
    goldenShield = diceFace.diceFace(goldenShieldTexture, "goldenShield")
    goldenHand = diceFace.diceFace(goldenHandTexture, "goldenHand")

    emptySlot = pg.transform.scale(pg.image.load("orlog pictures/slot.png"), DEFAULT_DICE_FACE_SIZE)

    heart = pg.transform.scale(pg.image.load("orlog pictures/heart.png"), DEFAULT_HEART_SIZE)

    #make dices
    diceType11 = Dice.dice(axe, shield, goldenArrow, axe, helmet, goldenHand)
    diceType12 = Dice.dice(axe, goldenShield, arrow, axe, goldenHand, helmet)
    diceType13 = Dice.dice(axe, goldenArrow, hand, axe, goldenHelmet, shield)
    diceType14 = Dice.dice(axe, shield, goldenHand, arrow, goldenHelmet, axe)
    diceType15 = Dice.dice(axe, goldenShield, hand, axe, helmet, goldenArrow)
    diceType16 = Dice.dice(axe, goldenShield, hand, axe, arrow, goldenHelmet)
    diceType21 = Dice.dice(axe, shield, goldenArrow, axe, helmet, goldenHand)
    diceType22 = Dice.dice(axe, goldenShield, arrow, axe, goldenHand, helmet)
    diceType23 = Dice.dice(axe, goldenArrow, hand, axe, goldenHelmet, shield)
    diceType24 = Dice.dice(axe, shield, goldenHand, arrow, goldenHelmet, axe)
    diceType25 = Dice.dice(axe, goldenShield, hand, axe, helmet, goldenArrow)
    diceType26 = Dice.dice(axe, goldenShield, hand, axe, arrow, goldenHelmet)

    diceList1 = [diceType11, diceType12, diceType13, diceType14, diceType15, diceType16]
    diceList2 = [diceType21, diceType22, diceType23, diceType24, diceType25, diceType26]

    player1 = player.player(1, diceList1, [70, 600], DEFAULT_HEART_SIZE, [280, 430], [350, 600], DEFAULT_DICE_FACE_SIZE)
    player2 = player.player(2, diceList2, [70, 110], DEFAULT_HEART_SIZE, [280, 320], [350, 150], DEFAULT_DICE_FACE_SIZE)

    player1RollButton = button.Button(460, 750, 100, 30, "black", "Roll", "white")
    player2RollButton = button.Button(460, 20, 100, 30, "black", "roll", "white")

    player1confirmButton = button.Button(700, 750, 100, 30, "black", "Confirm", "white")
    player2confirmButton = button.Button(700, 20, 100, 30, "black", "Confirm", "white")

    player1confirmButton.enable = False
    player2confirmButton.enable = False

    debugButton = button.Button(50, 360, 200, 30, "black", "", "white")
    fightButton = button.Button(650, 360, 60, 30, "black", "fight", "white")
    player1Money = button.Button(110, 720, 70, 30, "black", "0", "white")
    player2Money = button.Button(110, 50, 70, 30, "black", "0", "white")
    fightButton.enable = False

    done = False
    
    myGame = game.Game(1)

    player1dic = dict()
    player2dic = dict()
    firstTime = True
    applyGamePhase = True

    fight = False
    
    enableChooseDiceForPlayer1 = False
    enableChooseDiceForPlayer2 = False
    player1LastRoll = False
    player2lastRoll = False
    autoChoosePlayer1LastRoll = False
    autoChoosePlayer2lastRoll = False

    while not done:
        if fight == True:
            time.sleep(2)
        (whoseTurn, whichPhase) = myGame.phase
        if whichPhase <= 3 and applyGamePhase == True:
            print("game phase is ", myGame.phase)
            if whichPhase == 3:
                if whoseTurn == 1:
                    player1LastRoll = True
                elif whoseTurn == 2:
                    player2lastRoll = True
            debugButton.text = "player" + str(whoseTurn) + "should roll"
            applyGamePhase = False
            if whoseTurn == 1:
                player1RollButton.enable = True
                player2RollButton.enable = False
            else:
                player1RollButton.enable = False
                player2RollButton.enable = True
        elif whichPhase == 4 and applyGamePhase == True:
            print("game phase is ", myGame.phase)
            debugButton.text = "Resolution"
            applyGamePhase = False
            fightButton.enable = True
            firstTime = True
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            if event.type == pg.MOUSEBUTTONDOWN:
                (x, y) = pg.mouse.get_pos()
                print((x, y))
                if fightButton.enable == True and fightButton.hasButtonClicked(x, y):
                    fight = True
                    fightButton.enable = False

                ###################################
                if player1RollButton.hasButtonClicked(x, y) and player1RollButton.enable == True:
                    player1.rollDices()
                    player1RollButton.enable = False
                    if whichPhase < 3:
                        enableChooseDiceForPlayer1 = True
                        player1confirmButton.enable = True
                        debugButton.text = "player1 should choose"
                    elif player1LastRoll == True:
                        player1LastRoll = False
                        autoChoosePlayer1LastRoll = True
                if player2RollButton.hasButtonClicked(x, y) and player2RollButton.enable == True:
                    player2.rollDices()
                    player2RollButton.enable = False
                    if whichPhase < 3:
                        enableChooseDiceForPlayer2 = True
                        player2confirmButton.enable = True
                        debugButton.text = "player2 should choose"
                    elif player2lastRoll == True:
                        player2lastRoll = False
                        autoChoosePlayer2lastRoll = True
                #################################
                if autoChoosePlayer1LastRoll == True:
                    for i in range(len(player1.dices)):
                        if player1.dices[i] != None:
                            player1.moveDiceToSlot(i)
                    autoChoosePlayer1LastRoll = False
                    myGame.update()
                    applyGamePhase = True
                if autoChoosePlayer2lastRoll == True:
                    for i in range(len(player2.dices)):
                        if player2.dices[i] != None:
                            player2.moveDiceToSlot(i)
                    autoChoosePlayer2lastRoll = False
                    myGame.update()
                    applyGamePhase = True
                #################################
                player1ClickedDice = player1.getClickedDice(x, y)
                if player1ClickedDice != -1 and enableChooseDiceForPlayer1 == True:
                    player1.moveDiceToSlot(player1ClickedDice)
                player2ClickedDice = player2.getClickedDice(x, y)
                if player2ClickedDice != -1 and enableChooseDiceForPlayer2 == True:
                    player2.moveDiceToSlot(player2ClickedDice)
                #################################
                player1ClickedEmptySlot = player1.getClickedEmptySlot(x, y)
                if player1ClickedEmptySlot != -1 and enableChooseDiceForPlayer1 == True:
                    player1.returnDiceFromSlot(player1ClickedEmptySlot)
                player2ClickedEmptySlot = player2.getClickedEmptySlot(x, y)
                if player2ClickedEmptySlot != -1 and enableChooseDiceForPlayer2 == True:
                    player2.returnDiceFromSlot(player2ClickedEmptySlot)
                #################################
                if player1confirmButton.hasButtonClicked(x, y) and player1confirmButton.enable == True:
                    enableChooseDiceForPlayer1 = False
                    player1confirmButton.enable = False
                    myGame.update()
                    applyGamePhase = True
                if player2confirmButton.hasButtonClicked(x, y) and player2confirmButton.enable == True:
                    enableChooseDiceForPlayer2 = False
                    player2confirmButton.enable
                    myGame.update()
                    applyGamePhase = True
                
        if fight == True:
            if firstTime == True:
                firstTime = False
                myGame.initAnalyze(player1, player2)
            if myGame.fightWithDice(player1, player2, "axe", "helmet"):
                pass
            elif myGame.fightWithDice(player1, player2, "arrow", "shield"):
                pass
            elif myGame.fightWithDice(player1, player2, "goldenArrow", "shield"):
                pass
            elif myGame.fightWithDice(player2, player1, "axe", "helmet"):
                pass
            elif myGame.fightWithDice(player2, player1, "arrow", "shield"):
                pass
            elif myGame.fightWithDice(player2, player1, "goldenArrow", "shield"):
                pass
            elif myGame.removeUselessDice(player1, "helmet"):
                pass
            elif myGame.removeUselessDice(player1, "goldenHelmet"):
                pass
            elif myGame.removeUselessDice(player1, "shield"):
                pass
            elif myGame.removeUselessDice(player1, "goldenShield"):
                pass
            elif myGame.removeUselessDice(player2, "helmet"):
                pass
            elif myGame.removeUselessDice(player2, "goldenHelmet"):
                pass
            elif myGame.removeUselessDice(player2, "shield"):
                pass
            elif myGame.removeUselessDice(player2, "goldenShield"):
                pass
            elif myGame.takeMoney(player1, player2):
                pass
            elif myGame.takeMoney(player2, player1):
                pass
            else:
                fight = False
                myGame.update()
                applyGamePhase = True
        screen.fill("white")
        for i in range(player1.health):
            screen.blit(heart, player1.heartLocations[i])
        for i in range(player2.health):
            screen.blit(heart, player2.heartLocations[i])
        for i in range(6):
            screen.blit(emptySlot, player1.emptySlots[i])
            screen.blit(emptySlot, player2.emptySlots[i])
            if player1.choosenDices[i] != None:
                screen.blit(player1.choosenDices[i].shownFace.texture, player1.emptySlots[i])
            if player2.choosenDices[i] != None:
                screen.blit(player2.choosenDices[i].shownFace.texture, player2.emptySlots[i])
        for i in range(6):
            if player1.dices[i] != None:
                screen.blit(player1.dices[i].shownFace.texture, player1.diceLocations[i])
            if player2.dices[i] != None:
                screen.blit(player2.dices[i].shownFace.texture, player2.diceLocations[i])
        player1RollButton.draw(pg, screen)
        player2RollButton.draw(pg, screen)
        player1confirmButton.draw(pg, screen)
        player2confirmButton.draw(pg, screen)
        debugButton.draw(pg, screen)
        fightButton.draw(pg,screen)
        player1Money.text = str(player1.money)
        player2Money.text = str(player2.money)
        player1Money.draw(pg, screen)
        player2Money.draw(pg, screen)
        pg.display.flip()


main()