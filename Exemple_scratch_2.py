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
        for _ in range(10):
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
        index = 0
        for cercle in self.liste_cercles:
            distance_x = x - cercle.centre_x
            distance_y = y - cercle.centre_y
            distance_centre = int(math.sqrt((distance_x ** 2) + (distance_y ** 2)))

            if cercle.rayon > distance_centre:
                if arcade.MOUSE_BUTTON_LEFT == button:
                    self.liste_cercles.pop(index)
                else:
                    cercle.color = random.choice(COLOR_LIST)
            index += 1


def main():
    my_game = MyGame()
    my_game.setup()
    arcade.run()


main()
