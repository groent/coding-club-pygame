import pygame
import sys

from pygame.time import Clock

# Initialize Pygame
pygame.init()

# Set up the game window
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Basic Window and Movement")

# Set initial position of the red dot
dot_x, dot_y = 400, 300
dot_radius = 10
dot_color = (255, 0, 0)  # Red color
clock= pygame.time.Clock()


# Movement speed
speed = 3

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        # Handle the quit event
        if event.type == pygame.QUIT:
            running = False

        # Handle key presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    # Get all currently pressed keys
    keys = pygame.key.get_pressed()

    # Movement using WASD keys
    if keys[pygame.K_w] or keys[pygame.K_UP]:    # Move up
        dot_y -= speed
    if keys[pygame.K_s] or keys[pygame.K_DOWN]:  # Move down
        dot_y += speed
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:  # Move left
        dot_x -= speed
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]: # Move right
        dot_x += speed

    # Fill the screen with a color (optional)
    screen.fill((0, 0, 0))  # Black background

    # Draw the red dot
    pygame.draw.circle(screen, dot_color, (dot_x, dot_y), dot_radius)

    # Update the display
    pygame.display.flip()
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()

