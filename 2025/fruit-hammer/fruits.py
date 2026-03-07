import pygame
import random

def generate_fruit():
    fruit_x = random.randint(0,900)
    fruit_y = 700
    fruit1 = {
        'image': images_list[random.randint(0,3)],
        'coordinate': (fruit_x, fruit_y),
        'rectangle': pygame.Rect(fruit_x, fruit_y, 50, 50),
        'smashed': False,
        'speed_x': random.uniform(-0.5, +0.5),
        'speed_y': random.uniform(-2.0, -0.1)
    }
    return fruit1  

pygame.init()
screen = pygame.display.set_mode((1024, 768))
pygame.display.set_caption("Fruit Hammer")

background_image = pygame.image.load("img/background.png")
hammer_image = pygame.image.load("img/hammer.png")
hammer_down_image = pygame.image.load("img/hammer2.png")
splash_image = pygame.image.load("img/splash.png")
images_list = [
    pygame.image.load("img/apple.png"),
    pygame.image.load("img/ananas.png"),
    pygame.image.load("img/banana.png"),
    pygame.image.load("img/cherry.png")
]

fruit_list = []
for i in range(random.randint(2,5)):
    fruit_list.append(generate_fruit())

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

    visible_fruit = 0
    for fruit in fruit_list:
        if not fruit['smashed']:
            visible = True
            (fruit_x, fruit_y) = fruit['coordinate']
            if fruit_x > 1024 or fruit_x < 0:
                visible = False
            if fruit_y > 768:
                visible = False
            if visible:
                visible_fruit = visible_fruit + 1
    if visible_fruit < 3:
        fruit_list.append(generate_fruit())


    # Introduce gravity
    for fruit in fruit_list:
        fruit['speed_y'] = fruit['speed_y'] + 0.001

    # Move the fruits
    for fruit in fruit_list:
        if not fruit['smashed']:
            (fruit_x, fruit_y) = fruit['coordinate']
            fruit['coordinate'] = (fruit_x + fruit['speed_x'], fruit_y + fruit['speed_y'])
            fruit['rectangle'] = pygame.Rect(fruit_x + fruit['speed_x'], fruit_y + fruit['speed_y'], 50, 50)


    # Draw the fruit
    for fruit in fruit_list:
        if fruit['smashed']:
            screen.blit(splash_image, fruit['coordinate'])
        else:
            screen.blit(fruit['image'], fruit['coordinate'])

    # Draw the hammer
    if mouse_buttons[0]: # the mouse button was clicked
        for fruit in fruit_list:
            if fruit['rectangle'].collidepoint(mouse_pos): # click happened inside the fruit rectangle
                fruit['smashed'] = True
        # Draw the hammer down
        screen.blit(hammer_down_image, (mouse_pos[0] - 45, mouse_pos[1] - 45))
    else:  
        screen.blit(hammer_image, (mouse_pos[0] - 45, mouse_pos[1] - 45))

    pygame.display.flip()

pygame.quit()
