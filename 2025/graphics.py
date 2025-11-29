import pygame

# Initialize pygame
pygame.init()

# Create a window
screen = pygame.display.set_mode((1024, 768))
pygame.display.set_caption("99 days!")

mario_x = 0
mario_y = 0
speed_x = 1
speed_y = 1

# Game loop
running = True
while running:
    mario_x += speed_x
    mario_y += speed_y

    # Check for close event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Fill screen with white
    screen.fill((43, 92, 56))
    
    # Draw "Hello World" text
    font = pygame.font.Font(None, 74)
    text = font.render("99 days in the woods!", True, (153, 90, 86))
    text_rect = text.get_rect(center=(512, 384))
    screen.blit(text, text_rect)

    image = pygame.image.load('mario.png')
    screen.blit(image, (mario_x, mario_y))
    
    if mario_x > 1024 - image.get_rect().width:
        speed_x = -1
    if mario_y > 768 - image.get_rect().height:
        speed_y = -1
    if mario_x < 0:
        speed_x = 1
    if mario_y < 0:
        speed_y = 1


    # Update display
    pygame.display.flip()

# Quit
pygame.quit()