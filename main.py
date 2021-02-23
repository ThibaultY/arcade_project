"""
Créé par Yohan Thibault
Ce programme va être un jeux utilisant la libririe Arcade.
"""

import arcade
import random


class MyCame(arcade.Window):
    def __init__(self, width, height, title):
        # call the parent class's init function
        super().__init__(width, height, title)

    def on_draw(self):
        """
        C'est la métode de Arcade invoque à chaque
        frame pour afficher les éléments devotre jeux à l'écran.
        :return:
        """
        arcade.start_render()
        for i in range(20):
            arcade.draw_circle_filled(random.randint(0, 640), random.randint(0, 480), 20, (255, 54, 34))

class

def main():
    window = MyCame(640, 480, "Drawing Example")
    arcade.run()


main()
