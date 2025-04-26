from mario_lib import *

def initialize_character(x, y, fly, speed_x, speed_y, jump_impulse, picture_filename, height = 16, width = 16):
    return {
        'x': x,
        'y': y,
        'fly': fly,
        'speed_x': speed_x,
        'speed_y': speed_y,
        'jump_impulse': jump_impulse,
        'picture': ucitaj_sliku(picture_filename),
        'height': height,
        'width': width
    }

def draw_character(screen, character):
    nacrtaj_sliku(screen, character['x'], character['y'], character['picture'])

def can_character_move_to(character, level, kolona_pocetka, next_x, next_y):
    character_rect = pygame.Rect(next_x, next_y, character['width'], character['height'])
    level_rects = generiraj_rectanglove_polja(level, kolona_pocetka)
    if character_rect.collidelist(level_rects) != -1:
        return False

    return True

def what_row_col_is_character_in(character, kolona_pocetka):
    row = character['y'] // 16
    col = kolona_pocetka + character['x'] // 16
    return (int(row), int(col))

def does_character_fly(character, polje, kolona_pocetka):
    (row, col) = what_row_col_is_character_in(character, kolona_pocetka)
    working_row = row
    working_col = col
    if character['y'] // 16 == character['y'] / 16:
        if character['x'] % 16 == 0:
            i = 0
            while polje[working_row][working_col] == 0:
                working_row += 1
                i += 1
            if i == 1:
                return False, 0
            else:
                return True, (i - 1) * 16
        else:
            i0 = 0
            while polje[working_row][working_col] == 0:
                working_row += 1
                i0 += 1
            i1 = 1
            while polje[working_row][working_col + 1] == 0:
                working_row += 1
                i1 += 1
            i = min(i0, i1)
            if i == 1:
                return False, 0
            else:
                return True, (working_row - i) * 16
    else:
        if character['x'] % 16 == 0:
            i = 0
            while polje[working_row][working_col] == 0:
                working_row += 1
                i += 1
            if i == 2:
                return True, 16 - character['y'] % 16
            else:
                return True, (i - 2) * 16 + (16 - character['y'] % 16)
            
        else:
            i0 = 0
            while polje[working_row][working_col] == 0:
                working_row += 1
                i0 += 1
            i1 = 1
            while polje[working_row][working_col + 1] == 0:
                working_row += 1
                i1 += 1
            i = min(i0, i1)
            if i == 1:
                return True, 0
            else:
                return True, (working_row - i) * 16