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
    # arcade.color.BLACK,
    arcade.color.WHITE
]


@dataclass
class Cercle:
    centre_x: int
    centre_y: int
    rayon: int
    couleur: (int, int, int)
    change_x = 150
    change_y = 150

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
        self.centre_x += self.change_x * delta_time
        self.centre_y += self.change_y * delta_time

        # checking and correcting colitions with the wall
        if self.centre_x + self.rayon >= SCREEN_WIDTH:
            self.change_x *= -1
            self.centre_x = SCREEN_WIDTH - self.rayon - 10
        elif self.centre_x - self.rayon <= 0:
            self.change_x *= -1
            self.centre_x = 0 + self.rayon + 10
        if self.centre_y + self.rayon >= SCREEN_HEIGHT:
            self.change_y *= -1
            self.centre_y = SCREEN_HEIGHT - self.rayon - 10
        elif self.centre_y - self.rayon <= 0:
            self.change_y *= -1
            self.centre_y = 0 + self.rayon + 10


class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, 'DvD', update_rate=1/60)
        self.liste_cercles = []

    def setup(self):
        """
        Setup window and it's objects.
        :return:
        """
        while len(self.liste_cercles) <= 20:
            rayon = random.randint(10, 50)
            pos_x = random.randint(0 + rayon, SCREEN_WIDTH - rayon)
            pos_y = random.randint(0 + rayon, SCREEN_HEIGHT - rayon)
            color = random.choice(COLOR_LIST)
            # est dans les deux cercle
            is_over_lapping = False
            for cercle in self.liste_cercles:
                distance_centre = ((pos_x - cercle.centre_x) ** 2) + ((pos_y - cercle.centre_y) ** 2)
                min_distance = (rayon + cercle.rayon) ** 2
                if distance_centre < min_distance:  # La distance est bonne pour ne pas over lap :
                    is_over_lapping = True

            if not is_over_lapping:
                self.liste_cercles.append(Cercle(pos_x, pos_y, rayon, color))
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        arcade.start_render()
        for cercle in self.liste_cercles:
            cercle.draw()

    def on_update(self, delta_time: float):
        for cercle in self.liste_cercles:
            cercle.update(delta_time)

            is_over_lapping = False
            for autre_cercle in self.liste_cercles:
                if self.liste_cercles.index(cercle) != self.liste_cercles.index(autre_cercle):
                    distance_centre = ((cercle.centre_x - autre_cercle.centre_x) ** 2) + ((cercle.centre_y - autre_cercle.centre_y) ** 2)
                    min_distance = (cercle.rayon + autre_cercle.rayon) ** 2
                    if distance_centre < min_distance:  # Si ils overlap
                        overlap_x = autre_cercle.centre_x - cercle.centre_x
                        overlap_y = autre_cercle.centre_y - cercle.centre_y
                        # déterminer quel partie overlap par rapport au cercle principale
                        if overlap_x > 0 and overlap_y > 0:  # en haut a droite (quadrant 1)
                            if cercle.change_x > 0:
                                cercle.change_x *= -1
                            if cercle.change_y > 0:
                                cercle.change_y *= -1
                        elif overlap_x < 0 and overlap_y > 0:  # en haut a gauche (quadrant 2)
                            if cercle.change_x < 0:
                                cercle.change_x *= -1
                            if cercle.change_y > 0:
                                cercle.change_y *= -1
                        elif overlap_x < 0 and overlap_y < 0:  # en bas a gauche (quadrant 3)
                            if cercle.change_x < 0:
                                cercle.change_x *= -1
                            if cercle.change_y < 0:
                                cercle.change_y *= -1
                        elif overlap_x > 0 and overlap_y < 0:  # en bas à droite (quadrant 4)
                            if cercle.change_x > 0:
                                cercle.change_x *= -1
                            if cercle.change_y < 0:
                                cercle.change_y *= -1
                        cercle.centre_x += cercle.change_x * delta_time
                        cercle.centre_y += cercle.change_y * delta_time


def main():
    my_game = MyGame()
    my_game.setup()
    arcade.run()


if __name__ == '__main__':
    main()
