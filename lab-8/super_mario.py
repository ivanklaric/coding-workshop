import pygame
import sys
from mario_lib import *
from mario_levels import *

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 512
BROJ_REDAKA, BROJ_STUPACA = 32, 50

polje = second_level()

pygame.init()
font = pygame.font.SysFont('Arial', 24)
pygame.display.set_caption("Super Mario!")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
score = 0
running = True
lista_slika = ucitaj_sve_slike()
kolona_pocetka = 0

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                kolona_pocetka -= 1
            if keys[pygame.K_RIGHT]:
                kolona_pocetka += 1
            

    screen.fill((80, 163, 255))
 
    score_text = font.render('Score: ' + str(score), True, (0, 0, 0))
    screen.blit(score_text, (0,0))

    nacrtaj_polje(screen, lista_slika, polje, kolona_pocetka)
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)


# Quit Pygame
pygame.quit()
sys.exit()