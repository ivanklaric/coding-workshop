from mario_lib import *

def initialize_character(x, y, speed_x, speed_y, jump_impulse, picture_filename):
    return {
        'x': x,
        'y': y,
        'speed_x': speed_x,
        'speed_y': speed_y,
        'jump_impulse': jump_impulse,
        'picture': ucitaj_sliku(picture_filename)
    }

def draw_character(screen, character):
    nacrtaj_sliku(screen, character['x'], character['y'], character['picture'])