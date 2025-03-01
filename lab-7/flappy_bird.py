import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Set up the game window
WIDTH, HEIGHT = 800, 600
BOJA_STUPOVA = (49, 122, 17)
BOJA_PTICE = (252, 190, 45)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy bird")

# Set up fonts
font = pygame.font.SysFont('Arial', 24)

def napravi_stup(x):
    return {
        'x': x,
        'yg': random.randint(50,490),
        'hole_height': 120,
        'width': 50
    }

def nacrtaj_stup(screen, stup):
    # Prvo, nacrtaj gornji stup
    pygame.draw.rect(screen, BOJA_STUPOVA, (stup['x'], 0, stup['width'], stup['yg']))
    # Onda, nacrtaj donji stup
    pygame.draw.rect(screen, BOJA_STUPOVA, (stup['x'], stup['yg'] + stup['hole_height'], stup['width'], HEIGHT-stup['yg'] - stup['hole_height']))

def ucitaj_sliku(filename, size=(40, 30)):
    image = pygame.image.load(filename)
    return pygame.transform.scale(image, size)


def nacrtaj_pticu(screen, ptica, slika_ptice):
    screen.blit(slika_ptice, (ptica['x'], ptica['y']))

slika_ptice = ucitaj_sliku("lab-7/bird2.png")
stupovi = [napravi_stup(250), napravi_stup(500), napravi_stup(750)]
ptica = {
    'x': 20,
    'y': HEIGHT//2-15,
    'speed': 0
}
gravitacija = 0.1
impuls = -2.5

# Main game loop
speed = 1
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                ptica['speed'] += impuls


    # Pomakni stupove u lijevo
    for stup in stupovi:
        stup['x'] -= speed
    # Ako je prvi stup nestao s ekrana, makni ga i dodaj jedan stup na kraj
    if stupovi[0]['x'] <= 50 and len(stupovi)<4:
        stupovi.append(napravi_stup(800))
    if stupovi[0]['x'] <= -50:
        stupovi = stupovi[1:]

    ptica['y'] += ptica['speed']
    ptica['speed'] += gravitacija
    if ptica['y'] < 15:
        ptica['y'] = 15
        ptica['speed'] = 0
    if ptica['y'] > HEIGHT-15:
        ptica['y'] = HEIGHT-15
        ptica['speed'] = 0

    # Nacrtaj scenu
    screen.fill((80, 163, 255))
    # Draw the score in the upper left corner
    # Nacrtaj stupove
    for stup in stupovi:
        nacrtaj_stup(screen, stup)
    score_text = font.render('Score: XX', True, (0, 0, 0))
    screen.blit(score_text, (0,0))
    nacrtaj_pticu(screen, ptica, slika_ptice)
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
