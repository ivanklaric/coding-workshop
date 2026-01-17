import pygame

pygame.init()
screen = pygame.display.set_mode((600, 768))
pygame.display.set_caption("Vjesala.")
font = pygame.font.SysFont("Courier New", 48)

BACKGROUND_COLOR = (8, 56, 4)
LINE_COLOR = (255, 0, 0)
LINE_WIDTH = 3
FONT_COLOR = (255, 255, 255)

mistake_count = 0
secret_word = 'BUNKER'
guessed_letters = ['_', '_', '_', '_', '_', '_']

running = True
while running:
    guessed_word = " ".join(guessed_letters)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            user_char = event.unicode.upper()
            if user_char in secret_word:
                for index, letter in enumerate(secret_word):
                    if letter == user_char:
                        guessed_letters[index] = user_char
            else:
                mistake_count += 1

    screen.fill( BACKGROUND_COLOR )

    text = font.render(guessed_word, True, FONT_COLOR)
    screen.blit(text, (100, 10))

    # Drawing the gallows
    pygame.draw.line(screen, LINE_COLOR, (50, 700), (150, 700), LINE_WIDTH)  
    pygame.draw.line(screen, LINE_COLOR, (100, 100), (100, 700), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (100, 100), (300, 100), LINE_WIDTH) 
    pygame.draw.line(screen, LINE_COLOR, (300, 100), (300, 150), LINE_WIDTH)  

    # Drawing the man
    ## Head
    if mistake_count >= 1:
        pygame.draw.circle(screen, LINE_COLOR, (300, 175), 25, LINE_WIDTH)
    ## Neck
    if mistake_count >= 2:
        pygame.draw.line(screen, LINE_COLOR, (300, 200), (300, 225), LINE_WIDTH)  
    ## Left arm
    if mistake_count >= 3:
        pygame.draw.line(screen, LINE_COLOR, (300, 225), (200, 300), LINE_WIDTH)  
    ## Right arm
    if mistake_count >= 4:
        pygame.draw.line(screen, LINE_COLOR, (300, 225), (400, 300), LINE_WIDTH)  
    ## Core
    if mistake_count >= 5:
        pygame.draw.line(screen, LINE_COLOR, (300, 225), (300, 375), LINE_WIDTH)  
    ## Left leg
    if mistake_count >= 6:
        pygame.draw.line(screen, LINE_COLOR, (300, 375), (250, 500), LINE_WIDTH)  
    ## Right leg
    if mistake_count >= 7:
        pygame.draw.line(screen, LINE_COLOR, (300, 375), (350, 500), LINE_WIDTH)  

    pygame.display.flip()

pygame.quit()