import pygame


class Tile(pygame.sprite.Sprite):
    """
        Klasa Tile reprezentuje pojedynczy element (kafel, płytka) w grze, dziedzicząc po klasie Sprite z modułu pygame.

        Atrybuty:
            image (Surface): Powierzchnia reprezentująca obraz kafelka.
            rect (Rect): Prostokątny obszar pokrywający obraz.
            mask (Mask): Obiekt maski używany do precyzyjnej detekcji kolizji.

        Metody:
            __init__(self, pos, surf, groups): Inicjalizuje obiekt Tile, ustawia jego obraz, obszar i maskę.
        """
    def __init__(self, pos, surf, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(topleft=pos)
        self.mask = pygame.mask.from_surface(surf)
