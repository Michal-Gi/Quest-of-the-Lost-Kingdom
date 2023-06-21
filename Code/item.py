import pygame, SpriteSheet, random

class item(pygame.sprite.Sprite):
    item_list = []

    def __init__(self, groups, name, pos=None):
        super().__init__(groups)
        if pos is None:
            x = random.randint(0, 768)
            y = random.randint(0, 432)
            self.pos = (x, y)
        else:
            self.pos = pos
        self.name = name
        # if self.name == 'coin':
        #     self.scale = 0.5
        # else:
        #     self.scale = 1
        self.image = pygame.image.load(f'../Assets/Items/{self.name}.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (16, 16))
        self.rect = self.image.get_rect(topleft=self.pos)
        self.direction = pygame.math.Vector2()
        self.collected = False
        item.item_list.append(self)

    def checkifcollected(self, player):
        player_pos = pygame.math.Vector2(player.rect.x, player.rect.y)
        itemp_pos = pygame.math.Vector2(self.rect.x, self.rect.y)

        distance = player_pos.distance_to(itemp_pos)

        if distance < 30 and not self.collected:
            self.collected = True
            if self.name == 'coin':
                player.coininventory.append(self)
                player.speed += 1
            if self.name == 'potion':
                player.potioninventory.append(self)
                if player.hp != player.maxhp:
                    player.hp += 20
            self.kill()

