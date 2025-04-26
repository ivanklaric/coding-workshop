from mario_lib import *

STATE_STANDING = 1
STATE_WALKING = 2
STATE_JUMP = 3

def initialize_character(x, y, speed_x, speed_y, jump_impulse, picture_filename, walking_pictures, jumping_picture, height = 16, width = 16):
    ret = {
        'x': x,
        'y': y,
        'speed_x': speed_x,
        'speed_y': speed_y,
        'jump_impulse': jump_impulse,
        'state': STATE_STANDING,
        'picture': ucitaj_sliku(picture_filename),
        'jumping_picture': ucitaj_sliku(jumping_picture),
        'height': height,
        'width': width
    }
    walking_animation = []
    for picture_filename in walking_pictures:
        walking_animation.append(ucitaj_sliku(picture_filename))
    ret['walking_pictures'] = walking_animation
    return ret

def draw_character(screen, character):
    if character['state'] == STATE_STANDING:
        nacrtaj_sliku(screen, character['x'], character['y'], character['picture'])
    elif character['state'] == STATE_WALKING:
        nacrtaj_sliku(screen, character['x'], character['y'], character['walking_pictures'][0])
    elif character['state'] == STATE_JUMP:
        nacrtaj_sliku(screen, character['x'], character['y'], character['jumping_picture'])

def can_character_move_to(character, level, kolona_pocetka, next_x, next_y):
    character_rect = pygame.Rect(next_x, next_y, character['width'], character['height'])
    level_rects = generiraj_rectanglove_polja(level, kolona_pocetka)
    if character_rect.collidelist(level_rects) != -1:
        return False

    return True