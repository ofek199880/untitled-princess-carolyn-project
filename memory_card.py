import pygame
import random
def memory_game():
# Initialize pygame
    pygame.init()

    # Define colors
    red = (255, 0, 0)
    blue = (0, 0, 255)
    black = (0, 0, 0)
    white = (255, 255, 255)

    # Define screen size
    screen_size = (800, 600)

    # Define card size
    card_size = (100, 100)

    # Define number of rows and columns
    rows = 4
    columns = 4

    # Create list of card pairs
    card_pairs = []
    for i in range(int(rows * columns / 2)):
        card_pairs.append(i)
        card_pairs.append(i)

    # Shuffle card pairs
    random.shuffle(card_pairs)

    # Define screen
    screen = pygame.display.set_mode(screen_size)

    # Set screen title
    pygame.display.set_caption("Memory Card Game")

    # Create list to store state of cards (hidden or shown)
    card_state = [False] * (rows * columns)

    # Create list to store last card selected
    last_card = None

    # Create game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONUP:
                # Get position of mouse click
                pos = pygame.mouse.get_pos()
                # Calculate which card was clicked based on position
                column = pos[0] // card_size[0]
                row = pos[1] // card_size[1]
                card_index = row * columns + column
                # If the card is not already shown
                if not card_state[card_index]:
                    # Show the card
                    card_state[card_index] = True
                    # If a previous card was selected
                    if last_card:
                        # Check if the cards match
                        if card_pairs[last_card] == card_pairs[card_index]:
                            print("Match found!")
                        else:
                            # If cards do not match, hide both cards after a short delay
                            pygame.time.wait(1000)
                            card_state[last_card] = False
                            card_state[card_index] = False
                    last_card = card_index

        # Clear screen
        screen.fill(white)

        # Draw cards
        for row in range(rows):
            for column in range(columns):
                card_x = column * card_size[0]
                card_y = row * card_size[1]
                card_rect = pygame.Rect(card_x, card_y, card_size[0], card_size[1])
                if card_state[row * columns + column]:
                    pygame.draw.rect(screen, red, card_rect)
                else:
                    pygame.draw.rect(screen, blue, card_rect)

        # Update screen
        pygame.display.update()

    # Quit pygame
    pygame.quit()


if __name__ == '__main__':
    memory_game()
