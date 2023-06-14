import pygame
# from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, speed):
        super().__init__(groups)
        self.image = pygame.image.load('C:/Users/s24333/PycharmProjects/Quest-of-the-Lost-Kingdom/Assets/Characters/Player/sorlo.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)

        self.direction = pygame.math.Vector2()
        self.speed = speed
        self.sprint = 1.0

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.direction.y = -1
        elif keys[pygame.K_s]:
            self.direction.y = 1
        else:
            self.direction.y = 0

        if keys[pygame.K_a]:
            self.direction.x = -1
        elif keys[pygame.K_d]:
            self.direction.x = 1
        else:
            self.direction.x = 0

        if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
            self.sprint = 3
        else:
            self.sprint = 1.0




    def move(self, speed):
        self.rect.center += self.direction * speed * self.sprint

    def update(self):
        self.input()
        self.move(self.speed)
