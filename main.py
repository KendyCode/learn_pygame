import pygame
from sys import exit
pygame.init()

screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Runner")
# Pour les FPS
clock = pygame.time.Clock()
test_font = pygame.font.Font("font/Pixeltype.ttf", 50)

sky_surface = pygame.image.load("graphics/Sky.png")
ground_surface = pygame.image.load("graphics/ground.png")
#Antialisa en False puisque on va faire du pixel art sinon cest mieux de le mettre en True dans les autres cas
text_surface = test_font.render("My game", False, "Black")
# Pour que la fenetre reste ouverte
while True:

    for event in pygame.event.get():
        #Pour fermer la fenetre
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Pour mettre une surface sur une autre surface

    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,300))
    screen.blit(text_surface,(300,50))



    pygame.display.update()
    # MAX 60 image par seconde
    clock.tick(60)