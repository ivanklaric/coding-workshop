import pygame

pygame.init()

screen = pygame.display.set_mode((768, 1024))
pygame.display.set_caption("Pacman!")

maze_element = pygame.image.load("img/maze-element.png")
small_dot = pygame.image.load("img/small-dot.png")
# 0 = prazno polje
# 1 = zid
# 2 = mala mrvica
# 3 = velika mrvica

level = [
    (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
    (1, 2, 2, 2, 2, 2, 2, 1, 2, 0, 0, 0, 0, 0, 1),
    (1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1),
    (1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1),
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

    for r in range(15):
        for i in range(15):
            if level[r][i] == 1:
                screen.blit(maze_element, (9 + 50*i, 174 +50*r))


    pygame.display.flip()

pygame.quit()