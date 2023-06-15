import pygame
import time


class BasicEnemy(pygame.sprite.Sprite):
    enemy_list = []

    def __init__(self, pos, groups, speed):
        super().__init__(groups)
        #self.image = pygame.image.load('../Assets/Characters/Enemies/testenemy.png').convert_alpha()
        self.image = pygame.image.load('../Assets/Characters/Enemies/skeleton16bit.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)

        self.direction = pygame.math.Vector2()
        self.speed = speed
        self.sprint = 1.0
        self.timer = time.time()
        BasicEnemy.enemy_list.append(self)


    def move_left_right(self):
        self.rect.center += self.direction * self.speed

    def random_movement(self):
        elapsed_time = time.time() - self.timer

        if elapsed_time < 0.5:
            self.direction = pygame.math.Vector2(-1, 0)
        elif elapsed_time < 1:
            self.direction = pygame.math.Vector2(0, 1)
        elif elapsed_time < 1.5:
            self.direction = pygame.math.Vector2(1, 0)
        elif elapsed_time < 2.0:
            self.direction = pygame.math.Vector2(0, -1)
        else:
            self.timer = time.time()
            self.direction.x = -1

    def update(self):
        self.move_left_right()
        self.random_movement()
