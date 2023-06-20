import pygame, SpriteSheet, random

class item(pygame.sprite.Sprite):


    def __init__(self, groups, pos=None):
        super().__init__(groups)
        if pos is None:
            x = random.randint(0, 768)
            y = random.randint(0, 432)
            self.pos = (x, y)
        else:
            self.pos = pos
        self.image = pygame.image.load('../Assets/Characters/Enemies/skeleton16bit.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=self.pos)
        self.direction = pygame.math.Vector2()
        self.collected = False

    def checkifcollected(self, player):
        player_pos = pygame.math.Vector2(player.rect.x, player.rect.y)
        itemp_pos = pygame.math.Vector2(self.rect.x, self.rect.y)

        distance = player_pos.distance_to(itemp_pos)

        if distance < 50:
            self.collected = True
            self.kill()

