import pygame, SpriteSheet
import time
import random



class BasicEnemy(pygame.sprite.Sprite):
    enemy_list = []

    def __init__(self, pos, groups, speed, chase_range, scale, animation_speed, player):
        super().__init__(groups)
        self.scale = scale
        self.current_state = 'idle'
        self.elapsed_time = 0
        self.animation_speed = animation_speed
        self.back_frame = (0, 0, 64, 64)
        self.left_frame = (0, 64, 64, 64)
        self.front_frame = (0, 128, 64, 64)
        self.right_frame = (0, 192, 64, 64)
        self.current_frame = self.front_frame
        self.image = pygame.image.load('../Assets/Characters/Enemies/skeleton16bit.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.direction = pygame.math.Vector2()
        self.speed = speed
        self.sprint = 1.0
        self.timer = time.time()
        self.chase_range = chase_range
        self.focus = False
        self.player = player
        BasicEnemy.enemy_list.append(self)

    def load(self, path, scale):
        spritesheet = SpriteSheet.SpriteSheet(path)
        self.image = SpriteSheet.SpriteSheet.get_image(spritesheet, self.current_frame)
        self.image = pygame.transform.scale(self.image, (64*scale, 64*scale))


    def random_movement(self):
        elapsed_time = (time.time() - self.timer) % 2

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

    def move(self, speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
        self.rect.center += self.direction * speed * self.sprint

    def chaseplayer(self, player):
        player_pos = pygame.math.Vector2(player.rect.x, player.rect.y)
        enemy_pos = pygame.math.Vector2(self.rect.x, self.rect.y)

        distance = player_pos.distance_to(enemy_pos)
        if distance < self.chase_range:
            self.focus = True
        else:
            self.focus = False

        if self.focus:
            self.direction = player_pos - enemy_pos
            if self.direction.length() > 0:
                self.direction.normalize()
        else:
            self.random_movement()

    def update(self):

        if self.direction.x == 1:
            self.current_frame = self.right_frame
        elif self.direction.x == -1:
            self.current_frame = self.left_frame
        elif self.direction.y == -1:
            self.current_frame = self.back_frame
        else:
            self.current_frame = self.front_frame

        self.elapsed_time += self.animation_speed
        frame = int(self.elapsed_time % 9)
        self.load(f'../Assets/Characters/Enemies/skeleton_bow-{1 + frame}.png', scale=self.scale)
        self.move(self.speed)
