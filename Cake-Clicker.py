import pygame
pygame.init()
blue = (12, 43, 78)

screen = pygame.display.set_mode(500, 650)
pygame.display.set_caption("Cake Clicker")
background = blue
framerate = 60
font = pygame.font.Font('Courier')
timer = pygame.time.Clock()

def draw_task(color, y_coord):
    pygame.draw.circle(screen, color, (50, y_coord), 20, 5)
    pygame.draw.rect(screen, color, (70, y_coord - 15), 20, 5)

running = True
while running:
    timer.tick(framerate)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(background)

    screen.display.flip()

pygame.quit()