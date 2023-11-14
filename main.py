import pygame as pg
import dice, player, game, button
import random


def main():

    pg.init()
    WINDOW_SIZE = [800, 800]
    screen = pg.display.set_mode(WINDOW_SIZE)

    pg.display.set_caption("Orlog")

    DEFAULT_DICE_FACE_SIZE = (50, 50)
    DEFAULT_HEART_SIZE = (30, 30)

    #dice faces
    arrow = pg.transform.scale(pg.image.load("orlog pictures/arrow.png"), DEFAULT_DICE_FACE_SIZE)
    axe = pg.transform.scale(pg.image.load("orlog pictures/axe.png"), DEFAULT_DICE_FACE_SIZE)
    hand = pg.transform.scale(pg.image.load("orlog pictures/hand.png"), DEFAULT_DICE_FACE_SIZE)
    helmet = pg.transform.scale(pg.image.load("orlog pictures/helmet.png"), DEFAULT_DICE_FACE_SIZE)
    shield = pg.transform.scale(pg.image.load("orlog pictures/shield.png"), DEFAULT_DICE_FACE_SIZE)
    goldenArrow = pg.transform.scale(pg.image.load("orlog pictures/goldenArrow.png"), DEFAULT_DICE_FACE_SIZE)
    goldenHand = pg.transform.scale(pg.image.load("orlog pictures/goldenHand.png"), DEFAULT_DICE_FACE_SIZE)
    goldenHelmet = pg.transform.scale(pg.image.load("orlog pictures/goldenHelmet.png"), DEFAULT_DICE_FACE_SIZE)
    goldenShield = pg.transform.scale(pg.image.load("orlog pictures/goldenShield.png"), DEFAULT_DICE_FACE_SIZE)
    emptySlot = pg.transform.scale(pg.image.load("orlog pictures/slot.png"), DEFAULT_DICE_FACE_SIZE)

    heart = pg.transform.scale(pg.image.load("orlog pictures/heart.png"), DEFAULT_HEART_SIZE)

    #make dices
    diceType11 = dice.dice(axe, shield, goldenArrow, axe, helmet, goldenHand)
    diceType12 = dice.dice(axe, goldenShield, arrow, axe, goldenHand, helmet)
    diceType13 = dice.dice(axe, goldenArrow, hand, axe, goldenHelmet, shield)
    diceType14 = dice.dice(axe, shield, goldenHand, arrow, goldenHelmet, axe)
    diceType15 = dice.dice(axe, goldenShield, hand, axe, helmet, goldenArrow)
    diceType16 = dice.dice(axe, goldenShield, hand, axe, arrow, goldenHelmet)
    diceType21 = dice.dice(axe, shield, goldenArrow, axe, helmet, goldenHand)
    diceType22 = dice.dice(axe, goldenShield, arrow, axe, goldenHand, helmet)
    diceType23 = dice.dice(axe, goldenArrow, hand, axe, goldenHelmet, shield)
    diceType24 = dice.dice(axe, shield, goldenHand, arrow, goldenHelmet, axe)
    diceType25 = dice.dice(axe, goldenShield, hand, axe, helmet, goldenArrow)
    diceType26 = dice.dice(axe, goldenShield, hand, axe, arrow, goldenHelmet)

    diceList1 = [diceType11, diceType12, diceType13, diceType14, diceType15, diceType16]
    diceList2 = [diceType21, diceType22, diceType23, diceType24, diceType25, diceType26]

    player1 = player.player(diceList1, [70, 600], DEFAULT_HEART_SIZE, [280, 430], [350, 600], DEFAULT_DICE_FACE_SIZE)
    player2 = player.player(diceList2, [70, 110], DEFAULT_HEART_SIZE, [280, 320], [350, 150], DEFAULT_DICE_FACE_SIZE)

    player1RollButton = button.Button(460, 750, 100, 30, "black", "Roll", "white")
    player2RollButton = button.Button(460, 20, 100, 30, "black", "roll", "white")
    

    done = False
    
    game.Game(random.randint(1, 2))

    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            if event.type == pg.MOUSEBUTTONDOWN:
                (x, y) = pg.mouse.get_pos()
                print((x, y))
                if player1RollButton.hasButtonClicked(x, y) and player1RollButton.enable == True:
                    player1.rollDices()
                if player2RollButton.hasButtonClicked(x, y) and player2RollButton.enable == True:
                    player2.rollDices()
                #################################
                player1ClickedDice = player1.getClickedDice(x, y)
                if player1ClickedDice != -1:
                    player1.choosenDices[player1ClickedDice] = player1.removeDice(player1ClickedDice)
                player2ClickedDice = player2.getClickedDice(x, y)
                if player2ClickedDice != -1:
                    player2.choosenDices[player2ClickedDice] = player2.removeDice(player2ClickedDice)
                
        
        screen.fill("white")
        for i in range(player1.health):
            screen.blit(heart, player1.heartLocations[i])
        for i in range(player2.health):
            screen.blit(heart, player2.heartLocations[i])
        for i in range(6):
            screen.blit(emptySlot, player1.emptySlots[i])
            screen.blit(emptySlot, player2.emptySlots[i])
            if player1.choosenDices[i] != None:
                screen.blit(player1.choosenDices[i].getShownFace(), player1.emptySlots[i])
            if player2.choosenDices[i] != None:
                screen.blit(player2.choosenDices[i].getShownFace(), player2.emptySlots[i])
        for i in range(6):
            if player1.dices[i] != None:
                screen.blit(player1.dices[i].getShownFace(), player1.diceLocations[i])
            if player2.dices[i] != None:
                screen.blit(player2.dices[i].getShownFace(), player2.diceLocations[i])
        player1RollButton.draw(pg, screen)
        player2RollButton.draw(pg, screen)
        pg.display.flip()


main()