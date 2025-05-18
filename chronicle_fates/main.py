import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600

# Grid dimensions and cell size
grid_size = 10
cell_size = 50

# Player position (in grid coordinates)
player_pos = [0, 0]

# Colors
white = (255, 255, 255)
blue = (0, 0, 255)

# Create the screen surface
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the window title
pygame.display.set_caption("Chronicle Fates")

# Game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if player_pos[0] > 0:
                    player_pos[0] -= 1
            if event.key == pygame.K_RIGHT:
                if player_pos[0] < grid_size - 1:
                    player_pos[0] += 1
            if event.key == pygame.K_UP:
                if player_pos[1] > 0:
                    player_pos[1] -= 1
            if event.key == pygame.K_DOWN:
                if player_pos[1] < grid_size - 1:
                    player_pos[1] += 1


    # Drawing
    screen.fill((0, 0, 0))  # Fill the background with black

    # Draw the grid
    for x in range(grid_size):
        pygame.draw.line(screen, white, (x * cell_size, 0), (x * cell_size, grid_size * cell_size))
        pygame.draw.line(screen, white, (0, x * cell_size), (grid_size * cell_size, x * cell_size))
    pygame.draw.line(screen, white, (grid_size * cell_size, 0), (grid_size * cell_size, grid_size * cell_size))
    pygame.draw.line(screen, white, (0, grid_size * cell_size), (grid_size * cell_size, grid_size * cell_size))

    # Draw the player
    player_rect = pygame.Rect(player_pos[0] * cell_size, player_pos[1] * cell_size, cell_size, cell_size)
    pygame.draw.rect(screen, blue, player_rect)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()