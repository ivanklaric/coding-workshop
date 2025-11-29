import pygame
import sys
import time

pygame.init()

screen = pygame.display.set_mode((900, 900))
pygame.display.set_caption("Krizic-kruzic!")

background_color = (3, 252, 152)
line_color = (0, 0, 0)

def nacrtaj_polje():
    pygame.draw.line(screen, line_color, (0, 300), (900, 300), 2)
    pygame.draw.line(screen, line_color, (0, 600), (900, 600), 2)
    pygame.draw.line(screen, line_color, (300, 0), (300, 900), 2)
    pygame.draw.line(screen, line_color, (600, 0), (600, 900), 2)

def nacrtaj_krizic(x, y):
    pygame.draw.line(screen, line_color, (x+30, y+30), (x+270, y+270), 2)
    pygame.draw.line(screen, line_color, (x+30, y+270), (x+270, y+30), 2)

def nacrtaj_kruzic(x, y):
    pygame.draw.circle(screen, line_color, (x+150, y+150), 120, 2)

polje = [[0, 0, 0], 
         [0, 0, 0], 
         [0, 0, 0]]
sljedeci_znak = 1
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            position = event.pos
            redak = position[1] // 300
            kolona = position[0] // 300
            if polje[redak][kolona] == 0:
                polje[redak][kolona] = sljedeci_znak
                if sljedeci_znak == 1:
                    sljedeci_znak = 2
                else:
                    sljedeci_znak = 1

    screen.fill(background_color)
    nacrtaj_polje()
    for redak in range(3):
        for kolona in range(3):
            x = kolona * 300
            y = redak * 300
            if polje[redak][kolona] == 1:
                nacrtaj_krizic(x, y)
            if polje[redak][kolona] == 2:
                nacrtaj_kruzic(x, y)

    pygame.display.update()

pygame.quit()
sys.exit()