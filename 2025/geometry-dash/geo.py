import pygame
import random

def are_they_clashing(player, spike):
    player_rect = player['image'].get_rect(topleft=(player['x'], player['y']))
    spike_rect = spike['image'].get_rect(topleft=(spike['x'], spike['y']))
    return player_rect.colliderect(spike_rect)

# Initialize pygame
pygame.init()

# Create a window
screen = pygame.display.set_mode((1024, 768))
pygame.display.set_caption("Geometry Dash")

background = pygame.image.load("img/background.png")
background_left_x = 0
time_since_background_move = pygame.time.get_ticks()

GRAVITY = 4
JUMP_VELOCITY = -40
SCREEN_SPEED = 16
ROTATION_SPEED = -5
player = {
    'image': pygame.image.load("img/player.png"),
    'x': 256,
    'y': 644,
    'speed_y': 0,
    'rotation_angle': 0
}
level = [
    {
        'image': pygame.image.load("img/spike.png"),
        'x': 600,
        'y': 644,
        'type': 'spike'
    },
    {
        'image': pygame.image.load("img/spike.png"),
        'x': 1700,
        'y': 644,
        'type': 'spike'
    },
    {
        'image': pygame.image.load("img/block.png"),
        'x': 1200,
        'y': 644,
        'type': 'block'
    },
    {
        'image': pygame.image.load("img/block.png"),
        'x': 1264,
        'y': 644,
        'type': 'block'
    },

]

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
    
    # If needed, draw the new screen state
    if pygame.time.get_ticks() - time_since_background_move > 40:
        background_left_x -= SCREEN_SPEED
        for element in level:
            element['x'] -= SCREEN_SPEED
        # Move the player
        player['speed_y'] += GRAVITY
        player['y'] += player['speed_y']
        player['rotation_angle'] += ROTATION_SPEED
        time_since_background_move = pygame.time.get_ticks()
        if player['y'] >= 644:
            player['y'] = 644
            player['speed_y'] = 0
            player['rotation_angle'] = round(player['rotation_angle'] / 90) * 90
        
        for element in level:
            if are_they_clashing(player, element):
                if element['type'] == 'spike':
                    running = False
                if element['type'] == 'block' and player['y'] < 644:
                    player['speed_y'] = 0
                    player['y'] = 580
                    player['rotation_angle'] = round(player['rotation_angle'] / 90) * 90
                    print("here!")


    if background_left_x <= -1024:
        background_left_x = 0



    # Draw the background
    screen.blit(background, (background_left_x, 0))
    screen.blit(background, (background_left_x+1024, 0))
    for element in level:
        screen.blit(element['image'], (element['x'], element['y']))
    # Draw the player
    rotated_player = pygame.transform.rotate(player['image'], player['rotation_angle'])
    screen.blit(rotated_player, (player['x'], player['y']))

    pygame.display.flip()

pygame.quit()