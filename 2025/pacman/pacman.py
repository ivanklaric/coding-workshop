import pygame

pygame.init()

screen = pygame.display.set_mode((768, 1024))
pygame.display.set_caption("Pacman!")

maze_element = pygame.image.load("img/maze-element.png")
blank_element = pygame.image.load("img/blank-element.png")
small_dot = pygame.image.load("img/small-dot.png")
big_dot = pygame.image.load("img/big-dot.png")
pacman = pygame.image.load("img/pacman.png")
# 0 = prazno polje
# 1 = zid
# 2 = mala mrvica
# 3 = velika mrvica

pacman_x = 9 + 7 * 50
pacman_y = 174 + 11 * 50

level = [
    (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
    (1, 2, 2, 2, 2, 2, 2, 1, 2, 0, 0, 0, 0, 0, 1),
    (1, 0, 1, 1, 0, 1, 0, 1, 3, 1, 0, 1, 1, 0, 1),
    (1, 0, 1, 1, 0, 1, 0, 0, 3, 1, 0, 1, 1, 0, 1),
    (1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1),
    (1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1),
    (1, 0, 0, 0, 1, 0, 1, 1, 1, 2, 1, 0, 0, 0, 1),
    (1, 0, 1, 0, 0, 0, 1, 0, 1, 2, 0, 0, 1, 0, 1),
    (1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1),
    (1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1),
    (1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1),
    (1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1),
    (1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1),
    (1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1),
    (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
]
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys_pressed = pygame.key.get_pressed()

    if keys_pressed[pygame.K_LEFT] or keys_pressed[pygame.K_a]:
        pacman_x -= 50


    for r in range(15):
        for i in range(15):
            if level[r][i] == 0:
                screen.blit(blank_element, (9 + 50*i, 174 +50*r))
            if level[r][i] == 1:
                screen.blit(maze_element, (9 + 50*i, 174 +50*r))
            if level[r][i] == 2:
                screen.blit(small_dot, (9 + 50*i, 174 +50*r))
            if level[r][i] == 3:
                screen.blit(big_dot, (9 + 50*i, 174 +50*r))


    screen.blit(pacman, (pacman_x, pacman_y))
    pygame.display.flip()

pygame.quit()