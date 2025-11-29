import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 600, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Board
BOARD = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]

def draw_board():
    # Draw vertical lines
    pygame.draw.line(SCREEN, BLACK, (200, 0), (200, 600), 4)
    pygame.draw.line(SCREEN, BLACK, (400, 0), (400, 600), 4)
    # Draw horizontal lines
    pygame.draw.line(SCREEN, BLACK, (0, 200), (600, 200), 4)
    pygame.draw.line(SCREEN, BLACK, (0, 400), (600, 400), 4)

def draw_symbols():
    for row in range(3):
        for col in range(3):
            if BOARD[row][col] == 1:  # O
                pygame.draw.circle(SCREEN, BLUE, (col * 200 + 100, row * 200 + 100), 60, 4)
            elif BOARD[row][col] == 2:  # X
                pygame.draw.line(SCREEN, RED, (col * 200 + 50, row * 200 + 50), 
                                 (col * 200 + 150, row * 200 + 150), 4)
                pygame.draw.line(SCREEN, RED, (col * 200 + 150, row * 200 + 50), 
                                 (col * 200 + 50, row * 200 + 150), 4)

def check_winner():
    # Check rows and columns
    for i in range(3):
        if BOARD[i][0] == BOARD[i][1] == BOARD[i][2] != 0:
            return BOARD[i][0]
        if BOARD[0][i] == BOARD[1][i] == BOARD[2][i] != 0:
            return BOARD[0][i]
    
    # Check diagonals
    if BOARD[0][0] == BOARD[1][1] == BOARD[2][2] != 0:
        return BOARD[0][0]
    if BOARD[0][2] == BOARD[1][1] == BOARD[2][0] != 0:
        return BOARD[0][2]
    
    # Check for tie
    if all(BOARD[i][j] != 0 for i in range(3) for j in range(3)):
        return 3  # Tie
    
    return 0  # No winner yet

def display_winner(winner):
    font = pygame.font.Font(None, 74)
    if winner == 1:
        text = font.render("O Wins!", True, BLUE)
    elif winner == 2:
        text = font.render("X Wins!", True, RED)
    else:
        text = font.render("It's a Tie!", True, BLACK)
    text_rect = text.get_rect(center=(WIDTH//2, HEIGHT//2))
    SCREEN.blit(text, text_rect)
    pygame.display.flip()
    pygame.time.wait(3000)  # Wait for 3 seconds

# Game loop
running = True
current_player = 1
winner = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and winner == 0:
            mouseX, mouseY = pygame.mouse.get_pos()
            clicked_row = mouseY // 200
            clicked_col = mouseX // 200
            if BOARD[clicked_row][clicked_col] == 0:
                BOARD[clicked_row][clicked_col] = current_player
                winner = check_winner()
                if winner == 0:
                    current_player = 3 - current_player  # Switch player (1 -> 2, 2 -> 1)

    SCREEN.fill(WHITE)
    draw_board()
    draw_symbols()
    
    if winner != 0:
        display_winner(winner)
        # Reset the game
        BOARD = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        current_player = 1
        winner = 0

    pygame.display.flip()

pygame.quit()
sys.exit()