import pygame

def ucitaj_sve_slike():
    lista = []
    lista.append(None)
    lista.append(ucitaj_sliku('lab-8/ground-tile.png'))
    lista.append(ucitaj_sliku('lab-8/grassy-tile.png'))
    lista.append(ucitaj_sliku('lab-8/question-box.png'))
    lista.append(ucitaj_sliku('lab-8/ground-tile.png'))
    return lista

def ucitaj_sliku(filename, size=(16, 16)):
    image = pygame.image.load(filename)
    return pygame.transform.scale(image, size)

def nacrtaj_sliku(screen, x, y, slika):
    if slika != None:
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

def nacrtaj_pravokutnik_polja(screen, slika, redak, kolona):
    nacrtaj_sliku(screen, kolona * 16, redak * 16, slika)

def nacrtaj_polje(screen, lista_slika, polje, kolona_pocetka):
    for broj_retka in range(len(polje)):
        red = polje[broj_retka]
        for broj_kolone in range(kolona_pocetka, len(red)):
            slika_za_nacrtat =  polje[broj_retka][broj_kolone]
            nacrtaj_pravokutnik_polja(screen, lista_slika[slika_za_nacrtat], broj_retka, broj_kolone-kolona_pocetka)

def generiraj_rectanglove_polja(polje, kolona_pocetka):
    ret = []
    for broj_retka in range(len(polje)):
        red = polje[broj_retka]
        for broj_kolone in range(kolona_pocetka, len(red)):
            if polje[broj_retka][broj_kolone] > 0:
                ret.append(pygame.Rect(broj_kolone*16, broj_retka*16, 16, 16))
    return ret