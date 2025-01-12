import pygame
import random

VELICINA_BLOKA = 30
BROJ_KOLONA = 10
BROJ_REDOVA = 20
SIRINA_EKRANA = BROJ_KOLONA * VELICINA_BLOKA
VISINA_EKRANA = BROJ_REDOVA * VELICINA_BLOKA

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

BOJE = [ BLUE, RED, GREEN]

OBLICI = [
    [[1, 1, 1, 1]],  # I
    [[1, 1], [1, 1]],  # O
    [[1, 1, 1], [0, 1, 0]],  # T
    [[1, 1, 1], [1, 0, 0]],  # L
    [[1, 1, 1], [0, 0, 1]],  # J
    [[1, 1, 0], [0, 1, 1]],  # S
    [[0, 1, 1], [1, 1, 0]]   # Z
]

pygame.init()
screen = pygame.display.set_mode((SIRINA_EKRANA, VISINA_EKRANA))
pygame.display.set_caption('Tetris')

def napravi_polje():
    polje = []
    for i in range(BROJ_REDOVA):
        row = []
        for j in range(BROJ_KOLONA):
            row.append(0)
        polje.append(row)
    return polje

def napravi_novi_oblik():
    oblik = OBLICI[random.randint(0, len(OBLICI) - 1)]
    boja = random.randint(0, len(BOJE)-1)
    pozicija_kolona = BROJ_KOLONA // 2
    pozicija_red = 0
    for r in range(len(oblik)):
        for k in range(len(oblik[0])):
            if oblik[r][k] > 0:
                oblik[r][k] = boja+1
    return oblik, pozicija_kolona, pozicija_red


def smije_biti_postavljen(polje, oblik, x, y):
    for i in range(len(oblik)):
        for j in range(len(oblik[0])):
            if oblik[i][j] > 0:
                if (y + i >= BROJ_REDOVA or
                    x + j < 0 or
                    x + j >= BROJ_KOLONA or
                    (y + i >= 0 and polje[y + i][x + j] > 0)):
                    return False
    return True

def postavi_oblik(polje, oblik, pozicija_kolona, pozicija_red):
    for oblik_r in range(len(oblik)):
        for oblik_k in range(len(oblik[0])):
            if oblik[oblik_r][oblik_k] > 0:
                polje[pozicija_red + oblik_r][pozicija_kolona + oblik_k] = oblik[oblik_r][oblik_k]

def nacrtaj_stanje_igre(screen, polje, trenutni_oblik, pozicija_kolona, pozicija_red):
    screen.fill(BLACK)
    
    # Nacrtaj trenutni oblik
    for oblik_r in range(len(trenutni_oblik)):
        for oblik_k in range(len(trenutni_oblik[0])):
            if trenutni_oblik[oblik_r][oblik_k] > 0:
                boja = trenutni_oblik[oblik_r][oblik_k] -1
                x = (pozicija_kolona + oblik_k) * VELICINA_BLOKA
                y = (pozicija_red + oblik_r) * VELICINA_BLOKA
                pygame.draw.rect(screen, BOJE[boja], (x, y, VELICINA_BLOKA, VELICINA_BLOKA))
    
    # Nacrtaj ostatak polja
    for polje_r in range(BROJ_REDOVA):
        for polje_k in range(BROJ_KOLONA):
            if polje[polje_r][polje_k] > 0:
                boja = polje[polje_r][polje_k] -1
                x = polje_k * VELICINA_BLOKA
                y = polje_r * VELICINA_BLOKA
                pygame.draw.rect(screen, BOJE[boja], (x, y, VELICINA_BLOKA, VELICINA_BLOKA))
    pygame.display.update()

def rotiraj_oblik(oblik):
    print("rotiraj_oblik: ", oblik)
    rows, cols = len(oblik[0]), len(oblik)
    novi_oblik = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(0)
        novi_oblik.append(row)

    
    for oblik_k in range(len(oblik[0])):
        for oblik_r in range(len(oblik)):
            # len(novi_oblik)
            novi_oblik [ len(novi_oblik)-1 -oblik_k ][ oblik_r ] = oblik[oblik_r][oblik_k]

    return novi_oblik

def obrisi_redak(polje, redak):
    novo_polje = polje
    for polje_r in range(redak, 0, -1):
        for polje_k in range(len(polje[redak])):
            novo_polje[polje_r][polje_k] = polje[polje_r-1][polje_k]
    return novo_polje

def nadji_popunjeni_redak(polje):
    for redak in range(len(polje)):
        popunjeni_redak = True
        for kolona in range(len(polje[redak])):
            if polje[redak][kolona] == 0:
                popunjeni_redak = False
        if popunjeni_redak == True:
            return redak

    return -1

polje = napravi_polje()
trenutni_oblik, pozicija_kolona, pozicija_red = napravi_novi_oblik()
game_over = False

milisekundi_izmedju_padova = 500  # milliseconds
zadnje_vrijeme_pada = pygame.time.get_ticks()

while not game_over:   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if smije_biti_postavljen(polje, trenutni_oblik, pozicija_kolona - 1, pozicija_red):
                    pozicija_kolona -= 1
            
            if event.key == pygame.K_RIGHT:
                if smije_biti_postavljen(polje, trenutni_oblik, pozicija_kolona + 1, pozicija_red):
                    pozicija_kolona += 1     

            if event.key == pygame.K_UP:
                privremeni_oblik = rotiraj_oblik(trenutni_oblik)
                if smije_biti_postavljen(polje, privremeni_oblik, pozicija_kolona, pozicija_red):
                    trenutni_oblik = privremeni_oblik

            if event.key == pygame.K_DOWN:
                if smije_biti_postavljen(polje, trenutni_oblik, pozicija_kolona, pozicija_red+2):
                    pozicija_red += 2

    popunjeni_redak = nadji_popunjeni_redak(polje)
    if popunjeni_redak >= 0:
        polje = obrisi_redak(polje, popunjeni_redak)

    # Upali gravitaciju
    trenutno_vrijeme = pygame.time.get_ticks()
    proslo_milisekundi = trenutno_vrijeme - zadnje_vrijeme_pada
    if proslo_milisekundi > milisekundi_izmedju_padova:
        if smije_biti_postavljen(polje, trenutni_oblik, pozicija_kolona, pozicija_red + 1):
            pozicija_red += 1
        else:
            postavi_oblik(polje, trenutni_oblik, pozicija_kolona, pozicija_red)
            trenutni_oblik, pozicija_kolona, pozicija_red = napravi_novi_oblik()
            if not smije_biti_postavljen(polje, trenutni_oblik, pozicija_kolona, pozicija_red):
                game_over = True
        zadnje_vrijeme_pada = trenutno_vrijeme
    
    # Draw everything
    nacrtaj_stanje_igre(screen, polje, trenutni_oblik, pozicija_kolona, pozicija_red)

# Game Over screen
font = pygame.font.Font(None, 48)
game_over_text = font.render('Game Over!', True, WHITE)
screen.blit(game_over_text,
            (SIRINA_EKRANA // 2 - game_over_text.get_width() // 2,
                VISINA_EKRANA // 2 - game_over_text.get_height() // 2))
pygame.display.update()
pygame.time.wait(2000)

pygame.quit()