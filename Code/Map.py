import pygame
from Tile import Tile

class Map:
    def __init__(self, tmx_data, background_sprite_group, character_sprite_group, object_group, enemy_sprite_group, player, item_sprite_group):

        self.background_sprite_group = background_sprite_group
        self.character_sprite_group = character_sprite_group
        self.object_sprite_group = object_group
        self.enemy_sprite_group = enemy_sprite_group
        self.player = player
        self.item_sprite_group = item_sprite_group

        for layer in tmx_data.layers:
            print(layer.name)
            if hasattr(layer, 'data'):
                for x, y, surf in layer.tiles():
                    pos = (x * 16, y * 16)
                    if layer.name == 'Objects':
                        Tile(pos=pos, surf=surf, groups=self.object_sprite_group)
                    else:
                        Tile(pos=pos, surf=surf, groups=self.background_sprite_group)

    def draw_map(self, screen):
        self.object_sprite_group.draw(screen)
        self.background_sprite_group.draw(screen)
        self.enemy_sprite_group.draw(screen)
        self.item_sprite_group.draw(screen)
        self.character_sprite_group.draw(screen)
        self.item_sprite_group.update()
        self.enemy_sprite_group.update()
        self.character_sprite_group.update()

