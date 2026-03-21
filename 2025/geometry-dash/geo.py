import pygame

# Initialize pygame
pygame.init()

# Create a window
screen = pygame.display.set_mode((1024, 768))
pygame.display.set_caption("Geometry Dash")

background = pygame.image.load("img/background.png")
background_left_x = 0
time_since_background_move = pygame.time.get_ticks()

GRAVITY = 2.5
JUMP_VELOCITY = -30
SCREEN_SPEED = 8
ROTATION_SPEED = -6
player = {
    'image': pygame.image.load("img/player.png"),
    'x': 256,
    'y': 644,
    'speed_y': 0,
    'rotation_angle': 0
}

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and player['y'] == 644:
                player['speed_y'] = JUMP_VELOCITY
        if event.type == pygame.MOUSEBUTTONDOWN and player['y'] == 644:
            player['speed_y'] = JUMP_VELOCITY
    
    # If needed, move the background
    if pygame.time.get_ticks() - time_since_background_move > 40:
        background_left_x -= SCREEN_SPEED
        # Move the player
        player['speed_y'] += GRAVITY
        player['y'] += player['speed_y']
        player['rotation_angle'] += ROTATION_SPEED
        time_since_background_move = pygame.time.get_ticks()
        if player['y'] >= 644:
            player['y'] = 644
            player['speed_y'] = 0
            player['rotation_angle'] = round(player['rotation_angle'] / 90) * 90

    if background_left_x <= -1024:
        background_left_x = 0
    # Draw the background
    screen.blit(background, (background_left_x, 0))
    screen.blit(background, (background_left_x+1024, 0))
    # Draw the player
    rotated_player = pygame.transform.rotate(player['image'], player['rotation_angle'])
    screen.blit(rotated_player, (player['x'], player['y']))

    pygame.display.flip()

pygame.quit()