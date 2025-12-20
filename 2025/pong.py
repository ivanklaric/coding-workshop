import pygame

pygame.init()

clock = pygame.time.Clock() 

RACKET_HEIGHT = 100
RACKET_WIDTH = 30
BACKGROUND_COLOR = (18, 59, 13)
RACKET_COLOR = (255, 255, 255)

left_racket_y = 768 // 2 - RACKET_HEIGHT // 2
right_racket_y = 768 // 2 - RACKET_HEIGHT // 2
ball_x = 512
ball_y = 384
ball_speed_x = 3
ball_speed_y = 3
left_player_score = 0
right_player_score = 0

screen = pygame.display.set_mode((1024, 768))
pygame.display.set_caption("Pong!")
font = pygame.font.Font(None, 36)  # None = default font, 36 = size

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        left_racket_y -= 10
    if keys[pygame.K_s]:
        left_racket_y += 10
    if keys[pygame.K_UP]:
        right_racket_y -= 10
    if keys[pygame.K_DOWN]:
        right_racket_y += 10

    # move the ball according to the speed
    ball_x = ball_x + ball_speed_x
    ball_y = ball_y + ball_speed_y


    # check if the ball reached left or right edge of the screen
    if ball_x > 1024-15 or ball_x < 15:
        ball_speed_x = -ball_speed_x
        if ball_x > 1024-15:
            left_player_score += 1
        if ball_x < 15:
            right_player_score += 1
        
    # check if the ball reached top or bottom of the screen
    if ball_y > 765-15 or ball_y < 15:
        ball_speed_y = -ball_speed_y


    # make sure the rackets can't fall off the screen
    if left_racket_y < 0:
        left_racket_y = 0
    if left_racket_y > 668:
        left_racket_y = 668
    if right_racket_y < 0:
        right_racket_y = 0
    if right_racket_y > 668:
        right_racket_y = 668

    # check if the ball collided with the racket
    left_racket = pygame.Rect(0, left_racket_y, RACKET_WIDTH, RACKET_HEIGHT)
    right_racket = pygame.Rect(1024-RACKET_WIDTH, right_racket_y, RACKET_WIDTH, RACKET_HEIGHT)
    ball_rect = pygame.Rect(ball_x-15 , ball_y-15 ,30, 30)

    if ball_rect.colliderect(left_racket):
        ball_speed_x = 3
    if ball_rect.colliderect(right_racket):
        ball_speed_x = -3

    # Fill the screen with the background color (Green)
    screen.fill( BACKGROUND_COLOR )     
    # Draw the left racket
    pygame.draw.rect(screen, RACKET_COLOR, left_racket)
    # Draw the right racket
    pygame.draw.rect(screen, RACKET_COLOR, right_racket)
    # Draw the ball
    pygame.draw.circle(screen, RACKET_COLOR, (ball_x, ball_y), 15)
    # Draw the net
    pygame.draw.line(screen, RACKET_COLOR, (512, 0), (512, 768))

    score_text = font.render(f" {left_player_score}   {right_player_score}", True, RACKET_COLOR)
    screen.blit(score_text, (480, 5))



    pygame.display.flip()
    clock.tick(60)

pygame.quit()