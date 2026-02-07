import pygame

pygame.init()
screen = pygame.display.set_mode((1024, 768))
pygame.display.set_caption("Fruit Hammer")

background_image = pygame.image.load("img/background.png")
hammer_image = pygame.image.load("img/hammer.png")
hammer_down_image = pygame.image.load("img/hammer2.png")
splash_image = pygame.image.load("img/splash.png")

fruit = {
    'image': pygame.image.load("img/apple.png"),
    'coordinate': (300, 300),
    'rectangle': pygame.Rect(300, 300, 50, 50),
    'smashed': False
}

pygame.mouse.set_visible(False)

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    mouse_pos = pygame.mouse.get_pos()
    mouse_buttons = pygame.mouse.get_pressed()

    # Draw the background
    screen.blit(background_image, (0, 0))
    screen.blit(background_image, (0, 559))

    # Draw the fruit
    if fruit['smashed']:
        screen.blit(splash_image, fruit['coordinate'])
    else:
        screen.blit(fruit['image'], fruit['coordinate'])

    # Draw the hammer
    if mouse_buttons[0]: # the mouse button was clicked
        if fruit['rectangle'].collidepoint(mouse_pos): # click happened inside the fruit rectangle
            fruit['smashed'] = True
        # Draw the hammer down
        screen.blit(hammer_down_image, (mouse_pos[0] - 45, mouse_pos[1] - 45))
    else:  
        screen.blit(hammer_image, (mouse_pos[0] - 45, mouse_pos[1] - 45))

    pygame.display.flip()

pygame.quit()
