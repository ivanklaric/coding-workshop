import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
CELL_SIZE = 30
GRID_WIDTH = 19
GRID_HEIGHT = 21
WINDOW_WIDTH = GRID_WIDTH * CELL_SIZE
WINDOW_HEIGHT = GRID_HEIGHT * CELL_SIZE

# Colors
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)

# Set up display
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Pac-Man")

# Game map (0: empty path, 1: wall, 2: dot, 3: power pellet)
game_map = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,2,2,2,2,2,2,2,2,1,2,2,2,2,2,2,2,2,1],
    [1,3,1,1,2,1,1,1,2,1,2,1,1,1,2,1,1,3,1],
    [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1],
    [1,2,1,1,2,1,2,1,1,1,1,1,2,1,2,1,1,2,1],
    [1,2,2,2,2,1,2,2,2,1,2,2,2,1,2,2,2,2,1],
    [1,1,1,1,2,1,1,1,0,1,0,1,1,1,2,1,1,1,1],
    [1,0,0,1,2,1,0,0,0,0,0,0,0,1,2,1,0,0,1],
    [1,1,1,1,2,1,0,1,1,0,1,1,0,1,2,1,1,1,1],
    [0,0,0,0,2,0,0,1,0,0,0,1,0,0,2,0,0,0,0],
    [1,1,1,1,2,1,0,1,1,1,1,1,0,1,2,1,1,1,1],
    [1,0,0,1,2,1,0,0,0,0,0,0,0,1,2,1,0,0,1],
    [1,1,1,1,2,1,0,1,1,1,1,1,0,1,2,1,1,1,1],
    [1,2,2,2,2,2,2,2,2,1,2,2,2,2,2,2,2,2,1],
    [1,2,1,1,2,1,1,1,2,1,2,1,1,1,2,1,1,2,1],
    [1,3,2,1,2,2,2,2,2,2,2,2,2,2,2,1,2,3,1],
    [1,1,2,1,2,1,2,1,1,1,1,1,2,1,2,1,2,1,1],
    [1,2,2,2,2,1,2,2,2,1,2,2,2,1,2,2,2,2,1],
    [1,2,1,1,1,1,1,1,2,1,2,1,1,1,1,1,1,2,1],
    [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]

# Pacman properties
pacman_x = CELL_SIZE * 9
pacman_y = CELL_SIZE * 15
pacman_direction = [0, 0]  # [x_direction, y_direction]
next_direction = [0, 0]

# Ghost properties
ghosts = [
    {"x": 9 * CELL_SIZE, "y": 9 * CELL_SIZE, "color": RED, "direction": [1, 0]},
    {"x": 10 * CELL_SIZE, "y": 9 * CELL_SIZE, "color": (255, 182, 255), "direction": [-1, 0]}
]

# Game state
score = 0
game_over = False
power_mode = False
power_timer = 0

# Font
font = pygame.font.Font(None, 36)

