import pygame, SpriteSheet
from os import path
# from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, speed):
        super().__init__(groups)
        self.image = pygame.image.load('../Assets/Characters/Player/idle1.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)

        self.direction = pygame.math.Vector2()
        self.speed = speed
        self.sprint = 1.0


    def load(self):
        spritesheet = SpriteSheet.SpriteSheet('../Assets/Characters/Player/idle1.png')

        standing_front_frame = ()

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.direction.y = -1
        elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.direction.y = 1
        else:
            self.direction.y = 0

        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.direction.x = -1
        elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.direction.x = 1
        else:
            self.direction.x = 0

        if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
            self.sprint = 3
        else:
            self.sprint = 1.0


    def move(self, speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
        self.rect.center += self.direction * speed * self.sprint

    def update(self):
        self.input()
        self.move(self.speed)
