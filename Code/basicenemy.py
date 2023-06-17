import pygame
import time


def calculate_distance(position1, position2):
    return pygame.math.Vector2(position2) - pygame.math.Vector2(position1)


class BasicEnemy(pygame.sprite.Sprite):
    enemy_list = []

    def __init__(self, pos, groups, speed, chase_range):
        super().__init__(groups)
        #self.image = pygame.image.load('../Assets/Characters/Enemies/testenemy.png').convert_alpha()
        self.image = pygame.image.load('../Assets/Characters/Enemies/skeleton16bit.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)

        self.direction = pygame.math.Vector2()
        self.speed = speed
        self.sprint = 1.0
        self.timer = time.time()
        self.chase_range = chase_range
        self.focus = False
        BasicEnemy.enemy_list.append(self)

    def set_focus(self, focus):
        self.focus = focus

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


    #def update(self):
     #   self.move_left_right()
      #  self.random_movement()
       # if self.focus:
        #    print("Enemy is focusing on the player.")

    def update(self, player_position):
        self.move_left_right()
        self.random_movement()

        distance = calculate_distance(self.rect.center, player_position)
        if distance <= self.chase_range:
            self.set_focus(True)
        else:
            self.set_focus(False)

        if self.focus:
            print("Enemy is focusing on the player.")

