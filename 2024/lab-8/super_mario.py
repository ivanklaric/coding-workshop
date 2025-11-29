import pygame
import sys
from mario_lib import *
from mario_levels import *
from character_lib import *
from mario_character import * 

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
super_mario = MarioCharacter(100, 100, 0, 0, 3, 'lab-8/mario.png', ['lab-8/mario_w1.png', 'lab-8/mario_w2.png', 'lab-8/mario_w3.png'], 'lab-8/mario_jump.png')
evil_turtle = Turtle(300, 100, -2, 0, 3,'lab-8/turtle.png', ['lab-8/turtle.png'], 'lab-8/turtle.png', 32, 32)
evil_turtle_flip = Turtle(300, 150, 2, 0, 3,'lab-8/turtle.png', ['lab-8/turtle.png'], 'lab-8/turtle.png', 32, 32)
kolona_pocetka = 0

turtle_list = [evil_turtle,evil_turtle_flip]

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    super_mario.walk_stop()
    if keys[pygame.K_LEFT]:
        super_mario.walk_left()
    if keys[pygame.K_RIGHT]:
        super_mario.walk_right()
    if keys[pygame.K_SPACE]:
        super_mario.jump()
    super_mario.update_character_state()

    for turtle in turtle_list:
        turtle.update_character_state()
        turtle.apply_gravity(polje, kolona_pocetka)
        turtle.turnTowardsMario(super_mario)
        turtle.move(polje, kolona_pocetka)

    super_mario.apply_gravity(polje, kolona_pocetka)

    # move mario according to speed_x and speed_y
    super_mario.move(polje, kolona_pocetka)    
    # move turtle according to speed_x and speed_y
    
    
        
    

    screen.fill((80, 163, 255))
 
    score_text = font.render('Score: ' + str(score), True, (0, 0, 0))
    screen.blit(score_text, (0,0))
    nacrtaj_polje(screen, lista_slika, polje, kolona_pocetka)
    
    super_mario.draw(screen)

    for turtle in turtle_list:
        turtle.draw(screen)
   
    
    pygame.display.flip()
    # Cap the frame rate
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()
sys.exit()