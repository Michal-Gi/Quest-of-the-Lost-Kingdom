import pygame

class SpriteSheet:
    """
        Klasa SpriteSheet służy do obsługi arkusza sprite'ów (obrazka zawierającego wiele mniejszych obrazków,
        zazwyczaj stanowiących klatki animacji).

        Atrybuty:
            spritesheet (Surface): Powierzchnia zawierająca obraz arkusza sprite'ów.

        Metody:
            __init__(self, filename): Inicjalizuje obiekt SpriteSheet, wczytując obraz arkusza sprite'ów z pliku.
            get_image(self, frame): Zwraca konkretny sprite (obrazek) z arkusza na podstawie podanej ramki.
        """
    def __init__(self, filename):
        self.spritesheet = pygame.image.load(filename).convert()


    def get_image(self, frame):
        image = self.spritesheet.subsurface(pygame.Rect(frame))
        return image