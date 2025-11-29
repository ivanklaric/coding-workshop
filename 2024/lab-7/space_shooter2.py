import os
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

def ucitaj_sliku(filename, size=(40, 40)):
    try:
        # Get the directory where the script/binary is located
        script_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(script_dir, "assets", filename)
        image = pygame.image.load(image_path)
        return pygame.transform.scale(image, size)
    except pygame.error as e:
        print(f"Couldn't load image {filename}: {e}")
        # Create a colored rectangle as fallback
        surface = pygame.Surface(size)
        surface.fill((255, 255, 255))
        return surface

def napravi_neprijatelja():
    return {
        'x': SIRINA_EKRANA-50,
        'y': random.randint(0,VISINA_EKRANA-50),
        'slika': ucitaj_sliku("enemy_ship.png", (45, 26)),
        'w': 45,
        'h': 26,
        'brzina': random.uniform(-0.1, -0.01)
    }

def napravi_brod():
    return {
        'x': 50,
        'y': VISINA_EKRANA // 2,
        'slika': ucitaj_sliku("player_ship.png", (71, 26)),
        'w': 71,
        'h': 26,
        'health': 100
    }

def napravi_metak(x, y):
    return {
        'x': x,
        'y': y,
        'slika': ucitaj_sliku("bullet.png", (53, 5)),
        'w': 53,
        'h': 5,
        'brzina': 0.4
    }

def nacrtaj_sliku(brod):
    screen.blit(brod['slika'], (brod['x'], brod['y'], 47, 17))

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

def pomakni_letala(letala):
    for i in range(len(letala)):
        letala[i]['x'] = letala[i]['x'] + letala[i]['brzina']
    letala = list(
        filter(lambda letalo: letalo['x'] <= SIRINA_EKRANA and letalo['x'] >= 0, 
               letala))

# rectovi sadrzi x, y, w, h
def preklapaju_li_se( rect1, rect2):
    if rect2['x'] >= rect1['x'] and rect2['x'] <= rect1['x'] + rect1['w']:
        if rect2['y'] >= rect1['y'] and rect2['y'] <= rect1['y'] + rect1['h']:
            return True
        if rect1['y'] >= rect2['y'] and rect1['y'] <= rect2['y'] + rect2['h']:
            return True
        
    if rect1['x'] >= rect2['x'] and rect1['x'] <= rect2['x'] + rect1['w']:
        if rect2['y'] >= rect1['y'] and rect2['y'] <= rect1['y'] + rect1['h']:
            return True
        if rect1['y'] >= rect2['y'] and rect1['y'] <= rect2['y'] + rect2['h']:
            return True
    
    return False

def detektiraj_sudare(metci, neprijatelji):
    for i in range(len(metci)):
        for j in range(len(neprijatelji)):
            if preklapaju_li_se( metci[i], neprijatelji[j]):
                metci[i]['x'] = 1000
                neprijatelji[j]['x'] = -100

zvijezde = []
for i in range(100):
    zvijezde.append(napravi_zvijezdu())
zadnje_osvjezavanje = 0

metci = []
neprijatelji = [ napravi_neprijatelja(), 
                napravi_neprijatelja(), 
                napravi_neprijatelja()]
vrijeme_zadnjeg_neprijatelja = 0

moj_brod = napravi_brod()

while not game_over:   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            metci.append(napravi_metak( moj_brod['x'], moj_brod['y'] ))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_DOWN] and moj_brod['y'] <= VISINA_EKRANA-40:
        moj_brod['y'] = moj_brod['y'] + 1
    if keys[pygame.K_UP] and moj_brod['y'] >= 4:
        moj_brod['y'] = moj_brod['y'] - 1
    if keys[pygame.K_RIGHT] and moj_brod['x'] <= SIRINA_EKRANA-40:
        moj_brod['x'] = moj_brod['x'] + 1
    if keys[pygame.K_LEFT] and moj_brod['x'] >= 1:
        moj_brod['x'] = moj_brod['x'] - 1


    trenutno_vrijeme = pygame.time.get_ticks()
    proslo_vremena = trenutno_vrijeme - zadnje_osvjezavanje

    if proslo_vremena > 1000 // FPS:
        broj_sekundi_od_zadnjeg_neprijatelja = (trenutno_vrijeme - vrijeme_zadnjeg_neprijatelja) // 1000
        if len(neprijatelji) < 10 and random.randint(0,100) < broj_sekundi_od_zadnjeg_neprijatelja:
            neprijatelji.append(napravi_neprijatelja()) 
            vrijeme_zadnjeg_neprijatelja = trenutno_vrijeme


        pomakni_zvijezde(zvijezde)
        pomakni_letala(metci)
        pomakni_letala(neprijatelji)
        detektiraj_sudare(metci, neprijatelji)

        screen.fill((0, 0, 0))
        for i in range(len(zvijezde)):
            nacrtaj_zvijezdu(zvijezde[i])
        for i in range(len(metci)):
            nacrtaj_sliku(metci[i])
        for i in range(len(neprijatelji)):
            nacrtaj_sliku(neprijatelji[i])
        nacrtaj_sliku(moj_brod)
        pygame.display.update()

pygame.quit()