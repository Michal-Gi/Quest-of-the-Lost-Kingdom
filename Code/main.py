import pygame, player, Map, basicenemy
import sys
from pytmx.util_pygame import load_pygame


pygame.init()
screen = pygame.display.set_mode((768, 432), pygame.FULLSCREEN)
clock = pygame.time.Clock()
background_tmx_data = load_pygame('../Assets/Starting-Location.tmx')
background_sprite_group = pygame.sprite.Group()
character_sprite_group = pygame.sprite.Group()

running = True
gracz = player.Player(pos=(100,200), groups=character_sprite_group, speed=5)
current_level = Map.Map(tmx_data=background_tmx_data, background_sprite_group=background_sprite_group, character_sprite_group=character_sprite_group)
enemy = basicenemy.BasicEnemy(pos=(100, 300), groups=character_sprite_group, speed=1)
enemy1 = basicenemy.BasicEnemy(pos=(100, 330), groups=character_sprite_group, speed=1)
enemy2 = basicenemy.BasicEnemy(pos=(100, 360), groups=character_sprite_group, speed=1)



while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # RENDER YOUR GAME HERE
    current_level.draw_map(screen=screen)
    for allenemies in basicenemy.BasicEnemy.enemy_list:
        allenemies.move_left_right()
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()