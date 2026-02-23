import pygame
from sys import exit
pygame.init()

screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Runner")
# Pour les FPS
clock = pygame.time.Clock()

test_surface = pygame.Surface((100,200))
test_surface.fill("Red")

# Pour que la fenetre reste ouverte
while True:

    for event in pygame.event.get():
        #Pour fermer la fenetre
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Pour mettre une surface sur une autre surface
    screen.blit(test_surface,(200,100))


    pygame.display.update()
    # MAX 60 image par seconde
    clock.tick(60)