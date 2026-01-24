import pygame
import random

pygame.init()
screen = pygame.display.set_mode((600, 768))
pygame.display.set_caption("Vjesala.")
font = pygame.font.SysFont("Courier New", 48)
font2 = pygame.font.SysFont("Courier New", 24)


BACKGROUND_COLOR = (8, 56, 4)
LINE_COLOR = (255, 0, 0)
LINE_WIDTH = 3
FONT_COLOR = (255, 255, 255)

mistake_count = 0
dictionary = [
    "DIJETE", "ŽENA", "GRAD", "KUĆA", "PAS", "MAČKA", "DRVO", "RIJEKA", "MORE",
    "PLANINA", "SUNCE", "MJESEC", "ZVIJEZDA", "NEBO", "ZEMLJA", "VODA", "HRANA", "KRUH", "MLIJEKO",
    "KAVA", "CAJ", "VOCE", "POVRCE", "MESO", "RIBA", "KREMŠNITA", "TRG", "ULICA", "CESTA",
    "AUTO", "VLAK", "AVION", "BROD", "BICIKL", "SKOLA", "KNJIGA", "OLOVKA", "PAPIR", "RACUNALO",
    "TELEFON", "STOL", "STOLICA", "KREVET", "PROZOR", "VRATA", "SOBA", "KUHINJA", "KUPAONICA", "VRT",
    "CVIJET", "TRAVA", "SUMA", "POLJE", "OTOK", "OBALA", "PIJESAK", "KAMEN", "ZIMA", "LJETI",
    "PROLJECE", "JESEN", "KIŠA", "SNIJEG", "VJETAR", "OBLAK", "VATRA", "SRECA", "LJUBAV", "PRIJATELJ",
    "OBITELJ", "MAJKA", "OTAC", "BRAT", "SESTRA", "RAD", "IGRA", "PJESMA", "GLAZBA", "FILM",
    "SLIKA", "JEZIK", "RIJEC", "VRIJEME", "DAN", "NOC", "JUTRO", "VECER", "SAT", "TJEDAN",
    "MJESEC", "GODINA", "DRZAVA", "NAROD", "NOVAC", "POSAO", "ŠKOLA", "BOLNICA", "CRKVA", "ZAKON"
]
dictionary_index = random.randint(0, len(dictionary)-1)
secret_word = dictionary[dictionary_index]
guessed_letters = ['_'] * len(secret_word)
attempted_letters = []

running = True
game_over = False
while running:
    guessed_word = " ".join(guessed_letters)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and not game_over:
            user_char = event.unicode.upper()
            if user_char in secret_word:
                for index, letter in enumerate(secret_word):
                    if letter == user_char:
                        guessed_letters[index] = user_char
                       
            else:
                if not user_char in attempted_letters:
                    attempted_letters.append(user_char)
                    mistake_count += 1

    screen.fill( BACKGROUND_COLOR )

    text = font.render(guessed_word, True, FONT_COLOR)
    screen.blit(text, (100, 10))

    attempted_str = ",".join(attempted_letters)
    attempted_text = font2.render(attempted_str, True, FONT_COLOR)
    screen.blit(attempted_text, (50, 710))

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
        game_over_text = font.render("Game Over!", True, FONT_COLOR)
        secret_word_text = font.render(secret_word, True, FONT_COLOR)
        screen.blit(game_over_text, (150, 300))
        screen.blit(secret_word_text, (150, 350))
        game_over = True

    if not "_" in guessed_letters:
        victory_text = font.render("Victory!", True, FONT_COLOR)
        screen.blit(victory_text, (170, 300))
        game_over = True


    pygame.display.flip()

pygame.quit()