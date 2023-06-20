import pygame
from player import Player
from Map import Map
from basicenemy import BasicEnemy
import sys
from item import item
from pytmx.util_pygame import load_pygame


pygame.init()
screen = pygame.display.set_mode((768, 432), pygame.FULLSCREEN)
clock = pygame.time.Clock()
background_tmx_data = load_pygame('../Assets/Starting-Location.tmx')
background_sprite_group = pygame.sprite.Group()
character_sprite_group = pygame.sprite.Group()
object_group = pygame.sprite.Group()

running = True
gracz = Player(pos=(400,300), groups=character_sprite_group, speed=2, animation_speed=0.2, scale=0.75, obstacles=object_group)
current_level = Map(tmx_data=background_tmx_data, background_sprite_group=background_sprite_group, character_sprite_group=character_sprite_group, object_group=object_group)
enemy = BasicEnemy(pos=(100, 300), groups=character_sprite_group, speed=1, chase_range=80, scale=0.75, animation_speed=0.2, player=gracz)
enemy1 = BasicEnemy(pos=(100, 330), groups=character_sprite_group, speed=1, chase_range=80, scale=0.75, animation_speed=0.2, player=gracz)
enemy2 = BasicEnemy(pos=(100, 360), groups=character_sprite_group, speed=1, chase_range=80, scale=0.75, animation_speed=0.2, player=gracz)

item1 = item(groups=character_sprite_group)


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
    for allenemies in BasicEnemy.enemy_list:
        allenemies.update()
        allenemies.chaseplayer(gracz)
    # flip() the display to put your work on screen
    item1.checkifcollected(gracz)
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()