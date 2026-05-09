import pygame
import random

def are_they_clashing(player, spike):
    player_rect = player['image'].get_rect(topleft=(player['x'], player['y']))
    spike_rect = spike['image'].get_rect(topleft=(spike['x'], spike['y']))
    return player_rect.colliderect(spike_rect)

# Initialize pygame
pygame.init()

# Create a window
font = pygame.font.SysFont("Comics Sans", 48)
screen = pygame.display.set_mode((1024, 768))
pygame.display.set_caption("Geometry Dash")

background = pygame.image.load("img/background.png")
background_left_x = 0
time_since_background_move = pygame.time.get_ticks()

GRAVITY = 4
JUMP_VELOCITY = -43
SCREEN_SPEED = 16
ROTATION_SPEED = -5
player = {
    'image': pygame.image.load("img/player.png"),
    'x': 256,
    'y': 644,
    'speed_y': 0,
    'rotation_angle': 0
}

def reset_level():
    return [
    # Warm-up: single spike
    {'image': pygame.image.load("img/spike.png"), 'x': 700, 'y': 644, 'type': 'spike'},

    # Two spikes close together (one jump clears both)
    {'image': pygame.image.load("img/spike.png"), 'x': 1300, 'y': 644, 'type': 'spike'},
    {'image': pygame.image.load("img/spike.png"), 'x': 1364, 'y': 644, 'type': 'spike'},

    # Block platform to jump onto, with a spike right after
    {'image': pygame.image.load("img/block.png"), 'x': 2000, 'y': 644, 'type': 'block'},
    {'image': pygame.image.load("img/block.png"), 'x': 2064, 'y': 644, 'type': 'block'},
    {'image': pygame.image.load("img/spike.png"), 'x': 2300, 'y': 644, 'type': 'spike'},

    # Spike trio - need a well-timed jump
    {'image': pygame.image.load("img/spike.png"), 'x': 2900, 'y': 644, 'type': 'spike'},
    {'image': pygame.image.load("img/spike.png"), 'x': 2964, 'y': 644, 'type': 'spike'},
    {'image': pygame.image.load("img/spike.png"), 'x': 3028, 'y': 644, 'type': 'spike'},

    # Block staircase leading up
    {'image': pygame.image.load("img/block.png"), 'x': 3700, 'y': 644, 'type': 'block'},
    {'image': pygame.image.load("img/block.png"), 'x': 3764, 'y': 644, 'type': 'block'},
    {'image': pygame.image.load("img/block.png"), 'x': 3828, 'y': 644, 'type': 'block'},

    # Gap, then another platform
    {'image': pygame.image.load("img/block.png"), 'x': 4300, 'y': 644, 'type': 'block'},

    # Spike right after landing - quick reaction needed
    {'image': pygame.image.load("img/spike.png"), 'x': 4600, 'y': 644, 'type': 'spike'},

    # Long spike field - the climax
    {'image': pygame.image.load("img/spike.png"), 'x': 5300, 'y': 644, 'type': 'spike'},
    {'image': pygame.image.load("img/spike.png"), 'x': 5364, 'y': 644, 'type': 'spike'},
    {'image': pygame.image.load("img/block.png"), 'x': 5500, 'y': 644, 'type': 'block'},
    {'image': pygame.image.load("img/spike.png"), 'x': 5700, 'y': 644, 'type': 'spike'},
    {'image': pygame.image.load("img/spike.png"), 'x': 5764, 'y': 644, 'type': 'spike'},

    # Victory stretch - a couple final spikes
    {'image': pygame.image.load("img/spike.png"), 'x': 6500, 'y': 644, 'type': 'spike'},
    {'image': pygame.image.load("img/spike.png"), 'x': 7100, 'y': 644, 'type': 'spike'},
    {'image': pygame.image.load("img/spike.png"), 'x': 7164, 'y': 644, 'type': 'spike'},
]

level = reset_level()

game_over = False
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_over:
                game_over = False
                background_left_x = 0
                player['x'] = 256
                player['y'] = 644
                level = reset_level()
                continue
            if event.key == pygame.K_SPACE and player['y'] in (644, 580):
                player['speed_y'] = JUMP_VELOCITY
        if event.type == pygame.MOUSEBUTTONDOWN and player['y'] in (644, 580):
            player['speed_y'] = JUMP_VELOCITY
    
    if game_over:
        # Draw the score
        text = font.render("Game Over!", True, "WHITE")
        screen.blit(text, (500, 300))
        pygame.display.flip()
        continue

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
                if element['type'] == 'spike' or element['type'] == 'block' and player['y'] == 644:
                    game_over = True
                if element['type'] == 'block' and player['y'] < 644:
                    player['speed_y'] = 0
                    player['y'] = 580
                    player['rotation_angle'] = round(player['rotation_angle'] / 90) * 90
                


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