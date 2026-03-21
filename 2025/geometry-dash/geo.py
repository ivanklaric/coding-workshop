import pygame

# Initialize pygame
pygame.init()

# Create a window
screen = pygame.display.set_mode((1024, 768))
pygame.display.set_caption("Geometry Dash")

background = pygame.image.load("img/background.png")
background_left_x = 0
time_since_background_move = pygame.time.get_ticks()

GRAVITY = 1
JUMP_VELOCITY = -15
SCREEN_SPEED = 8
player = {
    'image': pygame.image.load("img/player.png"),
    'x': 256,
    'y': 644,
    'speed_y': 0
}

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player['speed_y'] = JUMP_VELOCITY
    
    # If needed, move the background
    if pygame.time.get_ticks() - time_since_background_move > 40:
        background_left_x -= SCREEN_SPEED
        # Move the player
        player['speed_y'] += GRAVITY
        player['y'] += player['speed_y']
        time_since_background_move = pygame.time.get_ticks()
    if background_left_x <= -1024:
        background_left_x = 0
    # Draw the background
    screen.blit(background, (background_left_x, 0))
    screen.blit(background, (background_left_x+1024, 0))
    # Draw the player
    screen.blit(player['image'], (player['x'], player['y']))

    pygame.display.flip()

pygame.quit()