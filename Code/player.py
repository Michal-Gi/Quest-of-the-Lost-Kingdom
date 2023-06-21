import pygame
from SpriteSheet import SpriteSheet
from Character import Character
from item import item
from os import path
# from settings import *


class Player(Character, pygame.sprite.Sprite):
    def __init__(self, pos, groups, speed, animation_speed, scale, obstacles, enemies, hp, mp, stamina, damage, avatar):
        Character.__init__(self, hp=hp, mp=mp, stamina=stamina, damage=damage)
        pygame.sprite.Sprite.__init__(self, groups)
        # animations
        self.state_animation_frames = { 'idle': 2, 'sword': 6, 'bow': 13, 'spear': 8, 'fall': 6, 'walk': 9}
        self.current_state = 'idle'
        self.elapsed_time = 0
        self.animation_speed = animation_speed
        self.in_action = False
        self.action_cooldown_times = {'idle': 0, 'sword': 200, 'bow': 500, 'spear': 700, 'fall': 200}
        self.action_time = None
        # rendering
        self.scale = scale
        self.back_frame = (0, 0, 64, 64)
        self.left_frame = (0, 64, 64, 64)
        self.front_frame = (0, 128, 64, 64)
        self.right_frame = (0, 192, 64, 64)
        self.current_frame = self.front_frame
        self.load('../Assets/Characters/Player/idle1.png', scale)
        self.rect = self.image.get_rect(topleft=pos)
        self.mask = pygame.mask.from_surface(self.image)
        # movement
        self.direction = pygame.math.Vector2()
        self.speed = speed
        self.sprint = 1.0
        self.obstacles = obstacles
        self.enemies = enemies
        self.avatar = avatar
        self.maxhp = hp
        self.coininventory = []
        self.potioninventory = []
        self.fontpath = '../Font/PressStart2P.ttf'


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

        # run
        if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
            self.sprint = 3
        else:
            self.sprint = 1.0

        # attack
        if keys[pygame.K_SPACE] and not self.in_action:
            self.elapsed_time = 0
            self.current_state = 'spear'
            self.in_action = True
            self.action_time = pygame.time.get_ticks()


    def collision(self):
        # horizontal movement
        for sprite in self.obstacles:
            if pygame.sprite.spritecollide(self, [sprite], False, pygame.sprite.collide_mask):
                if self.direction.x > 0 > self.rect.centerx - sprite.rect.centerx:
                    if self.direction.y > 0:
                        for sprite2 in self.obstacles:
                            if sprite2.rect.collidepoint(self.rect.midbottom):
                                self.direction.y = 0
                    elif self.direction.y < 0:
                        for sprite2 in self.obstacles:
                            if sprite2.rect.collidepoint(self.rect.midtop):
                                self.direction.y = 0
                    self.direction.x = 0
                elif self.direction.x < 0 < self.rect.centerx - sprite.rect.centerx:
                    if self.direction.y > 0:
                        for sprite2 in self.obstacles:
                            if sprite2.rect.collidepoint(self.rect.midbottom):
                                self.direction.y = 0
                    elif self.direction.y < 0:
                        for sprite2 in self.obstacles:
                            if sprite2.rect.collidepoint(self.rect.midtop):
                                self.direction.y = 0
                    self.direction.x = 0
                else:
                    if self.direction.y > 0 > self.rect.centery - sprite.rect.centery:
                        if self.direction.x > 0 > self.rect.centerx - sprite.rect.centerx:
                            for sprite2 in self.obstacles:
                                if sprite2.rect.collidepoint(self.rect.midright):
                                    self.direction.x = 0
                        elif self.direction.x < 0 < self.rect.centerx - sprite.rect.centerx:
                            for sprite2 in self.obstacles:
                                if sprite2.rect.collidepoint(self.rect.midleft):
                                    self.direction.x = 0
                        self.direction.y = 0
                    elif self.direction.y < 0 < self.rect.centery - sprite.rect.centery:
                        if self.direction.x > 0 > self.rect.centerx - sprite.rect.centerx:
                            for sprite2 in self.obstacles:
                                if sprite2.rect.collidepoint(self.rect.midright):
                                    self.direction.x = 0
                        elif self.direction.x < 0 < self.rect.centerx - sprite.rect.centerx:
                            for sprite2 in self.obstacles:
                                if sprite2.rect.collidepoint(self.rect.midleft):
                                    self.direction.x = 0
                        self.direction.y = 0


        for sprite in self.enemies:
            if pygame.sprite.spritecollide(self, [sprite], False, pygame.sprite.collide_mask):
                if self.current_state == 'walk' or self.current_state == 'idle':
                    self.get_hurt(sprite.damage)
                    if self.hp <= 0:
                        self.current_state = 'fall'
                        sprite.get_hurt(10000)
            if self.rect.colliderect(sprite) and self.current_state == 'spear':
                sprite.get_hurt(self.damage)
                print(sprite.hp)


    def draw_hp_bar(self, surface, x, y):
        if self.hp < 0:
            self.hp = 0
        bar_length = 100
        bar_height = 20
        pct = self.hp / self.maxhp
        fill = pct * bar_length
        outline_rect = pygame.Rect(x, y, bar_length, bar_height)
        fill_rect = pygame.Rect(x, y, fill, bar_height)
        pygame.draw.rect(surface, (255, 0, 0), fill_rect)
        pygame.draw.rect(surface, (255, 255, 255), outline_rect, 2)

    def draw_coininventory(self, surface, x, y):
        font = pygame.font.Font(self.fontpath, 12)
        text = font.render(f'Coins collected: {len(self.coininventory)}', True, (255, 255, 255))
        surface.blit(text, (x, y))

    def draw_potioninventory(self, surface, x, y):
        font = pygame.font.Font(self.fontpath, 12)
        text = font.render(f'Potions collected: {len(self.potioninventory)}', True, (255, 255, 255))
        surface.blit(text, (x, y))




    def move(self, speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        self.collision()
        self.rect.centerx += self.direction.x * speed * self.sprint
        self.rect.centery += self.direction.y * speed * self.sprint

    def update(self):
        self.input()
        # character rotation
        if self.direction.x == 1:
            self.current_frame = self.right_frame
        elif self.direction.x == -1:
            self.current_frame = self.left_frame
        elif self.direction.y == -1:
            self.current_frame = self.back_frame
        elif self.direction.y == 1:
            self.current_frame = self.front_frame

        if self.current_state == 'fall':
            self.current_frame = self.back_frame

        if self.current_state != 'fall':
            if (self.direction.x != 0 or self.direction.y != 0) and not self.in_action:
                self.current_state = 'walk'
            elif self.direction.x == 0 and self.direction.y == 0 and not self.in_action:
                self.current_state = 'idle'

        self.elapsed_time += self.animation_speed

        frame = int(self.elapsed_time % self.state_animation_frames.get(self.current_state))
        self.load(f'../Assets/Characters/Player/{self.avatar}{self.current_state}{1 + frame}.png', scale=self.scale)
        if self.current_state != 'fall':
            self.move(self.speed)

        self.cooldowns(self.current_state)


        self.immunity_time = max(self.immunity_time - 1, 0)
        # print(self.rect.center)

    def cooldowns(self, action):
        current_time = pygame.time.get_ticks()

        if self.in_action:
            if current_time - self.action_time >= self.action_cooldown_times.get(action):
                self.in_action = False
                self.current_state = 'idle'
                self.elapsed_time = 0
