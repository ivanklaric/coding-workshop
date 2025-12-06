import pygame

pygame.init()

RACKET_HEIGHT = 100
RACKET_WIDTH = 30
BACKGROUND_COLOR = (18, 59, 13)
RACKET_COLOR = (255, 255, 255)

left_racket_y = 768 // 2 - RACKET_HEIGHT // 2
right_racket_y = 768 // 2 - RACKET_HEIGHT // 2

screen = pygame.display.set_mode((1024, 768))
pygame.display.set_caption("Pong!")
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            # Check for left racket events
            if event.key == pygame.K_w:
                left_racket_y -= 30
            if event.key == pygame.K_s:
                left_racket_y += 30
            # Check for right racket events
            if event.key == pygame.K_UP:
                right_racket_y -= 30
            if event.key == pygame.K_DOWN:
                right_racket_y += 30


    if left_racket_y < 0:
        left_racket_y = 0
    if left_racket_y > 668:
        left_racket_y = 668
    if right_racket_y < 0:
        right_racket_y = 0
    if right_racket_y > 668:
        right_racket_y = 668

    # Fill the screen with the background color (Green)
    screen.fill( BACKGROUND_COLOR )     
    # Draw the left racket
    pygame.draw.rect(screen, RACKET_COLOR, (0, left_racket_y, RACKET_WIDTH, RACKET_HEIGHT))
    # Draw the right racket
    pygame.draw.rect(screen, RACKET_COLOR, (1024-RACKET_WIDTH, right_racket_y, RACKET_WIDTH, RACKET_HEIGHT))
    # Draw the net
    pygame.draw.line(screen, RACKET_COLOR, (512, 0), (512, 768))

    pygame.display.flip()

pygame.quit()