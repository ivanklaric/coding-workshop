import pygame

pygame.init()
screen = pygame.display.set_mode((600, 768))
pygame.display.set_caption("Vjesala.")

BACKGROUND_COLOR = (8, 56, 4)
LINE_COLOR = (255, 0, 0)
LINE_WIDTH = 3

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill( BACKGROUND_COLOR )

    # Crtamo vjesala   
    pygame.draw.line(screen, LINE_COLOR, (50, 700), (150, 700), LINE_WIDTH)  
    pygame.draw.line(screen, LINE_COLOR, (100, 100), (100, 700), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (100, 100), (300, 100), LINE_WIDTH) 
    pygame.draw.line(screen, LINE_COLOR, (300, 100), (300, 150), LINE_WIDTH)  

    # Crtamo covjeka
    ## Glava
    pygame.draw.circle(screen, LINE_COLOR, (300, 175), 25, LINE_WIDTH)
    ## Vrat
    ## Lijeva ruka
    ## Desna ruka
    ## Trup
    ## Lijeva noga
    ## Desna noga

    pygame.display.flip()

pygame.quit()