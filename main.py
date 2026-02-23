import pygame
from sys import exit
pygame.init()

screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Runner")
# Pour les FPS
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


    pygame.display.update()
    # MAX 60 image par seconde
    clock.tick(60)