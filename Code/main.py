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
enemy_sprite_group = pygame.sprite.Group()
object_group = pygame.sprite.Group()
item_sprite_group = pygame.sprite.Group()
pygame.mixer.init()
pygame.mixer.music.load("../Assets/music/Casual game track.mp3")

chosen = False
while not chosen:
    avatar = input('Wybierz postać.\nPostacie do wyboru: guy, robe\n')
    if avatar == 'guy' or avatar == 'robe':
        chosen = True
        if avatar == 'guy':
            avatar = ''
        else:
            avatar = 'r'
    else:
        print('nie rozpoznano postaci')

running = True
gracz = Player(pos=(400,300), groups=character_sprite_group, speed=2.5, animation_speed=0.5, scale=0.75, obstacles=object_group, enemies=enemy_sprite_group, hp=100, mp=10, stamina=10, damage=30, avatar=avatar)
current_level = Map(tmx_data=background_tmx_data, background_sprite_group=background_sprite_group, character_sprite_group=character_sprite_group, object_group=object_group, enemy_sprite_group=enemy_sprite_group, player=gracz, item_sprite_group=item_sprite_group)
enemy = BasicEnemy(pos=(100, 300), groups=enemy_sprite_group, speed=1, chase_range=80, scale=0.75, animation_speed=0.2, player=gracz, obstacles=object_group, charactersprite=character_sprite_group, hp=100, mp=10, stamina=10, damage=20)
enemy1 = BasicEnemy(pos=(200, 350), groups=enemy_sprite_group, speed=1, chase_range=80, scale=0.75, animation_speed=0.2, player=gracz, obstacles=object_group, charactersprite=character_sprite_group, hp=100, mp=10, stamina=10, damage=20)
enemy2 = BasicEnemy(pos=(200, 200), groups=enemy_sprite_group, speed=1, chase_range=80, scale=0.75, animation_speed=0.2, player=gracz, obstacles=object_group, charactersprite=character_sprite_group, hp=100, mp=10, stamina=10, damage=20)

item1 = item(groups=item_sprite_group, name='coin')
item2 = item(groups=item_sprite_group, name='coin')
item3 = item(groups=item_sprite_group, name='coin')
item4 = item(groups=item_sprite_group, name='potion')
item5 = item(groups=item_sprite_group, name='potion')
item6 = item(groups=item_sprite_group, name='potion')


pygame.mixer.music.play(-1)
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
    hp_pct = gracz.hp / 100
    gracz.draw_hp_bar(screen, 20, 20)
    gracz.draw_coininventory(screen, 150, 10)
    gracz.draw_potioninventory(screen, 150, 35)
    for allenemies in BasicEnemy.enemy_list:
        allenemies.update()
        allenemies.chaseplayer(gracz)
    # flip() the display to put your work on screen
    for allitems in item.item_list:
        allitems.checkifcollected(gracz)
    pygame.display.flip()

    if gracz.current_state == 'fall' and gracz.elapsed_time >=5:
        break
    clock.tick(60)  # limits FPS to 60

pygame.quit()