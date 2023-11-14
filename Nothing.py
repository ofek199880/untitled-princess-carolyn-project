import pygame
import random
from pygame.locals import *
import os

pygame.init()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Memory Matching Game')

# Load the card images
card_images = [
    pygame.image.load(os.path.join("Assets/Buttons","card.png")).convert(),
    pygame.image.load(os.path.join("Assets/Buttons","card.png")).convert(),
    pygame.image.load(os.path.join("Assets/Buttons","card.png")).convert(),
    pygame.image.load(os.path.join("Assets/Buttons","card.png")).convert(),
    pygame.image.load(os.path.join("Assets/Buttons","card.png")).convert(),
]

# Create a list of card surfaces, with the backs facing up
card_surfaces = [pygame.Surface((100, 100)) for i in range(10)]
for surface in card_surfaces:
    surface.fill((0, 0, 255))

# Place the card surfaces on a grid
card_rects = []
for i in range(2):
    for j in range(5):
        card_rect = card_surfaces[i * 5 + j].get_rect()
        card_rect.top = i * 120 + 50
        card_rect.left = j * 120 + 50
        card_rects.append(card_rect)

# Shuffle the card images
random.shuffle(card_images)

# Create a list of card front surfaces, with the images facing up
card_fronts = []
for i in range(10):
    card_front = pygame.Surface((100, 100))
    card_front.blit(card_images[i // 2], (0, 0))
    card_fronts.append(card_front)

# Initialize the game state
first_card = None
second_card = None
game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == QUIT:
            game_over = True
        elif event.type == MOUSEBUTTONDOWN and event.button == 1:
            # Check which card was clicked
            for i, card_rect in enumerate(card_rects):
                if card_rect.collidepoint(event.pos):
                    # If this is the first card clicked, show its front
                    if first_card is None:
                        first_card = i
                        card_surfaces[i] = card_fronts[i]
                    # If this is the second card clicked, show its front and check for a match
                    elif second_card is None:
                        second_card = i
                        card_surfaces[i] = card_fronts[i]
                        # If the cards match, remove them from the screen
                        if card_images[first_card // 2] == card_images[second_card // 2]:
                            card_surfaces[first_card] = pygame.Surface((100, 100))
                            card_surfaces[second_card] = pygame.Surface((100, 100))
                        # If the cards don't match, flip them back over after a short delay
                        else:
                            pygame.time.wait(500)
                            card_surfaces[first_card] = pygame.Surface((100, 100))
                            card_surfaces[second_card] = pygame.Surface((100, 100))
                        first_card = None
                        second_card = None

    # Draw the screen
    screen.fill((255, 255,255))
    pygame.display.update()
pygame.quit()