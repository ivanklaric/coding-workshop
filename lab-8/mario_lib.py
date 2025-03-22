import pygame

def ucitaj_sliku(filename, size=(40, 30)):
    image = pygame.image.load(filename)
    return pygame.transform.scale(image, size)

def nacrtaj_sliku(screen, x, y, slika):
    screen.blit(slika, (x, y))