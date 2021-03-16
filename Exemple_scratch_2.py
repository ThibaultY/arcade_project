import arcade
import random
import time
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
    rayon: int
    centre_x: int
    centre_y: int
    color: (int, int, int)

    def draw(self):
        arcade.draw_circle_filled(self.centre_x, self.centre_y, self.rayon, self.color)


class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Exercice arcade #1")
        self.liste_cercles = []

    def setup(self):
        for i in range(20):
            rayon = random.randint(10, 50)
            self.liste_cercles.append(Cercle(random.randint(10, 50),
                                             random.randint(0 + rayon, SCREEN_WIDTH - rayon),
                                             random.randint(0 + rayon, SCREEN_HEIGHT - rayon),
                                             random.choice(COLOR_LIST))
                                      )

    def on_draw(self):
        arcade.start_render()
        for i in range(len(self.liste_cercles)):
            self.liste_cercles[i].draw()


def main():
    my_game = MyGame()
    my_game.setup()
    arcade.run()


main()
