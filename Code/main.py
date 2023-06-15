import pygame, player, Map
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
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()