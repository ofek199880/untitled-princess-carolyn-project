import random
import pygame
import os
from Background import Background
import sys
from Trigo_Game import*
from Button import *
random_list = []
#making random list of the trigo identities
#creating an empty board
board_matrix = [[0,0,0,0,0,0],
                [0,0,0,0,0,0],
                [0,0,0,0,0,0],
                [0,0,0,0,0,0]]
n = 0
count = 0

screen = py.display.set_mode((1080, 720))
PURPLE = (120,0,80)
X,Y = 0,-20

card_button = py.image.load(os.path.join("Assets/Buttons","card.png")).convert_alpha()
card_button = py.transform.scale(card_button,(100,150))

yrow1 = 100
yrow2 = 250
yrow3 = 400
yrow4 = 550
xrow1 = 100
xrow2 = 250
xrow3 = 400
xrow4 = 550
xrow5 = 700
xrow6 = 850
stage = py.image.load(os.path.join("Assets/Background","stage.png"))
stage = py.transform.scale(stage,(1080,720))
stage = Background(stage)
first_card = False
second_card = False
first_guess_num = 0
second_guess_num = 0
LastFantasy = os.path.join("Assets/Music", "The Final of The Fantasy.mp3")
card_btn1 = Card(xrow1,yrow1,card_button,card1)
card_btn2 = Card(xrow2,yrow1,card_button,card2)
card_btn3 = Card(xrow3,yrow1,card_button,card3)
card_btn4 = Card(xrow4,yrow1,card_button,card4)
card_btn5 = Card(xrow5,yrow1,card_button,card5)
card_btn6 = Card(xrow6,yrow1,card_button,card6)

card_btn7 = Card(xrow1,yrow2,card_button,card7)
card_btn8 = Card(xrow2,yrow2,card_button,card8)
card_btn9 = Card(xrow3,yrow2,card_button,card9)
card_btn10 = Card(xrow4,yrow2,card_button,card10)
card_btn11= Card(xrow5,yrow2,card_button,card11)
card_btn12 = Card(xrow6,yrow2,card_button,card12)

card_btn13 = Card(xrow1,yrow3,card_button,card13)
card_btn14 = Card(xrow2,yrow3,card_button,card14)
card_btn15 = Card(xrow3,yrow3,card_button,card15)
card_btn16 = Card(xrow4,yrow3,card_button,card16)
card_btn17 = Card(xrow5,yrow3,card_button,card17)
card_btn18 = Card(xrow6,yrow3,card_button,card18)

card_btn19 = Card(xrow1,yrow4,card_button,card19)
card_btn20 = Card(xrow2,yrow4,card_button,card20)
card_btn21 = Card(xrow3,yrow4,card_button,card21)
card_btn22 = Card(xrow4,yrow4,card_button,card22)
card_btn23 = Card(xrow5,yrow4,card_button,card23)
card_btn24 = Card(xrow6,yrow4,card_button,card24)
card_list = [card_btn1,card_btn2,card_btn3,card_btn4,card_btn5,card_btn6,card_btn7,card_btn8,card_btn9,card_btn10,card_btn11,card_btn12,card_btn13,card_btn14,card_btn15,card_btn16,card_btn17,card_btn18,card_btn19,card_btn20,card_btn21,card_btn22,card_btn23,card_btn24]
for i in range(len(card_list)):
    j = random.randint(0,len(card_list)-1)
    random_list.append(card_list[j])
    card_list.pop(j)
for s in board_matrix:
    for k in range(len(s)):
        s[k] = random_list[count]
        n += 1
        count += 1
        if n == 6:
            n = 0
            continue

