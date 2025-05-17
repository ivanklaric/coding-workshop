import pygame
import sys
from mario_lib import *
from mario_levels import *
from character_lib import *

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 512
BROJ_REDAKA, BROJ_STUPACA = 32, 50
GRAVITACIJA = 0.2

polje = second_level()

pygame.init()
font = pygame.font.SysFont('Arial', 24)
pygame.display.set_caption("Super Mario!")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))     
score = 0
running = True
lista_slika = ucitaj_sve_slike()
mario = initialize_character(100, 100, 0, 0, 3, 'lab-8/mario.png', ['lab-8/mario_w1.png', 'lab-8/mario_w2.png', 'lab-8/mario_w3.png'], 'lab-8/mario_jump.png')
kolona_pocetka = 0
turtle = initialize_character(300,100,-2,0,3,'lab-8/turtle.png',['lab-8/turtle.png'],'lab-8/turtle.png',32,32)

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    mario['speed_x'] = 0
    if keys[pygame.K_LEFT]:
        mario['speed_x'] = -4
    if keys[pygame.K_RIGHT]:
        mario['speed_x'] = 4
    if keys[pygame.K_SPACE]:
        mario['speed_y'] -= mario['jump_impulse']

    mario['state'] = STATE_STANDING
    if mario['speed_x'] != 0:
        mario['state'] = STATE_WALKING
    if mario['speed_y'] != 0:
        mario['state'] = STATE_JUMP

    turtle['state'] = STATE_STANDING
    if turtle['speed_x'] != 0:
        turtle['state'] = STATE_WALKING
    if turtle['speed_y'] != 0:
        turtle['state'] = STATE_JUMP

    # upali gravitaciju
    if can_character_move_to(mario, polje, kolona_pocetka, mario['x'], mario['y'] + GRAVITACIJA):
        mario['speed_y'] += GRAVITACIJA
        mario['jump_impulse'] = 0
    else:
        mario['jump_impulse'] = 3
    # upali gravitaciju za turtle
    if can_character_move_to(turtle, polje, kolona_pocetka,turtle['x'], turtle['y'] + GRAVITACIJA):
        turtle['speed_y'] += GRAVITACIJA


    # move mario according to speed_x and speed_y
    mario_next_x = mario['x'] + mario['speed_x']
    mario_next_y = mario['y'] + mario['speed_y']
    if can_character_move_to(mario, polje, kolona_pocetka, mario_next_x, mario['y']):
        mario['x'] += mario['speed_x']
    else:
        (mario_row, mario_col) = what_row_col_is_character_in(mario, kolona_pocetka)
        if polje[mario_row][mario_col+1] == 5 and mario['speed_x'] > 0:
            score += 1
            polje[mario_row][mario_col+1] = 0
        if polje[mario_row][mario_col-1] == 5 and mario['speed_x'] < 0:
            score += 1
            polje[mario_row][mario_col-1] = 0
        mario['speed_x'] = 0

    if can_character_move_to(mario, polje, kolona_pocetka, mario['x'], mario_next_y):
        mario['y'] += mario['speed_y']
    else:
        (mario_row, mario_col) = what_row_col_is_character_in(mario, kolona_pocetka)
        if mario_row > 1 and mario['speed_y'] < 0:
            # check for questionmark boxes
            if polje[mario_row-1][mario_col] == 3:
                polje[mario_row-1][mario_col] = 4
            if polje[mario_row-1][mario_col+1] == 3:
                polje[mario_row-1][mario_col+1] = 4
            if polje[mario_row-1][mario_col-1] == 3:
                polje[mario_row-1][mario_col-1] = 4
            # check for coins
            if polje[mario_row-1][mario_col] == 5: # coin hit
                score += 1
                polje[mario_row-1][mario_col] = 0
        elif mario['speed_y'] > 0:
            if polje[mario_row+1][mario_col] == 5: # coin hit
                score += 1
                polje[mario_row+1][mario_col] = 0
        mario['speed_y'] = 0        
    # move turtle according to speed_x and speed_y
    turtle_next_x = turtle['x'] + turtle['speed_x']
    turtle_next_y = turtle['y'] + turtle['speed_y']
    if can_character_move_to(turtle, polje, kolona_pocetka, turtle_next_x, turtle['y']):
        turtle['x'] += turtle['speed_x']

    if can_character_move_to(turtle, polje, kolona_pocetka, turtle['x'],turtle_next_y):
        turtle['y'] += turtle['speed_y']

    screen.fill((80, 163, 255))
 
    score_text = font.render('Score: ' + str(score), True, (0, 0, 0))
    screen.blit(score_text, (0,0))
    nacrtaj_polje(screen, lista_slika, polje, kolona_pocetka)
    
    draw_character(screen, mario) 
    draw_character(screen, turtle)   
    
    pygame.display.flip()
    # Cap the frame rate
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()
sys.exit()