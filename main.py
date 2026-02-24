import pygame
from sys import exit
pygame.init()

screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Runner")
# Pour les FPS
clock = pygame.time.Clock()
test_font = pygame.font.Font("font/Pixeltype.ttf", 50)

sky_surface = pygame.image.load("graphics/Sky.png").convert()
ground_surface = pygame.image.load("graphics/ground.png").convert()
#Antialisa en False puisque on va faire du pixel art sinon cest mieux de le mettre en True dans les autres cas
text_surface = test_font.render("My game", False, "Black")

snail_surf = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
snail_rect = snail_surf.get_rect(midbottom=(600,300))


player_surf = pygame.image.load("graphics/player/player_walk_1.png").convert_alpha()
player_rect = player_surf.get_rect(midbottom=(80,300))
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

    snail_rect.x -= 4
    if snail_rect.right <= 0:
        snail_rect.left = 800



    screen.blit(snail_surf,snail_rect)
    screen.blit(player_surf,player_rect)

    if player_rect.colliderect(snail_rect):
        print("Collision")




    pygame.display.update()
    # MAX 60 image par seconde
    clock.tick(60)