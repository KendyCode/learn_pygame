import pygame
from sys import exit

from sqlalchemy import false

pygame.init()

screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Runner")
# Pour les FPS
clock = pygame.time.Clock()
test_font = pygame.font.Font("font/Pixeltype.ttf", 50)
game_active = True

sky_surface = pygame.image.load("graphics/Sky.png").convert()
ground_surface = pygame.image.load("graphics/ground.png").convert()
#Antialisa en False puisque on va faire du pixel art sinon cest mieux de le mettre en True dans les autres cas
score_surf = test_font.render("My game", False, (64,64,64))
score_rect = score_surf.get_rect(center=(400,50))

snail_surf = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
snail_rect = snail_surf.get_rect(midbottom=(600,300))


player_surf = pygame.image.load("graphics/player/player_walk_1.png").convert_alpha()
player_rect = player_surf.get_rect(midbottom=(80,300))
player_gravity = 0

# Pour que la fenetre reste ouverte
while True:

    for event in pygame.event.get():
        #Pour fermer la fenetre
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos) and player_rect.bottom >= 300:
                    player_gravity = -20
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                    player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                snail_rect.left = 800

    if game_active:
        # Pour mettre une surface sur une autre surface
        screen.blit(sky_surface,(0,0))
        screen.blit(ground_surface,(0,300))
        pygame.draw.rect(screen,"#c0e8ec", score_rect)
        pygame.draw.rect(screen,"#c0e8ec", score_rect,10)

        screen.blit(score_surf,score_rect)

        snail_rect.x -= 4
        if snail_rect.right <= 0: snail_rect.left = 800
        screen.blit(snail_surf,snail_rect)

        # Player
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300: player_rect.bottom = 300
        screen.blit(player_surf,player_rect)

        # collision
        if snail_rect.colliderect(player_rect):
            game_active = False
    else:
        screen.fill("#c0e8ec")

    pygame.display.update()
    # MAX 60 image par seconde
    clock.tick(60)