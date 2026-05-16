import pygame

pygame.init()

screen = pygame.display.set_mode((768, 1024))
pygame.display.set_caption("Pacman!")


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the labyrinth boundaries
    pygame.draw.line(screen, "BLUE", (9, 174), (759, 174), 2)
    pygame.draw.line(screen, "BLUE", (9, 174), (9, 924), 2)
    pygame.draw.line(screen, "BLUE", (9, 924), (759, 924), 2)
    pygame.draw.line(screen, "BLUE", (759, 174), (759, 924), 2)

    pygame.display.flip()

pygame.quit()