import pygame

# Initialize pygame
pygame.init()

# Create a window
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Hello Pygame!")

# Game loop
running = True
while running:
    # Check for close event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Fill screen with white
    screen.fill((255, 255, 255))
    
    # Draw "Hello World" text
    font = pygame.font.Font(None, 74)
    text = font.render("Hello World!", True, (0, 0, 0))
    text_rect = text.get_rect(center=(320, 240))
    screen.blit(text, text_rect)
    
    # Update display
    pygame.display.flip()

# Quit
pygame.quit()