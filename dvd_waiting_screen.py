"""
Créé par Yohan Thibault
Ce programme va faire la même chose que l'écran de veille d'une vieille
télévision.
"""
import arcade
import random
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
    x_mouvement = 300
    y_mouvement = 300

    def draw(self):
        """
        Draws the circle.
        """
        arcade.draw_circle_filled(self.centre_x, self.centre_y, self.rayon, self.couleur)

    def update(self, delta_time):
        """
        changes the values of the circle before they are drawn.
        :param delta_time: delta_time from, arcade.Window.on_update()
        """
        # changing position of the circle
        self.centre_x += self.x_mouvement * delta_time
        self.centre_y += self.y_mouvement * delta_time

        # checking and correcting colitions with the wall
        if self.centre_x + self.rayon >= SCREEN_WIDTH or self.centre_x - self.rayon <= 0:
            self.x_mouvement *= -1  # changes the direction
            self.centre_x += self.x_mouvement * delta_time  # keeps the circle form entering the wall before next update
        if self.centre_y + self.rayon >= SCREEN_HEIGHT or self.centre_y - self.rayon <= 0:
            self.y_mouvement *= -1
            self.centre_y += self.y_mouvement * delta_time


class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, 'DvD', update_rate=1/120)
        self.liste_cercle = []

    def setup(self):
        """
        Setup window and it's objects.
        :return:
        """
        self.liste_cercle.append(Cercle(random.randint(0 + 50, SCREEN_WIDTH - 50),
                                        random.randint(0+50, SCREEN_HEIGHT - 50),
                                        50,
                                        arcade.color.BRIGHT_GREEN))
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        arcade.start_render()
        for cercle in self.liste_cercle:
            cercle.draw()

    def on_update(self, delta_time: float):
        for cercle in self.liste_cercle:
            cercle.update(delta_time)


def main():
    my_game = MyGame()
    my_game.setup()
    arcade.run()


if __name__ == '__main__':
    main()
