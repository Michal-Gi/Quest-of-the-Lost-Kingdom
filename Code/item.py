import pygame, SpriteSheet, random

class item(pygame.sprite.Sprite):
    """
        Klasa item reprezentuje poszczególne przedmioty w grze. Klasa ta rozszerza klasę pygame.sprite.Sprite
        i jest używana do inicjowania, umieszczania, skalowania i kontrolowania różnych typów przedmiotów
        w grze. Każda instancja przedmiotu śledzi swój własny stan i właściwości.

        Atrybuty Klasy:
            item_list: Lista, która przechowuje wszystkie instancje przedmiotów stworzone z tej klasy.

        Atrybuty:
            groups (pygame.sprite.Group): Grupa, do której należy sprite.
            name (str): Nazwa przedmiotu.
            pos (tuple): Opcjonalnie; początkowa pozycja przedmiotu w przestrzeni 2D. Jeśli nie jest podana,
                         przypisywana jest losowa pozycja.
            image (pygame.Surface): Powierzchnia reprezentująca obraz przedmiotu.
            rect (pygame.Rect): Obiekt z atrybutami szerokość, wysokość, x, y dla przedmiotu.
            direction (pygame.math.Vector2): Kierunek przedmiotu.
            collected (bool): Czy przedmiot został zebrany.

        Metody:
            checkifcollected(self, player): Metoda sprawdza, czy przedmiot został zebrany przez gracza.
                                            Jeśli tak, następuje zmiana stanu przedmiotu oraz właściwości gracza.
        """
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

