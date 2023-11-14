import pygame as py
from pygame import mixer
import os
from Trigo_Game import Trigo
mixer.init()
click_audio = os.path.join("Assets/Music", "click audio.mp3")
click_sound = mixer.Sound(click_audio)
class Button:
    def __init__(self,x, y ,image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.click = False
    def draw(self,surface):
        action = False
        surface.blit(self.image,(self.rect.x,self.rect.y))
        pos = py.mouse.get_pos()
        #intercating with the left mouse click
        if self.rect.collidepoint(pos):
            if py.mouse.get_pressed()[0] == 1 and self.click == False:
                click_sound.play()
                self.click = True
                action = True
        if py.mouse.get_pressed()[0] == 0:
            self.click = False
        return action

class Card:
    def __init__(self,x, y ,image,trigo):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.click = False
        self.trigo = trigo
    def draw(self,surface):
        action = False
        surface.blit(self.image,(self.rect.x,self.rect.y))
        pos = py.mouse.get_pos()
        #intercating with the left mouse click
        if self.rect.collidepoint(pos):
            if py.mouse.get_pressed()[0] == 1 and self.click == False:
                click_sound.play()
                # surface.blit(self.trigo.image,(self.rect.x,self.rect.y))
                self.click = True
                action = True
        if py.mouse.get_pressed()[0] == 0:
            self.click = False
        return action


