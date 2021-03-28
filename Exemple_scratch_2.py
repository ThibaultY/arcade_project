import arcade
import random
from dataclasses import dataclass
import math

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
        arcade.set_background_color(arcade.color.GRAY_ASPARAGUS)
        for _ in range(20):
            rayon = random.randint(10, 50)
            pos_x = random.randint(0 + rayon, SCREEN_WIDTH - rayon)
            pos_y = random.randint(0 + rayon, SCREEN_HEIGHT - rayon)
            color = random.choice(COLOR_LIST)
            self.liste_cercles.append(Cercle(rayon, pos_x, pos_y, color))

    def on_draw(self):
        arcade.start_render()
        for cercle in self.liste_cercles:
            cercle.draw()

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        for cercle in self.liste_cercles:
            distance_centre = ((x - cercle.centre_x) ** 2) + ((y - cercle.centre_y) ** 2)

            if cercle.rayon ** 2 > distance_centre:
                if arcade.MOUSE_BUTTON_LEFT == button:
                    self.liste_cercles.pop(self.liste_cercles.index(cercle))
                else:
                    cercle.color = random.choice(COLOR_LIST)


def main():
    my_game = MyGame()
    my_game.setup()
    arcade.run()


if __name__ == '__main__':
    main()
