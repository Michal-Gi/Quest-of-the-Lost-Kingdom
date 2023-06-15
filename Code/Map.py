import pygame, Tile

class Map:
    def __init__(self, tmx_data, background_sprite_group, character_sprite_group):

        self.background_sprite_group = background_sprite_group
        self.character_sprite_group = character_sprite_group
        for layer in tmx_data.layers:
            if hasattr(layer, 'data'):
                for x, y, surf in layer.tiles():
                    pos = (x * 16, y * 16)
                    Tile.Tile(pos=pos, surf=surf, groups=self.background_sprite_group)

    def draw_map(self, screen):
        self.background_sprite_group.draw(screen)
        self.character_sprite_group.draw(screen)
        self.character_sprite_group.update()
