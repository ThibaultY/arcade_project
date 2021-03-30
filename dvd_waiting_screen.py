"""
Créé par Yohan Thibault
Ce programme va faire la même chose que l'écran de veille d'une vieille
télévision.
"""
import arcade
from dataclasses import dataclass

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
COLOR_LIST = [
    arcade.color.BLUE,
    arcade.color.GREEN,
    arcade.color.YELLOW,
    arcade.color.ORANGE,
    arcade.color.RED,
    arcade.color.PURPLE,
    arcade.color.BLACK,
    arcade.color.WHITE
]


@dataclass
class Cercle:
    centre_x: int
    centre_y: int
    rayon: int
    couleur: (int, int, int)
    x_update = 3
    y_update = 3

    def draw(self):
        arcade.draw_circle_filled(self.centre_x, self.centre_y, self.rayon, self.couleur)

    def update(self):

        if



