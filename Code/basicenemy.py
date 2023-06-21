import pygame, SpriteSheet
import time
from Character import Character
import random



class BasicEnemy(pygame.sprite.Sprite, Character):
    """
        Klasa BasicEnemy reprezentuje podstawowego wroga w grze. Klasa ta rozszerza klasy pygame.sprite.Sprite i Character.
        Wrogowie mają określone atrybuty, takie jak pozycja, grupa, prędkość, zasięg ścigania, skala, szybkość animacji,
        a także atrybuty dziedziczone z klasy Character.

        Atrybuty Klasy:
            enemy_list: Lista, która przechowuje wszystkie instancje wrogów stworzone z tej klasy.

        Atrybuty:
            pos (tuple): Początkowa pozycja wroga w przestrzeni 2D.
            groups (pygame.sprite.Group): Grupa, do której należy sprite.
            speed (float): Prędkość wroga.
            chase_range (int): Zasięg, w którym wróg zacznie ścigać gracza.
            scale (int): Skala wielkości wroga.
            animation_speed (int): Szybkość animacji wroga.
            player (object): Obiekt reprezentujący gracza.
            obstacles (pygame.sprite.Group): Grupa zawierająca przeszkody.
            charactersprite (str): Ścieżka do obrazka reprezentującego wroga.
            hp, mp, stamina, damage (int): Atrybuty dziedziczone z klasy Character.

        Metody:
            load(self, path, scale): Wczytuje sprite z podanej ścieżki i skaluje go.
            random_movement(self): Ustala losowy kierunek ruchu wroga.
            move(self, speed): Porusza wrogiem z określoną prędkością, z uwzględnieniem kolizji.
            chaseplayer(self, player): Wrog ściga gracza, jeśli ten znajduje się w zasięgu ścigania.
            collision(self): Sprawdza kolizje z przeszkodami i zatrzymuje wroga, jeśli takie wystąpią.
            update(self): Aktualizuje stan wroga - ładowanie odpowiedniego sprite'a, ruch, sprawdzanie czy wróg jest nadal "żywy".
        """
    enemy_list = []

    def __init__(self, pos, groups, speed, chase_range, scale, animation_speed, player, obstacles, charactersprite, hp, mp, stamina, damage):
        Character.__init__(self, hp=hp, mp=mp, stamina=stamina, damage=damage)
        pygame.sprite.Sprite.__init__(self, groups)
        self.scale = scale
        #self.current_state = 'idle'
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
        self.obstacles = obstacles
        self.charactersprite = charactersprite
        self.hp = hp
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

        self.collision()
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
        self.immunity_time = max(self.immunity_time - 1, 0)
        if self.hp <= 0:
            self.kill()
        frame = int(self.elapsed_time % 9)
        self.load(f'../Assets/Characters/Enemies/skeleton_bow-{1 + frame}.png', scale=self.scale)
        self.move(self.speed)
