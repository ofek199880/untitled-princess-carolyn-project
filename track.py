from pygame import mixer
import pygame as pygame
import os
mixer.init()
track1 = pygame.mixer.music.load(os.path.join("Assets","Title Theme.mp3"),"mp3")

def music():
    mixer.init()

    # Load audio file
    mixer.music.load(track1)

    # Set preferred volume
    mixer.music.set_volume(0.2)

    # Play the music
    mixer.music.play()

music()