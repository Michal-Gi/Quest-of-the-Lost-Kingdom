import pygame

class SpriteSheet:
    def __init__(self, filename):
        self.spritesheet = pygame.image.load(filename).convert()


    def get_image(self, frame):
        image = self.spritesheet.subsurface(pygame.Rect(frame))
        return image