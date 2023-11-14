import pygame as py
from Button import Button,Card
from Background import Background
from pygame import mixer
from Trigo_Game import Trigo
import os
import sys
from test import *

WIDTH, HEIGHT = 1080, 720
WIN = py.display.set_mode((WIDTH, HEIGHT))
py.display.set_caption("Untitled Princess Carolyn Project")
PINK = (240,75,189)
WHITE = (255,255,255)
FPS = 60

welcome = py.image.load(os.path.join("Assets/Background","open.png"))
welcome = py.transform.scale(welcome,(1080,720))
stage = py.image.load(os.path.join("Assets/Background","stage.png"))
stage = py.transform.scale(stage,(1080,720))
start_button = py.image.load(os.path.join("Assets/Buttons","start button.png")).convert_alpha()
start_button = py.transform.scale(start_button,(250,125))
music_button = py.image.load(os.path.join("Assets/Buttons","music wooden button.png")).convert_alpha()
music_button = py.transform.scale(music_button,(60,50))
pause_button = py.image.load(os.path.join("Assets/Buttons","pause wooden button.png")).convert_alpha()
pause_button = py.transform.scale(pause_button,(60,50))
card_button = py.image.load(os.path.join("Assets/Buttons","card.png")).convert_alpha()
card_button = py.transform.scale(card_button,(100,150))
Title_Theme = os.path.join("Assets/Music", "Title Theme.mp3")
click_audio = os.path.join("Assets/Music", "click audio.mp3")
Minigame = os.path.join("Assets/Music", "Minigame.mp3")
LastFantasy = os.path.join("Assets/Music", "The Final of The Fantasy.mp3")
start_btn = Button(415,400,start_button)
music_btn = Button(955,0,music_button)
pause_btn = Button(1017,0,pause_button)
# card_btn = Card(450,450,card_button)
open = Background(welcome)
stage = Background(stage)
py.init()

def draw_board():
    screen.fill(PURPLE)
    stage.draw(screen)
    if pause_btn.draw(WIN):
        main()
    if music_btn.draw(WIN):
        if py.mixer.music.get_volume() == 0:
            py.mixer.music.set_volume(0.2)
        elif py.mixer.music.get_volume() != 0:
            py.mixer.music.set_volume(0)
    card_btn1.draw(screen)
    card_btn2.draw(screen)
    card_btn3.draw(screen)
    card_btn4.draw(screen)
    card_btn5.draw(screen)
    card_btn6.draw(screen)
    card_btn7.draw(screen)
    card_btn8.draw(screen)
    card_btn9.draw(screen)
    card_btn10.draw(screen)
    card_btn11.draw(screen)
    card_btn12.draw(screen)
    card_btn13.draw(screen)
    card_btn14.draw(screen)
    card_btn15.draw(screen)
    card_btn16.draw(screen)
    card_btn17.draw(screen)
    card_btn18.draw(screen)
    card_btn19.draw(screen)
    card_btn20.draw(screen)
    card_btn21.draw(screen)
    card_btn22.draw(screen)
    card_btn23.draw(screen)
    card_btn24.draw(screen)
    py.display.update()
def start():
    global first_guess_num
    global first_card
    global second_guess_num
    global second_card
    global board_matrix
    global screen
    run = True
    py.init()
    mixer.init()
    mixer.music.load(LastFantasy)
    py.mixer.music.set_volume(0.2)
    mixer.music.play(-1)
    while run:
        for event in py.event.get():
            if event.type == py.QUIT:
                run = False
            elif event.type == py.MOUSEBUTTONDOWN:
                for i in board_matrix:
                    for j in i:
                        btn = j
                        if btn.rect.collidepoint(event.pos) and not first_card:
                            first_card = True
                            first_guess_num = len(btn.trigo)
                            while btn.draw(screen):
                                WIN.blit(btn.trigo.image, (btn.rect.x, btn.rect.y))
                                py.display.update()
                            if btn.rect.collidepoint(event.pos) and not second_card and first_card and len(btn.trigo) != first_guess_num:
                                second_card = True
                                second_guess_num = len(btn.trigo)
                                print(second_guess_num)
        if first_card and second_card:
            first_card = False
            second_card = False
        draw_board()
        py.display.update()
    py.quit()

def draw_stage():
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            sys.exit()
        if event.type == py.MOUSEBUTTONDOWN:
            start()
            pass
    WIN.fill(WHITE)
    stage.draw(WIN)
    if pause_btn.draw(WIN):
        main()
    if music_btn.draw(WIN):
        if py.mixer.music.get_volume() == 0:
            py.mixer.music.set_volume(0.2)
        elif py.mixer.music.get_volume() != 0:
            py.mixer.music.set_volume(0)

    py.display.update()

def draw_window():
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            sys.exit()
    WIN.fill(PINK)
    open.draw(WIN)
    if pause_btn.draw(WIN):
        print("pause")
    if start_btn.draw(WIN):
        print("start")
    if music_btn.draw(WIN):
        print('sound off')
        if py.mixer.music.get_volume() == 0:
            py.mixer.music.set_volume(0.2)
        elif py.mixer.music.get_volume() != 0:
            py.mixer.music.set_volume(0)

    py.display.update()


def main():
    clock = py.time.Clock()
    run = True
    level = False
    mixer.init()
    mixer.music.load(Title_Theme)
    py.mixer.music.set_volume(0.2)
    mixer.music.play(-1)
    while run:
        clock.tick(FPS)

        for event in py.event.get():
            if event.type == py.QUIT:
                run = False

        while level:
            draw_stage()
            if pause_btn.draw(WIN):
                main()
        if start_btn.draw(WIN):
            level = True
        draw_window()

    py.quit()



if __name__ == "__main__":
    main()