import pygame
pygame.init()  # Initialize Pygame

# Set up display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("My First Pygame Window")

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255, 255, 255))  # Fill the screen with white color
    pygame.display.flip()  # Update the display

pygame.quit()
