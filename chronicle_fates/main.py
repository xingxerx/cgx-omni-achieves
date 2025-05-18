import sys

# Grid dimensions and cell size
grid_size = 10
cell_size = 50

# Player position (in grid coordinates)
player_pos = [0, 0]

# Health
player_health = 10
enemy_health = 10

# Turn management
current_turn = "player"

# Future-sight
future_sight_active = False

# Fate Points
fate_points = 5

# Enemy position (in grid coordinates)
enemy_pos = [grid_size - 1, grid_size - 1] # Example starting position for the enemy

# Combat Logic Function
def handle_combat(player_pos, enemy_pos, enemy_health, player_health):
    enemy_defeated = False
    if player_pos == enemy_pos:
        if enemy_health > 0:
            print("Enemy hit!")
            enemy_health -= 1
            if enemy_health <= 0:
                enemy_defeated = True
        elif player_health > 0:
            player_health -= 1
    return enemy_health, enemy_defeated, player_health

if __name__ == "__main__":
    import pygame
    import pygame.font

    # Initialize Pygame
    pygame.init()
    pygame.font.init() # Initialize font module

    # Screen dimensions
    screen_width = 800
    screen_height = 600

    # Colors
    white = (255, 255, 255)
    blue = (0, 0, 255)
    red = (255, 0, 0)
    green = (0, 255, 0) # Color for future sight path
    black = (0, 0, 0)

    # Fonts
    font = pygame.font.Font(None, 36) # Default font, size 36

    # Create the screen surface
    screen = pygame.display.set_mode((screen_width, screen_height))

    # Set the window title
    pygame.display.set_caption("Chronicle Fates")

    # Predicted combat outcome display variables
    predicted_enemy_health_display = None
    predicted_combat_pos_display = None

    # Game loop
    running = True
    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Reset predicted combat display at the start of player turn event handling
            if current_turn == "player":
                predicted_enemy_health_display = None
                predicted_combat_pos_display = None

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

                    # Check for predicted combat outcome if future sight is active
                    temp_player_pos = list(player_pos) # Create a temporary copy
                    if event.key == pygame.K_LEFT and temp_player_pos[0] > 0:
                        temp_player_pos[0] -= 1
                    elif event.key == pygame.K_RIGHT and temp_player_pos[0] < grid_size - 1:
                        temp_player_pos[0] += 1
                    elif event.key == pygame.K_UP and temp_player_pos[1] > 0:
                        temp_player_pos[1] -= 1
                    elif event.key == pygame.K_DOWN and temp_player_pos[1] < grid_size - 1:
                        temp_player_pos[1] += 1


                    if future_sight_active and temp_player_pos == enemy_pos and enemy_health > 0:
                        predicted_enemy_health_display = enemy_health - 1
                        predicted_combat_pos_display = enemy_pos

                    if moved:
                        # Check for combat after player move
                        print(f"Player moved to: {player_pos}")
                        if player_pos == enemy_pos:
                            print("Combat!")
                            # Simple combat logic: player deals 1 damage
                            enemy_health, enemy_defeated, player_health = handle_combat(player_pos, enemy_pos, enemy_health, player_health)
                            print(f"Enemy health: {enemy_health}, Player health: {player_health}")
                            if enemy_defeated:
                                print("Enemy defeated!")
                                enemy_pos = [-1, -1] # Move enemy off-screen
                        current_turn = "enemy"


            # Toggle future sight with Fate Points
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if not future_sight_active and fate_points > 0:
                        future_sight_active = True
                        fate_points -= 1
                        print(f"Fate Points remaining: {fate_points}")
                        print("Future Sight Active!")
                    elif future_sight_active:
                        future_sight_active = False

        # Drawing
        screen.fill(black)  # Fill the background with black

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
        if enemy_health > 0:
            enemy_rect = pygame.Rect(enemy_pos[0] * cell_size, enemy_pos[1] * cell_size, cell_size, cell_size)
            pygame.draw.rect(screen, red, enemy_rect)

        # Draw predicted combat outcome
        if predicted_enemy_health_display is not None and predicted_combat_pos_display is not None:
            text_surface = font.render(f"Pred. HP: {predicted_enemy_health_display}", True, green)
            text_rect = text_surface.get_rect(center=(predicted_combat_pos_display[0] * cell_size + cell_size // 2, predicted_combat_pos_display[1] * cell_size + cell_size // 2 - 20)) # Adjust position to be above enemy
            screen.blit(text_surface, text_rect)

        # Draw Fate Points
        fate_points_text = font.render(f"Fate Points: {fate_points}", True, white)
        screen.blit(fate_points_text, (10, 10))

        # Enemy turn
        if current_turn == "enemy":
            print("\nEnemy turn!")
            print(f"Enemy starting position: {enemy_pos}")

            # Store original enemy position for drawing predicted path
            original_enemy_pos = list(enemy_pos)

            # Simple enemy AI: move towards the player
            if enemy_health > 0: # Only move if enemy is alive
                delta_x = player_pos[0] - enemy_pos[0]
                delta_y = player_pos[1] - enemy_pos[1]
                moved = False

                # Prioritize movement along the axis with the larger difference
                if abs(delta_x) > abs(delta_y):
                    # Move horizontally
                    if delta_x > 0 and enemy_pos[0] < grid_size - 1:
                        enemy_pos[0] += 1
                        moved = True
                    elif delta_x > 0 and enemy_pos[0] == grid_size - 1:
                        print("Enemy blocked by right boundary.")
                    elif delta_x < 0 and enemy_pos[0] > 0:
                        enemy_pos[0] -= 1
                        moved = True
                else:
                    # Move vertically
                    if delta_y > 0 and enemy_pos[1] < grid_size - 1:
                        enemy_pos[1] += 1
                        moved = True
                    elif delta_y < 0 and enemy_pos[1] > 0:
                        enemy_pos[1] -= 1

                if not moved and (abs(delta_x) > 0 or abs(delta_y) > 0):
                     print("Enemy blocked by boundary.")

                print(f"Enemy moved to: {enemy_pos}")
                # Check for combat after enemy move
                if player_pos == enemy_pos:
                    print("Combat!")
                    # Simple combat logic: enemy deals 1 damage
                    if player_health > 0: # Ensure player is still alive
                        player_health -= 1
                        print(f"Player health: {player_health}")
                        if player_health <= 0:
                            print("Player defeated!")
            current_turn = "player"

        # Update the display
        pygame.display.flip()

    # Quit Pygame
    pygame.quit()
    sys.exit()
