"""
Créé par Yohan Thibault
Ce programme va être un jeux utilisant la libririe Arcade.
"""

import arcade
import random

color_select = [
    arcade.color.BLUE,
    arcade.color.GREEN,
    arcade.color.YELLOW,
    arcade.color.ORANGE,
    arcade.color.RED,
    arcade.color.PURPLE,
    arcade.color.WHITE,
    arcade.color.BLACK,
    arcade.color.GRAY
]
rayon = 20


class MyCame(arcade.Window):
    def __init__(self, width, height, title):
        # call the parent class's init function
        super().__init__(width, height, title)

    def setup(self):
        self.background_color = arcade.color.WHITE
        arcade.start_render()
        for i in range(20):
            arcade.draw_circle_filled(
                random.randint(0 + rayon, 640 - rayon),
                random.randint(0 + rayon, 480 - rayon),
                rayon,
                random.choice(color_select)
            )
        arcade.finish_render()

    def on_draw(self):
        """
        C'est la métode de Arcade invoque à chaque
        frame pour afficher les éléments devotre jeux à l'écran.
        :return:
        """
        arcade.start_render()
        arcade.finish_render()

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        arcade.start_render()
        print("click")
        for i in range(20):
            arcade.draw_circle_filled(
                random.randint(0 + rayon, 640 - rayon),
                random.randint(0 + rayon, 480 - rayon),
                rayon,
                random.choice(color_select)
            )
        arcade.finish_render()

#    def on_mouse_release(self, x: float, y: float, button: int,
#                         modifiers: int):
#        arcade.start_render()
#        self.clear()
#        arcade.finish_render()


def main():
    game = MyCame(640, 480, "Drawing Example")
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
