import pygame as pg
import dice, player, game
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
    diceType1 = dice.dice(axe, shield, goldenArrow, axe, helmet, goldenHand)
    diceType2 = dice.dice(axe, goldenShield, arrow, axe, goldenHand, helmet)
    diceType3 = dice.dice(axe, goldenArrow, hand, axe, goldenHelmet, shield)
    diceType4 = dice.dice(axe, shield, goldenHand, arrow, goldenHelmet, axe)
    diceType5 = dice.dice(axe, goldenShield, hand, axe, helmet, goldenArrow)
    diceType6 = dice.dice(axe, goldenShield, hand, axe, arrow, goldenHelmet)

    diceList = [diceType1, diceType2, diceType3, diceType4, diceType5, diceType6]

    player1 = player.player(diceList, [70, 600], DEFAULT_HEART_SIZE, [280, 430], DEFAULT_DICE_FACE_SIZE)
    player2 = player.player(diceList, [70, 110], DEFAULT_HEART_SIZE, [280, 320], DEFAULT_DICE_FACE_SIZE)
    

    done = False
    
    game.Game(random.randint(1, 2))

    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            if event.type == pg.MOUSEBUTTONDOWN:
                print(pg.mouse.get_pos())
        
        screen.fill("white")
        for i in range(player1.health):
            screen.blit(heart, player1.heartLocations[i])
        for i in range(6):
            screen.blit(emptySlot, player1.emptySlots[i])
        for i in range(player2.health):
            screen.blit(heart, player2.heartLocations[i])
        for i in range(6):
            screen.blit(emptySlot, player2.emptySlots[i])

        pg.display.flip()


main()