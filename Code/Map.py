import pygame
from Tile import Tile

class Map:
    """
       Klasa Map służy do reprezentowania mapy w grze. Mapa jest generowana na podstawie danych tmx (Tile Map XML).
       Klasa ta obsługuje różne grupy sprite'ów (tła, postaci, obiektów, przeciwników, przedmiotów) oraz gracza.

       Atrybuty:
           background_sprite_group (pygame.sprite.Group): Grupa sprite'ów reprezentujących tło mapy.
           character_sprite_group (pygame.sprite.Group): Grupa sprite'ów reprezentujących postacie na mapie.
           object_sprite_group (pygame.sprite.Group): Grupa sprite'ów reprezentujących obiekty na mapie.
           enemy_sprite_group (pygame.sprite.Group): Grupa sprite'ów reprezentujących przeciwników na mapie.
           player (object): Obiekt reprezentujący gracza.
           item_sprite_group (pygame.sprite.Group): Grupa sprite'ów reprezentujących przedmioty na mapie.

       Metody:
           __init__(self, tmx_data, background_sprite_group, character_sprite_group, object_group, enemy_sprite_group, player, item_sprite_group):
               Inicjalizuje obiekt Map na podstawie danych tmx oraz grup sprite'ów. Tworzy kafelki (Tiles) na podstawie tych danych.

           draw_map(self, screen):
               Rysuje mapę na ekranie. Rysuje wszystkie grupy sprite'ów oraz aktualizuje ich stan.
       """
    def __init__(self, tmx_data, background_sprite_group, character_sprite_group, object_group, enemy_sprite_group, player, item_sprite_group):

        self.background_sprite_group = background_sprite_group
        self.character_sprite_group = character_sprite_group
        self.object_sprite_group = object_group
        self.enemy_sprite_group = enemy_sprite_group
        self.player = player
        self.item_sprite_group = item_sprite_group

        for layer in tmx_data.layers:
            print(layer.name)
            if hasattr(layer, 'data'):
                for x, y, surf in layer.tiles():
                    pos = (x * 16, y * 16)
                    if layer.name == 'Objects':
                        Tile(pos=pos, surf=surf, groups=self.object_sprite_group)
                    else:
                        Tile(pos=pos, surf=surf, groups=self.background_sprite_group)

    def draw_map(self, screen):
        self.object_sprite_group.draw(screen)
        self.background_sprite_group.draw(screen)
        self.enemy_sprite_group.draw(screen)
        self.item_sprite_group.draw(screen)
        self.character_sprite_group.draw(screen)
        self.item_sprite_group.update()
        self.enemy_sprite_group.update()
        self.character_sprite_group.update()

