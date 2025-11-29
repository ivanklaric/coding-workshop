import pygame
import random
import sys

# Initialize Pygame
pygame.init()
pygame.mixer.init()


# Set up the game window
WIDTH, HEIGHT = 800, 600
BOJA_STUPOVA = (49, 122, 17)
BOJA_PTICE = (252, 190, 45)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy bird")

# Set up fonts
font = pygame.font.SysFont('Arial', 24)

pygame.mixer.music.load('lab-7/background.mp3')
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1)

def napravi_stup(x):
    return {
        'x': x,
        'yg': random.randint(50,490),
        'hole_height': 200,
        'width': 50
    }

def napravi_oblak(x):
    return {
        'x': x,
        'y': random.randint(0, HEIGHT-100),
        'speed': random.randint(15, 20) / 10
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

def nacrtaj_oblak(screen, oblak, slika):
    screen.blit(slika, (oblak['x'], oblak['y']))

slika_ptice = ucitaj_sliku("lab-7/bird2.png")
zvuk_krila = pygame.mixer.Sound("lab-7/woosh.mp3")
scream = pygame.mixer.Sound("lab-7/scream.wav")
slika_oblaka = ucitaj_sliku("lab-7/big-cloud.png")

stupovi = [napravi_stup(250), napravi_stup(500), napravi_stup(750)]
oblaci = [napravi_oblak(100), napravi_oblak(200), napravi_oblak(300), napravi_oblak(500), napravi_oblak(600), napravi_oblak(700)]
ptica = {
    'x': 20,
    'y': HEIGHT//2-15,
    'speed': 0
}
gravitacija = 0.1
impuls = -2.5

# Main game loop
score = 0
speed = 1
running = True
game_over = False
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if not game_over:
            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_SPACE]:
                    ptica['speed'] += impuls
                    zvuk_krila.play()


    if not game_over:
        # Pomakni oblake u lijevo
        for oblak in oblaci:
            oblak['x'] -= oblak['speed']
        # Pomakni stupove u lijevo
        for stup in stupovi:
            stup['x'] -= speed
        
        # Ako je prvi oblak nestao s ekrana, makni ga i dodaj jedan stup na kraj
        if oblaci[0]['x'] <= 50 and len(oblaci)<7:
            oblaci.append(napravi_oblak(800))
        if oblaci[0]['x'] <= -50:
            oblaci = oblaci[1:] 

        # Ako je prvi stup nestao s ekrana, makni ga i dodaj jedan stup na kraj
        if stupovi[0]['x'] <= 50 and len(stupovi)<4:
            stupovi.append(napravi_stup(800))
        if stupovi[0]['x'] <= -50:
            stupovi = stupovi[1:]
            score += 1

        ptica['y'] += ptica['speed']
        ptica['speed'] += gravitacija
        if ptica['y'] < 15:
            ptica['y'] = 15
            ptica['speed'] = 0
        if ptica['y'] > HEIGHT-15:
            ptica['y'] = HEIGHT-15
            ptica['speed'] = 0

        prvi_stup = stupovi[0]
        ptica_rect = pygame.Rect(ptica['x'], ptica['y'], 35, 25)
        gornja_cijev = (prvi_stup['x'], 0, prvi_stup['width'], prvi_stup['yg'])
        donja_cijev = (prvi_stup['x'], prvi_stup['yg']+prvi_stup['hole_height'], prvi_stup['width'], HEIGHT-prvi_stup['yg']-prvi_stup['hole_height'])
        if pygame.Rect.colliderect( ptica_rect, gornja_cijev) or pygame.Rect.colliderect(ptica_rect, donja_cijev):
            game_over = True
            scream.play()

    # Nacrtaj scenu
    screen.fill((80, 163, 255))
    # Nacrtaj oblake
    for oblak in oblaci:
        nacrtaj_oblak(screen, oblak, slika_oblaka)
    # Nacrtaj stupove
    for stup in stupovi:
        nacrtaj_stup(screen, stup)
    score_text = font.render('Score: ' + str(score), True, (0, 0, 0))
    screen.blit(score_text, (0,0))
    slika_za_nacrtati = pygame.transform.rotate(slika_ptice, ptica['speed'] * (-5))
    nacrtaj_pticu(screen, ptica, slika_za_nacrtati)

    if game_over:
        game_over_text = font.render('Game Over!', True, (0, 0, 0))
        screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2))
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)


# Quit Pygame
pygame.quit()
sys.exit()
