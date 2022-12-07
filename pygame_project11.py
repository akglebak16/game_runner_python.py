import pygame
from sys import exit
import random


def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surface = test_font.render(f'QA Lessons: {current_time}', False, (64, 64, 64))
    score_rect = score_surface.get_rect(center=(400, 50))
    screen.blit(score_surface, score_rect)
    return current_time


def obsticle_movement(obsticle_list):
    if obsticle_list:
        for obsticle_rect in obsticle_list:
            obsticle_rect.x -= 5

            screen.blit(snail_surface, obsticle_rect)
        return obsticle_list
    else:
        return []

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Gena Rusov")
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)
game_active = True
start_time = 0
score = 0

sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()

# text_surface = test_font.render('Flexer the game', False, (61, 61, 61))
# score_rect = text_surface.get_rect(center=(400, 50))

snail_surface = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
snail_rectangle = snail_surface.get_rect(bottomright=(700, 300))

obsticle_tect_list = []

player_surface = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rectangle = player_surface.get_rect(midbottom=(80, 300))
player_gravity = 0
player_stand = pygame.image.load('graphics/player/player_stand.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
player_stand_rect = player_stand.get_rect(center=(400, 200))

game_name = test_font.render("NA ZAVOD!!!", False, (111, 196, 169))
game_name_rect = game_name.get_rect(center=(400, 80))

game_message = test_font.render("Press space to run", False, (11, 196, 169))
game_message_rect = game_message.get_rect(center=(400, 320))

# Timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 2000)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN and player_rectangle.bottom >= 300 and game_active:
                if player_rectangle.collidepoint(event.pos):
                    player_gravity = -20
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rectangle.bottom >= 300 and game_active:
                    player_gravity = -20
            if event.type == pygame.KEYUP:
                print('Key up')
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                snail_rectangle.left = 800
                start_time = int(pygame.time.get_ticks() / 1000)

        if event.type == obstacle_timer and game_active:
            obsticle_tect_list.append(snail_surface.get_rect(bottomright=(random.randint(900, 1100), 300)))

    if game_active:
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))
        # pygame.draw.rect(screen, "#c0e8ec", score_rect)
        # pygame.draw.rect(screen, "#c0e8ec", score_rect, 10)
        # # pygame.draw.ellipse(screen,"Brown",pygame.Rect(50,200,100,100))
        # screen.blit(text_surface, score_rect)

        # keys = pygame.key.get_pressed()
        # if keys[pygame.K_SPACE]:
        #     print("jump")
        score = display_score()
        snail_rectangle.x -= 6
        if snail_rectangle.right <= 0: snail_rectangle.left = 800
        screen.blit(snail_surface, snail_rectangle)
        # player
        player_gravity += 1
        player_rectangle.y += player_gravity

        if player_rectangle.bottom >= 300: player_rectangle.bottom = 300
        screen.blit(player_surface, player_rectangle)

        obsticle_tect_list = obsticle_movement(obsticle_tect_list)

        # collision
        if snail_rectangle.colliderect(player_rectangle):
            game_active = False
    else:
        screen.fill((94, 109, 162))
        screen.blit(player_stand, player_stand_rect)
        screen.blit(game_name, game_name_rect)
        # screen.blit(game_message,game_message_rect)
        score_message = test_font.render(f"Your Score:{score}", False, "Red")
        score_message_rect = score_message.get_rect(center=(400, 340))
        screen.blit(game_name, game_name_rect)

        if score == 0:
            screen.blit(game_message, game_message_rect)
        else:
            screen.blit(score_message, score_message_rect)
    # # if player_rectangle.colliderect(snail_rectangle):
    # #     print("col")
    # mouse_pos = pygame.mouse.get_pos()
    # if player_rectangle.collidepoint(mouse_pos):
    #     print("collision")

    pygame.display.update()
    clock.tick(60)
