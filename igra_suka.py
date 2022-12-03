import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Flexer")
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)

sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()
text_surface = test_font.render('Flexer the game', False, 'black')
score_rect = text_surface.get_rect(center=(400, 50))

snail_surface = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
snail_rectangle = snail_surface.get_rect(bottomright=(700, 300))

player_surface = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rectangle = player_surface.get_rect(midbottom=(80, 300))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # if event.type == pygame.MOUSEMOTION:
        #     if player_rectangle.collidepoint(event.pos):
        #         print("collisions11")
    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    screen.blit(text_surface, (score_rect))
    snail_rectangle.x -= 4
    if snail_rectangle.right <= 0: snail_rectangle.left = 800
    screen.blit(snail_surface, snail_rectangle)
    screen.blit(player_surface, player_rectangle)

    # # if player_rectangle.colliderect(snail_rectangle):
    # #     print("col")
    # mouse_pos = pygame.mouse.get_pos()
    # if player_rectangle.collidepoint(mouse_pos):
    #     print("collision")

    pygame.display.update()
    clock.tick(60)
