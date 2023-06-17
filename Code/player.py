import pygame
from SpriteSheet import SpriteSheet
from os import path
# from settings import *


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, speed, animation_speed, scale):
        super().__init__(groups)
        self.state_animation_frames = { 'idle' : 2, 'sword' : 6, 'bow' : 13, 'spear' : 8, 'fall' : 6}
        self.current_state = 'idle'
        self.scale = scale
        self.elapsed_time = 0
        self.animation_speed = animation_speed
        self.back_frame = (0, 0, 64, 64)
        self.left_frame = (0, 64, 64, 64)
        self.front_frame = (0, 128, 64, 64)
        self.right_frame = (0, 192, 64, 64)
        self.current_frame = self.front_frame
        self.load('../Assets/Characters/Player/idle1.png', scale)
        self.rect = self.image.get_rect(topleft=pos)
        self.direction = pygame.math.Vector2()
        self.speed = speed
        self.sprint = 1.0


    def load(self, path, scale):
        spritesheet = SpriteSheet(path)
        self.image = SpriteSheet.get_image(spritesheet, self.current_frame)
        self.image = pygame.transform.scale(self.image, (64*scale, 64*scale))

    def input(self):
        keys = pygame.key.get_pressed()

        # movement
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

        # animations
        if keys[pygame.K_SPACE]:
            self.current_state = 'spear'
        else:
            self.current_state = 'idle'




    def move(self, speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
        self.rect.center += self.direction * speed * self.sprint

    def update(self):
        self.input()
        if self.direction.x == 1:
            self.current_frame = self.right_frame
        elif self.direction.x == -1:
            self.current_frame = self.left_frame
        elif self.direction.y == -1:
            self.current_frame = self.back_frame
        else:
            self.current_frame = self.front_frame

        self.elapsed_time += self.animation_speed

        frame = int(self.elapsed_time % self.state_animation_frames.get(self.current_state))
        self.load(f'../Assets/Characters/Player/{self.current_state}{1 + frame}.png', scale=self.scale)
        self.move(self.speed)
