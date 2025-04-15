import pygame
import sys
from mario_lib import *
from mario_levels import *
from character_lib import *

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 512
BROJ_REDAKA, BROJ_STUPACA = 32, 50
GRAVITACIJA = 0.2
promjena_u_mogućnosti_pomicanja_charactera = True

polje = second_level()

pygame.init()
font = pygame.font.SysFont('Arial', 24)
pygame.display.set_caption("Super Mario!")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))     
score = 0
running = True
lista_slika = ucitaj_sve_slike()
mario = initialize_character(100, 100, 0, 0, 3, 'lab-8/mario.png')
kolona_pocetka = 0

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

    # upali gravitaciju
    if can_character_move_to(mario, polje, kolona_pocetka, mario['x'], mario['y'] + GRAVITACIJA):
        mario['speed_y'] += GRAVITACIJA
        mario['jump_impulse'] = 0
    else:
        mario['jump_impulse'] = 3

    mario_next_x = mario['x'] + mario['speed_x']
    mario_next_y = mario['y'] + mario['speed_y']

    if can_character_move_to(mario, polje, kolona_pocetka, mario_next_x, mario['y']):
        mario['x'] += mario['speed_x']
    else:
        mario['speed_x'] = 0
        if promjena_u_mogućnosti_pomicanja_charactera != can_character_move_to(mario, polje, kolona_pocetka, mario_next_x, mario['y']):
            mario['speed_y'] = 0
        else:
            promjena_u_mogućnosti_pomicanja_charactera = can_character_move_to(mario, polje, kolona_pocetka, mario_next_x, mario['y'])

    if can_character_move_to(mario, polje, kolona_pocetka, mario['x'], mario_next_y):
        mario['y'] += mario['speed_y']
    else:
        mario['speed_y'] = 0
        if promjena_u_mogućnosti_pomicanja_charactera != can_character_move_to(mario, polje, kolona_pocetka, mario['x'], mario_next_y):
            mario['speed_x'] = 0
        else:
            promjena_u_mogućnosti_pomicanja_charactera = can_character_move_to(mario, polje, kolona_pocetka, mario['x'], mario_next_y)
        (mario_row, mario_col) = what_row_col_is_character_in(mario, kolona_pocetka)
        if mario_row > 1:
            if polje[mario_row-1][mario_col] == 3:
                polje[mario_row-1][mario_col] = 4
            if polje[mario_row-1][mario_col+1] == 3:
                polje[mario_row-1][mario_col+1] = 4
            if polje[mario_row-1][mario_col-1] == 3:
                polje[mario_row-1][mario_col-1] = 4

    screen.fill((80, 163, 255))
 
    score_text = font.render('Score: ' + str(score), True, (0, 0, 0))
    screen.blit(score_text, (0,0))
    nacrtaj_polje(screen, lista_slika, polje, kolona_pocetka)
    
    draw_character(screen, mario)    
    
    pygame.display.flip()
    # Cap the frame rate
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()
sys.exit()