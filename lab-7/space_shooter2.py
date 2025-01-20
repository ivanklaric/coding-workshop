import pygame
import random

SIRINA_EKRANA = 800
VISINA_EKRANA = 800

pygame.init()
screen = pygame.display.set_mode((SIRINA_EKRANA, VISINA_EKRANA))
pygame.display.set_caption('Space shooter!')
game_over = False

BOJE_ZVIJEZDA = [
    (255, 255, 255),
    (200, 200, 200),
    (150, 150, 150)
]

FPS = 30

def napravi_zvijezdu():
    return {
        'x': random.randint(0, 800),
        'y': random.randint(0, 800),
        'velicina': random.randint(1, 3),
        'boja': BOJE_ZVIJEZDA[ random.randint(0,2)],
        'brzina': random.uniform(-0.3, -0.01)
    }

def nacrtaj_zvijezdu(zvijezda):
    pygame.draw.circle(screen, zvijezda['boja'], (zvijezda['x'], zvijezda['y']), zvijezda['velicina'])

def pomakni_zvijezde(zvijezde):
    for i in range(len(zvijezde)):
        zvijezde[i]['x'] = zvijezde[i]['x'] + zvijezde[i]['brzina']
        if zvijezde[i]['x'] < 0:
            zvijezde[i] = napravi_zvijezdu()
            zvijezde[i]['x'] = 800

zvijezde = []
for i in range(100):
    zvijezde.append(napravi_zvijezdu())
zadnje_osvjezavanje = 0

while not game_over:   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    trenutno_vrijeme = pygame.time.get_ticks()
    proslo_vremena = trenutno_vrijeme - zadnje_osvjezavanje

    if proslo_vremena > 1000 // FPS:
        pomakni_zvijezde(zvijezde)
        screen.fill((0, 0, 0))
        for i in range(len(zvijezde)):
            nacrtaj_zvijezdu(zvijezde[i])
        pygame.display.update()

pygame.quit()