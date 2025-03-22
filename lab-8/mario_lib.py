import pygame

def ucitaj_sliku(filename, size=(40, 30)):
    image = pygame.image.load(filename)
    return pygame.transform.scale(image, size)

def nacrtaj_sliku(screen, x, y, slika):
    screen.blit(slika, (x, y))

def inicijaliziraj_polje(broj_redaka, broj_stupaca):
    polje = []
    for _ in range(broj_redaka):
        red = [0] * broj_stupaca
        polje.append(red)
    return polje

def napravi_ravnicu(polje):
    donji_redak = polje[-1]
    for kolona in range(len(donji_redak)):
        polje[-1][kolona] = 1
    return polje

def nacrtaj_pravkutnik_polja(screen, boja, redak, kolona):
    pygame.draw.rect(screen, boja, ( kolona * 16, redak * 16, 16, 16 ))

def nacrtaj_polje(screen, polje):
    for broj_retka in range(len(polje)):
        red = polje[broj_retka]
        for broj_kolone in range(len(red)):
            if polje[broj_retka][broj_kolone] == 1:
                nacrtaj_pravkutnik_polja(screen, 'brown', broj_retka, broj_kolone)