import pygame

field_begin_x = 9
field_begin_y = 174

pygame.init()

screen = pygame.display.set_mode((768, 1024))
pygame.display.set_caption("Pacman!")
font = pygame.font.SysFont("Arial New", 24)

maze_element = pygame.image.load("img/maze-element.png")
blank_element = pygame.image.load("img/blank-element.png")
small_dot = pygame.image.load("img/small-dot.png")
big_dot = pygame.image.load("img/big-dot.png")
pacman = pygame.image.load("img/pacman.png")
# 0 = prazno polje
# 1 = zid
# 2 = mala mrvica
# 3 = velika mrvica

pacman_x = field_begin_x + 7 * 50
pacman_y = field_begin_y + 11 * 50

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

def get_row_col(pacman_x, pacman_y):
    row = (pacman_y - field_begin_y) // 50
    col = (pacman_x - field_begin_x) // 50

    return (row, col)

def get_remaining_space_x(pacman_x):
    return (pacman_x - field_begin_x) % 50

def get_remaining_space_y(pacman_y):
    return (pacman_y - field_begin_y) % 50


def can_move_left(pacman_x, pacman_y):
    (pacman_row, pacman_col) = get_row_col(pacman_x, pacman_y)
    if pacman_col == 0:
        return False
    if level[pacman_row][pacman_col-1] == 1:
        if get_remaining_space_x(pacman_x) == 0:
            return False
    return True

def can_move_right(pacman_x, pacman_y):
    (pacman_row, pacman_col) = get_row_col(pacman_x, pacman_y)
    if pacman_col == 0:
        return False
    if level[pacman_row][pacman_col+1] == 1:
        if get_remaining_space_x(pacman_x) == 0:
            return False
    return True

def can_move_up(pacman_x, pacman_y):
    (pacman_row, pacman_col) = get_row_col(pacman_x, pacman_y)
    if pacman_row == 0:
        return False
    if level[pacman_row - 1][pacman_col] == 1:
        if get_remaining_space_y(pacman_y) == 0:
            return False
    return True

def can_move_down(pacman_x, pacman_y):
    (pacman_row, pacman_col) = get_row_col(pacman_x, pacman_y)
    if pacman_row == 0:
        return False
    if level[pacman_row + 1][pacman_col] == 1:
        if get_remaining_space_y(pacman_y) == 0:
            return False
    return True

def get_debug_info():
    return "X: " + str(pacman_x) + ", Y:" + str(pacman_y) + ", S_X:" + str(field_begin_x) + ", S_Y:" + str(field_begin_y) + ", (R,C):" + str(get_row_col(pacman_x, pacman_y))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys_pressed = pygame.key.get_pressed()

    if (keys_pressed[pygame.K_LEFT] or keys_pressed[pygame.K_a]) and can_move_left(pacman_x, pacman_y):
        pacman_x -= 2
    if (keys_pressed[pygame.K_RIGHT] or keys_pressed[pygame.K_d]) and can_move_right(pacman_x, pacman_y):
        pacman_x += 2
    if (keys_pressed[pygame.K_UP] or keys_pressed[pygame.K_w]) and can_move_up(pacman_x, pacman_y):
        pacman_y -= 2
    if (keys_pressed[pygame.K_DOWN] or keys_pressed[pygame.K_s]) and can_move_down(pacman_x, pacman_y):
        pacman_y += 2


    screen.fill("BLACK")
    text = font.render(get_debug_info(), True, "WHITE")
    screen.blit(text, (10, 10))

    for r in range(15):
        for i in range(15):
            if level[r][i] == 0:
                screen.blit(blank_element, (field_begin_x + 50*i, field_begin_y + 50*r))
            if level[r][i] == 1:
                screen.blit(maze_element, (field_begin_x + 50*i, field_begin_y + 50*r))
            if level[r][i] == 2:
                screen.blit(small_dot, (field_begin_x + 50*i, field_begin_y + 50*r))
            if level[r][i] == 3:
                screen.blit(big_dot, (field_begin_x + 50*i, field_begin_y + 50*r))


    screen.blit(pacman, (pacman_x, pacman_y))
    pygame.display.flip()

pygame.quit()