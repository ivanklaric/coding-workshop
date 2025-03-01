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
        'hole_height': 60,
        'width': 50
    }

def nacrtaj_stup(screen, stup):
    # Prvo, nacrtaj gornji stup
    pygame.draw.rect(screen, BOJA_STUPOVA, (stup['x'], 0, stup['width'], stup['yg']))
    # Onda, nacrtaj donji stup
    pygame.draw.rect(screen, BOJA_STUPOVA, (stup['x'], stup['yg'] + stup['hole_height'], stup['width'], HEIGHT-stup['yg'] - stup['hole_height']))

def nacrtaj_pticu(screen, ptica):
    pygame.draw.circle(screen, BOJA_PTICE, (ptica['x'], ptica['y']), 15)

stupovi = [napravi_stup(250), napravi_stup(500), napravi_stup(750)]
ptica = {
    'x': 20,
    'y': HEIGHT//2-15
}

# Main game loop
speed = 1
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Pomakni stupove u lijevo
    for stup in stupovi:
        stup['x'] -= speed
    # Ako je prvi stup nestao s ekrana, makni ga i dodaj jedan stup na kraj
    if stupovi[0]['x'] <= 50 and len(stupovi)<4:
        stupovi.append(napravi_stup(800))
    if stupovi[0]['x'] <= -50:
        stupovi = stupovi[1:]


    # Drawing the scene
    screen.fill((80, 163, 255))
    # Draw the score in the upper left corner
    # Nacrtaj stupove
    for stup in stupovi:
        nacrtaj_stup(screen, stup)
    score_text = font.render('Score: XX', True, (0, 0, 0))
    screen.blit(score_text, (0,0))
    nacrtaj_pticu(screen, ptica)
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
