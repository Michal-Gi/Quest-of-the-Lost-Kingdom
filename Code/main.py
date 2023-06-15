import pygame
import player
import basicenemy
import sys
from pytmx.util_pygame import load_pygame



class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(topleft=pos)

pygame.init()
screen = pygame.display.set_mode((768, 432), pygame.FULLSCREEN)
clock = pygame.time.Clock()
tmx_data = load_pygame('../Assets/Starting-Location.tmx')
sprite_group = pygame.sprite.Group()
visible_sprite = pygame.sprite.Group()
for layer in tmx_data.layers:
    if hasattr(layer, 'data'):
        for x,y,surf in layer.tiles():
            pos = (x * 16, y * 16)
            Tile(pos=pos, surf=surf, groups=sprite_group)
print(tmx_data.layers)
running = True
gracz = player.Player(pos=(100,200), groups=visible_sprite, speed=5)
enemy = basicenemy.BasicEnemy(pos=(100, 300), groups=visible_sprite, speed=1)
enemy1 = basicenemy.BasicEnemy(pos=(100, 330), groups=visible_sprite, speed=1)
enemy2 = basicenemy.BasicEnemy(pos=(100, 360), groups=visible_sprite, speed=1)



while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # RENDER YOUR GAME HERE
    sprite_group.draw(screen)
    visible_sprite.draw(screen)
    visible_sprite.update()

    for allenemies in basicenemy.BasicEnemy.enemy_list:
        allenemies.move_left_right()
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()