from mario_lib import *

def initialize_character(x, y, speed_x, speed_y, jump_impulse, picture_filename, height = 16, width = 16):
    return {
        'x': x,
        'y': y,
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