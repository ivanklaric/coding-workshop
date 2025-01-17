import pygame
import random
import sys
import os

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PLAYER_SPEED = 5
BULLET_SPEED = 7
ENEMY_SPEED = 3
STAR_SPEED = 2
FPS = 60
NUM_STARS = 100

# Colors
BLACK = (0, 0, 0)
STAR_COLORS = [
    (150, 150, 150),  # Dim white
    (200, 200, 200),  # Bright white
    (200, 200, 255),  # Blue-ish
]

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Shooter")
clock = pygame.time.Clock()

# Load images
def load_image(filename, size=(40, 40)):
    try:
        # Get the directory where the script/binary is located
        script_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(script_dir, "assets", filename)
        image = pygame.image.load(image_path)
        return pygame.transform.scale(image, size)
    except pygame.error as e:
        print(f"Couldn't load image {filename}: {e}")
        # Create a colored rectangle as fallback
        surface = pygame.Surface(size)
        surface.fill((255, 255, 255))
        return surface

# Create stars
def create_stars():
    stars = []
    for _ in range(NUM_STARS):
        star = {
            'x': random.randint(0, SCREEN_WIDTH),
            'y': random.randint(0, SCREEN_HEIGHT),
            'speed': random.uniform(0.5, STAR_SPEED),
            'size': random.randint(1, 3),
            'color': random.choice(STAR_COLORS)
        }
        stars.append(star)
    return stars

def update_stars(stars):
    for star in stars:
        # Move star from right to left
        star['x'] -= star['speed']
        # If star moves off screen, reset it to the right
        if star['x'] < 0:
            star['x'] = SCREEN_WIDTH
            star['y'] = random.randint(0, SCREEN_HEIGHT)

def draw_stars(screen, stars):
    for star in stars:
        pygame.draw.circle(
            screen,
            star['color'],
            (int(star['x']), int(star['y'])),
            star['size']
        )

# Load game assets
player_image = load_image('player_ship.png')
enemy_image = load_image('enemy_ship.png')
bullet_image = load_image('bullet.png', (53, 5))

def create_player():
    return {
        'rect': pygame.Rect(50, SCREEN_HEIGHT // 2, 40, 40),
        'speed': PLAYER_SPEED,
        'bullets': [],
        'image': player_image
    }

def create_enemy():
    return {
        'rect': pygame.Rect(
            SCREEN_WIDTH,
            random.randint(0, SCREEN_HEIGHT - 40),
            40, 40
        ),
        'speed': ENEMY_SPEED,
        'image': enemy_image
    }

def create_bullet(player):
    return {
        'rect': pygame.Rect(
            player['rect'].right,
            player['rect'].centery - 2,
            10, 4
        ),
        'speed': BULLET_SPEED,
        'image': bullet_image
    }

def handle_input(player):
    keys = pygame.key.get_pressed()
    
    # Vertical movement
    if keys[pygame.K_UP] and player['rect'].top > 0:
        player['rect'].y -= player['speed']
    if keys[pygame.K_DOWN] and player['rect'].bottom < SCREEN_HEIGHT:
        player['rect'].y += player['speed']
    
    # Shooting
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player['bullets'].append(create_bullet(player))
    return True

def update_game_state(player, enemies):
    # Update bullet positions
    for bullet in player['bullets'][:]:
        bullet['rect'].x += bullet['speed']
        if bullet['rect'].left > SCREEN_WIDTH:
            player['bullets'].remove(bullet)
    
    # Update enemy positions
    for enemy in enemies[:]:
        enemy['rect'].x -= enemy['speed']
        if enemy['rect'].right < 0:
            enemies.remove(enemy)
    
    # Check for collisions
    for enemy in enemies[:]:
        for bullet in player['bullets'][:]:
            if enemy['rect'].colliderect(bullet['rect']):
                enemies.remove(enemy)
                player['bullets'].remove(bullet)
                break

def draw_game(screen, player, enemies, stars):
    screen.fill(BLACK)
    
    # Draw stars in background
    draw_stars(screen, stars)
    
    # Draw player
    screen.blit(player['image'], player['rect'])
    
    # Draw bullets
    for bullet in player['bullets']:
        screen.blit(bullet['image'], bullet['rect'])
    
    # Draw enemies
    for enemy in enemies:
        screen.blit(enemy['image'], enemy['rect'])
    
    pygame.display.flip()

def main():
    player = create_player()
    enemies = []
    stars = create_stars()
    enemy_spawn_timer = 0
    running = True
    
    while running:
        # Handle input
        running = handle_input(player)
        
        # Spawn enemies
        enemy_spawn_timer += 1
        if enemy_spawn_timer >= FPS:
            enemies.append(create_enemy())
            enemy_spawn_timer = 0
        
        # Update game state
        update_game_state(player, enemies)
        update_stars(stars)
        
        # Draw everything
        draw_game(screen, player, enemies, stars)
        
        # Control game speed
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()