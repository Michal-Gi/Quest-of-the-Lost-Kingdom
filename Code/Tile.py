import pygame


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups, sprite_type):
        super().__init__(groups)
        self.sprite_type = sprite_type
        self.image = surf
        self.rect = self.image.get_rect(topleft=pos)