def get_cell_position(x, y):
    """Convert pixel coordinates to grid cell position"""
    return int(x // CELL_SIZE), int(y // CELL_SIZE)

def can_move(x, y):
    """Check if movement to position is valid"""
    cell_x, cell_y = get_cell_position(x, y)
    if 0 <= cell_x < GRID_WIDTH and 0 <= cell_y < GRID_HEIGHT:
        return game_map[cell_y][cell_x] != 1
    return False

def move_ghost(ghost):
    """Move ghost and handle collision with walls"""
    possible_directions = []
    current_x, current_y = get_cell_position(ghost["x"], ghost["y"])
    
    # Check all possible directions
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        new_x = ghost["x"] + dx * CELL_SIZE
        new_y = ghost["y"] + dy * CELL_SIZE
        if can_move(new_x, new_y):
            possible_directions.append([dx, dy])
    
    # If at center of cell, maybe change direction
    if ghost["x"] % CELL_SIZE == 0 and ghost["y"] % CELL_SIZE == 0:
        if possible_directions:
            # Prefer current direction if possible
            if ghost["direction"] in possible_directions:
                if random.random() < 0.8:  # 80% chance to keep direction
                    return
            ghost["direction"] = random.choice(possible_directions)
    
    # Move ghost
    new_x = ghost["x"] + ghost["direction"][0] * 2
    new_y = ghost["y"] + ghost["direction"][1] * 2
    if can_move(new_x, new_y):
        ghost["x"] = new_x
        ghost["y"] = new_y

# Game loop
clock = pygame.time.Clock()
running = True

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                next_direction = [0, -1]
            elif event.key == pygame.K_DOWN:
                next_direction = [0, 1]
            elif event.key == pygame.K_LEFT:
                next_direction = [-1, 0]
            elif event.key == pygame.K_RIGHT:
                next_direction = [1, 0]
            elif event.key == pygame.K_SPACE and game_over:
                # Reset game
                pacman_x = CELL_SIZE * 9
                pacman_y = CELL_SIZE * 15
                pacman_direction = [0, 0]
                next_direction = [0, 0]
                score = 0
                game_over = False
                power_mode = False
                power_timer = 0
    
    if not game_over:
        # Try to change to next_direction if possible
        new_x = pacman_x + next_direction[0] * CELL_SIZE
        new_y = pacman_y + next_direction[1] * CELL_SIZE
        if can_move(new_x, new_y):
            pacman_direction = next_direction
        
        # Move Pacman
        new_x = pacman_x + pacman_direction[0] * 3
        new_y = pacman_y + pacman_direction[1] * 3
        if can_move(new_x, new_y):
            pacman_x = new_x
            pacman_y = new_y
        
        # Check for dot collection
        cell_x, cell_y = get_cell_position(pacman_x, pacman_y)
        if game_map[cell_y][cell_x] == 2:
            game_map[cell_y][cell_x] = 0
            score += 10
        elif game_map[cell_y][cell_x] == 3:
            game_map[cell_y][cell_x] = 0
            score += 50
            power_mode = True
            power_timer = 300  # 5 seconds at 60 FPS
        
        # Move ghosts
        for ghost in ghosts:
            move_ghost(ghost)
            
            # Check for collision with ghosts
            ghost_cell = get_cell_position(ghost["x"], ghost["y"])
            pacman_cell = get_cell_position(pacman_x, pacman_y)
            
            if ghost_cell == pacman_cell:
                if power_mode:
                    # Reset ghost position
                    ghost["x"] = 9 * CELL_SIZE
                    ghost["y"] = 9 * CELL_SIZE
                    score += 200
                else:
                    game_over = True
        
        # Update power mode timer
        if power_mode:
            power_timer -= 1
            if power_timer <= 0:
                power_mode = False
    
    # Draw game
    screen.fill(BLACK)
    
    # Draw maze and dots
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            cell = game_map[y][x]
            if cell == 1:  # Wall
                pygame.draw.rect(screen, BLUE, 
                               (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            elif cell == 2:  # Dot
                pygame.draw.circle(screen, WHITE,
                                 (x * CELL_SIZE + CELL_SIZE//2,
                                  y * CELL_SIZE + CELL_SIZE//2), 3)
            elif cell == 3:  # Power pellet
                pygame.draw.circle(screen, WHITE,
                                 (x * CELL_SIZE + CELL_SIZE//2,
                                  y * CELL_SIZE + CELL_SIZE//2), 8)
    
    # Draw Pacman
    pygame.draw.circle(screen, YELLOW,
                      (int(pacman_x + CELL_SIZE//2),
                       int(pacman_y + CELL_SIZE//2)), CELL_SIZE//2)
    
    # Draw ghosts
    for ghost in ghosts:
        color = ghost["color"]
        if power_mode:
            color = (0, 0, 255)  # Blue when vulnerable
        pygame.draw.circle(screen, color,
                         (int(ghost["x"] + CELL_SIZE//2),
                          int(ghost["y"] + CELL_SIZE//2)), CELL_SIZE//2)
    
    # Draw score
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))
    
    # Draw game over message
    if game_over:
        game_over_text = font.render("Game Over! Press SPACE to restart", True, WHITE)
        text_rect = game_over_text.get_rect(center=(WINDOW_WIDTH//2, WINDOW_HEIGHT//2))
        screen.blit(game_over_text, text_rect)
    
    # Update display
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()