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

# Turn management
current_turn = "player"

# Future-sight
future_sight_active = False

# Enemy position (in grid coordinates)
enemy_pos = [grid_size - 1, grid_size - 1] # Example starting position for the enemy

# Colors
white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)

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
        
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            future_sight_active = not future_sight_active

        if current_turn == "player":
            if event.type == pygame.KEYDOWN:
                moved = False
                if event.key == pygame.K_LEFT:
                    if player_pos[0] > 0:
                        player_pos[0] -= 1
                        moved = True
                elif event.key == pygame.K_RIGHT:
                    if player_pos[0] < grid_size - 1:
                        player_pos[0] += 1
                        moved = True
                elif event.key == pygame.K_UP:
                    if player_pos[1] > 0:
                        player_pos[1] -= 1
                        moved = True
                elif event.key == pygame.K_DOWN:
                    if player_pos[1] < grid_size - 1:
                        player_pos[1] += 1
                        moved = True

                if moved:
                    current_turn = "enemy"

    # Check for combat after player move
    if player_pos == enemy_pos:
        print("Combat!")

    # Future-sight placeholder
    if future_sight_active:
        print("Future Sight Active!")

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

    # Draw the enemy
    enemy_rect = pygame.Rect(enemy_pos[0] * cell_size, enemy_pos[1] * cell_size, cell_size, cell_size)
    pygame.draw.rect(screen, red, enemy_rect)

    # Enemy turn (placeholder)
    if current_turn == "enemy":
        print("Enemy turn!")
        pygame.time.delay(500) # Simulate enemy thinking/action time
        current_turn = "player"

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()