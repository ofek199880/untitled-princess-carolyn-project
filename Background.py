import pygame as py

class Background:
    def __init__(self,image):
        self.image = image
        self.rect = self.image.get_rect()
    def draw(self,surface):
        surface.blit(self.image,(0,0))