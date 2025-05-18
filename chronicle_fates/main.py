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

        # Draw predicted enemy path (placeholder: straight line to player)
        # This is a very basic prediction and will be improved later
        current_x, current_y = enemy_pos
        target_x, target_y = player_pos

        # Calculate steps to draw
        steps = max(abs(target_x - current_x), abs(target_y - current_y))
        if steps > 0:
            x_increment = (target_x - current_x) / steps
            y_increment = (target_y - current_y) / steps

            for i in range(steps + 1):
                predicted_x = int(current_x + x_increment * i)
                predicted_y = int(current_y + y_increment * i)
    # Drawing
                # Draw predicted enemy position (as small green squares)
                predicted_rect = pygame.Rect(predicted_x * cell_size, predicted_y * cell_size, cell_size, cell_size)
                pygame.draw.rect(screen, green, predicted_rect, 2) # Draw outline


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
    if current_turn == "enemy" and not future_sight_active: # Only move if future sight is not active
        print("Enemy turn!")

        # Simple enemy AI: move towards the player
        delta_x = player_pos[0] - enemy_pos[0]
        delta_y = player_pos[1] - enemy_pos[1]

        if abs(delta_x) > abs(delta_y):
            # Move horizontally
            if delta_x > 0 and enemy_pos[0] < grid_size - 1:
                enemy_pos[0] += 1
            elif delta_x < 0 and enemy_pos[0] > 0:
                enemy_pos[0] -= 1
        else:
            # Move vertically
            if delta_y > 0 and enemy_pos[1] < grid_size - 1:
                enemy_pos[1] += 1
            elif delta_y < 0 and enemy_pos[1] > 0:
                enemy_pos[1] -= 1
        current_turn = "player"

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()