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
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1],
    [1, 2, 1, 1, 2, 1, 2, 1, 3, 1, 2, 1, 1, 2, 1],
    [1, 2, 1, 1, 2, 1, 2, 2, 3, 1, 2, 1, 1, 2, 1],
    [1, 2, 2, 2, 2, 1, 1, 2, 1, 1, 2, 2, 2, 2, 1],
    [1, 1, 1, 2, 1, 2, 2, 2, 2, 2, 1, 2, 1, 1, 1],
    [1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 1, 2, 2, 2, 1],
    [1, 2, 1, 2, 2, 2, 1, 2, 1, 2, 2, 2, 1, 2, 1],
    [1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 1, 2, 2, 2, 1],
    [1, 1, 1, 2, 1, 2, 2, 2, 2, 2, 1, 2, 1, 1, 1],
    [1, 2, 2, 2, 2, 1, 1, 2, 1, 1, 2, 2, 2, 2, 1],
    [1, 2, 1, 1, 2, 1, 2, 0, 2, 1, 2, 1, 1, 2, 1],
    [1, 2, 1, 1, 2, 1, 2, 1, 2, 1, 2, 1, 1, 2, 1],
    [1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

def get_row_col(pacman_x, pacman_y):
    row = int((pacman_y - field_begin_y) // 50)
    col = int((pacman_x - field_begin_x) // 50)

    return (row, col)

def get_remaining_space_x(pacman_x):
    return (pacman_x - field_begin_x) % 50

def get_remaining_space_y(pacman_y):
    return (pacman_y - field_begin_y) % 50


def can_move_left(pacman_x, pacman_y):
    (pacman_row, pacman_col) = get_row_col(pacman_x, pacman_y)
    if pacman_col == 0:
        return False
    # samo skreni vodoravno kad smo poravnati po visini (inace bismo zagazili u zid)
    if get_remaining_space_y(pacman_y) != 0:
        return False
    if level[pacman_row][pacman_col-1] == 1:
        if get_remaining_space_x(pacman_x) == 0:
            return False
    return True

def can_move_right(pacman_x, pacman_y):
    (pacman_row, pacman_col) = get_row_col(pacman_x, pacman_y)
    if pacman_col == 14:
        return False
    if get_remaining_space_y(pacman_y) != 0:
        return False
    if level[pacman_row][pacman_col+1] == 1:
        if get_remaining_space_x(pacman_x) == 0:
            return False
    return True

def can_move_up(pacman_x, pacman_y):
    (pacman_row, pacman_col) = get_row_col(pacman_x, pacman_y)
    if pacman_row == 0:
        return False
    # samo skreni okomito kad smo poravnati po sirini
    if get_remaining_space_x(pacman_x) != 0:
        return False
    if level[pacman_row - 1][pacman_col] == 1:
        if get_remaining_space_y(pacman_y) == 0:
            return False
    return True

def can_move_down(pacman_x, pacman_y):
    (pacman_row, pacman_col) = get_row_col(pacman_x, pacman_y)
    if pacman_row == 14:
        return False
    if get_remaining_space_x(pacman_x) != 0:
        return False
    if level[pacman_row + 1][pacman_col] == 1:
        if get_remaining_space_y(pacman_y) == 0:
            return False
    return True

running = True
angle = 0
score = 0

x_pomicanje = 0
y_pomicanje = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys_pressed = pygame.key.get_pressed()

    tipka_pritisnuta = False
    if (keys_pressed[pygame.K_LEFT] or keys_pressed[pygame.K_a]) and can_move_left(pacman_x, pacman_y):
        tipka_pritisnuta = True
        angle = 180
        pacman_x -= 2
    if (keys_pressed[pygame.K_RIGHT] or keys_pressed[pygame.K_d]) and can_move_right(pacman_x, pacman_y):
        tipka_pritisnuta = True
        angle = 0
        pacman_x += 2
    if (keys_pressed[pygame.K_UP] or keys_pressed[pygame.K_w]) and can_move_up(pacman_x, pacman_y):
        tipka_pritisnuta = True
        angle = 90
        pacman_y -= 2
    if (keys_pressed[pygame.K_DOWN] or keys_pressed[pygame.K_s]) and can_move_down(pacman_x, pacman_y):
        tipka_pritisnuta = True
        angle = 270
        pacman_y += 2

    print(f'{x_pomicanje = }, {y_pomicanje = }, {pacman_x = }, {pacman_y = }, {tipka_pritisnuta = }')
    if not tipka_pritisnuta:
        print(f'{pacman_x / 50 = }')
        print(f'{pacman_y / 50 = }')
        x_pomicanje = round(round((pacman_x - 9) / 50) * 50 - (pacman_x - 9))
        y_pomicanje = round(round((pacman_y - 174) / 50) * 50 - (pacman_y - 174))
    else:
        x_pomicanje = 0
        y_pomicanje = 0
    
    if x_pomicanje != 0:
        pacman_x += 1 * x_pomicanje / abs(x_pomicanje)
        x_pomicanje += 1 * (-(x_pomicanje / abs(x_pomicanje)))
    if y_pomicanje != 0:
        pacman_y += 1 * y_pomicanje / abs(y_pomicanje)
        y_pomicanje += 1 * (-(y_pomicanje / abs(y_pomicanje)))


    screen.fill("BLACK")
    text = font.render(f'{score = }', True, "WHITE")
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

    rotated_pacman = pygame.transform.rotate(pacman, angle)
    screen.blit(rotated_pacman, (pacman_x, pacman_y))
    (pacman_row, pacman_col) = get_row_col(pacman_x, pacman_y)
    pygame.draw.rect(screen, "WHITE", ( field_begin_x + pacman_col * 50, field_begin_y + pacman_row * 50, 50, 50), 2)
    pygame.display.flip()

pygame.quit()