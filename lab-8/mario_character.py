from character_lib import *
from mario_lib import * 

STATE_STANDING = 1
STATE_WALKING = 2
STATE_WALKING_BACK = 2.5
STATE_JUMP = 3
GRAVITACIJA = 0.2


class MarioCharacter:
    def __init__(self, x, y, speed_x, speed_y, jump_impulse, picture_filename, walking_pictures, jumping_picture, height = 16, width = 16):
        self.x = x
        self.y = y
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.jump_impulse = jump_impulse
        self.state =  STATE_STANDING
        self.picture = ucitaj_sliku(picture_filename,(height,width))
        self.jumping_picture =  ucitaj_sliku(jumping_picture,(height,width))
        self.height = height
        self.width =  width
        self.walking_last_updated = 0
        walking_animation = []
        for picture_filename in walking_pictures:
            walking_animation.append(ucitaj_sliku(picture_filename,(height,width)))
        self.walking_pictures = walking_animation
        self.walking_picture_index = 0

    def walk_left(self):
        self.speed_x = -4

    def walk_right(self):
        self.speed_x = 4

    def jump(self):
        self.speed_y -= self.jump_impulse

    def update_character_state(self):
        self.state = STATE_STANDING
        if self.speed_x != 0:
            self.state = STATE_WALKING
        if self.speed_y != 0:
            self.state = STATE_JUMP

    def can_move_to(self, level, kolona_pocetka, next_x, next_y):
        character_rect = pygame.Rect(next_x, next_y, self.width, self.height)
        level_rects = generiraj_rectanglove_polja(level, kolona_pocetka)
        if character_rect.collidelist(level_rects) != -1:
            return False

        return True
    
    def apply_gravity(self, level, kolona_pocetka):
        if self.can_move_to(level, kolona_pocetka, self.x, self.y + GRAVITACIJA):
            self.speed_y += GRAVITACIJA
            self.jump_impulse = 0
        else:
            self.jump_impulse = 3

    def what_row_col(self, kolona_pocetka):
        row = self.y // 16
        col = kolona_pocetka + self.x // 16
        return (int(row), int(col))

    def move(self, level, kolona_pocetka):
        next_x = self.x + self.speed_x
        next_y = self.y + self.speed_y

        if self.can_move_to(level, kolona_pocetka, next_x, self.y):
            self.x += self.speed_x
        else:
            (character_row, character_col) = self.what_row_col(kolona_pocetka)
            if level[character_row][character_col+1] == 5 and self.speed_x > 0:
                level[character_row][character_col+1] = 0
            if level[character_row][character_col-1] == 5 and self.speed_x < 0:
                level[character_row][character_col-1] = 0
            self.speed_x = 0

        if self.can_move_to(level, kolona_pocetka, self.x, next_y):
            self.y += self.speed_y
        else:
            (character_row, character_col) = self.what_row_col(kolona_pocetka)
            if character_row > 1 and self.speed_y < 0:
                # check for questionmark boxes
                if level[character_row-1][character_col] == 3:
                    level[character_row-1][character_col] = 4
                if level[character_row-1][character_col+1] == 3:
                    level[character_row-1][character_col+1] = 4
                if level[character_row-1][character_col-1] == 3:
                    level[character_row-1][character_col-1] = 4
                # check for coins
                if level[character_row-1][character_col] == 5: # coin hit
                    score += 1
                    level[character_row-1][character_col] = 0
            elif self.speed_y > 0:
                if level[character_row+1][character_col] == 5: # coin hit
                    score += 1
                    level[character_row+1][character_col] = 0
            self.speed_y = 0            

    def draw(self, screen):
        flip = False
        if self.speed_x < 0:
            flip = True
        if self.state == STATE_STANDING:
            self.walking_last_updated = 0
            nacrtaj_sliku(screen, self.x, self.y, self.picture)
        elif self.state == STATE_WALKING:
            # move the animation to the next image if more than 100ms passed
            if pygame.time.get_ticks()-self.walking_last_updated > 50:
                self.walking_picture_index = (self.walking_picture_index + 1) % len(self.walking_pictures)
                self.walking_last_updated = pygame.time.get_ticks()
            nacrtaj_sliku(screen, self.x, self.y, self.walking_pictures[self.walking_picture_index], flip)        
        elif self.state == STATE_JUMP:
            self.walking_last_updated = 0
            nacrtaj_sliku(screen, self.x, self.y, self.jumping_picture, flip)