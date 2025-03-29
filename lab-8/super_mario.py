import pygame
import sys
from mario_lib import *

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 512
BROJ_REDAKA, BROJ_STUPACA = 32, 50

polje = inicijaliziraj_polje(BROJ_REDAKA, BROJ_STUPACA)
polje = napravi_ravnicu(polje)
polje[10][10] = 1

pygame.init()
font = pygame.font.SysFont('Arial', 24)
pygame.display.set_caption("Super Mario!")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
score = 0
running = True

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((80, 163, 255))
 
    score_text = font.render('Score: ' + str(score), True, (0, 0, 0))
    screen.blit(score_text, (0,0))

    nacrtaj_polje(screen, polje)
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)


# Quit Pygame
pygame.quit()
sys.exit()