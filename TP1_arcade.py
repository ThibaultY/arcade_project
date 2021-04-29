"""
Créé par yohan Thibault
Ce programme
"""
import arcade
import random
from dataclasses import dataclass

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Modèle de départ"

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
class Balle:
    centre_x: int
    centre_y: int
    rayon: int
    couleur: (int, int, int)
    change_x: int = 3
    change_y: int = 3

    @staticmethod
    def create(x, y):
        """
        This methode will create a circle at a precise spot.
        This circle will have a random size and color.
        :param x: center on the x axis
        :param y: center on the y axis
        :return: a Ball() type object
        """
        rayon = random.randint(10, 30)
        color = random.choice(COLOR_LIST)
        return Balle(x, y, rayon, color)

    def draw(self):
        """
        Draws the circle.
        """
        arcade.draw_circle_filled(self.centre_x, self.centre_y, self.rayon, self.couleur)

    def update(self):
        """
        Changes the position of the circle and make sure
        that they don't collide with the borders before they are drawn.
        """
        # changing position of the circle
        self.centre_x += self.change_x
        self.centre_y += self.change_y

        # Check if the circle is in collision with the border
        # On the right or left border
        if self.centre_x + self.rayon >= SCREEN_WIDTH:
            self.change_x *= -1
            self.centre_x = SCREEN_WIDTH - self.rayon
        elif self.centre_x - self.rayon <= 0:
            self.change_x *= -1
            self.centre_x = 0 + self.rayon

        # On the top or bottom border
        if self.centre_y + self.rayon >= SCREEN_HEIGHT:
            self.change_y *= -1
            self.centre_y = SCREEN_HEIGHT - self.rayon
        elif self.centre_y - self.rayon <= 0:
            self.change_y *= -1
            self.centre_y = 0 + self.rayon


@dataclass
class Rectangle:
    centre_x: int
    centre_y: int
    width: int
    height: int
    couleur: (int, int, int)
    angle: float = 0
    change_x: int = 3
    change_y: int = 3

    @staticmethod
    def create(x, y):
        """
        This methode will create a rectangle at a precise spot.
        :param x: center on the x axis
        :param y: center on the y axis
        :return: a Rectangle() type object
        """
        width = random.randint(5, 100)
        height = random.randint(5, 100)
        couleur = random.choice(COLOR_LIST)
        angle = random.randint(0, 360)

        return Rectangle(x, y, width, height, couleur, angle)

    def draw(self):
        """
        Draws the rectangle.
        """
        arcade.draw_rectangle_filled(self.centre_x, self.centre_y, self.width, self.height, self.couleur, self.angle)

    def update(self):
        """
        Changes the position of the rectangle and make sure
        that they don't collide with the borders before they are drawn.
        """
        # changing position of the rectangle
        self.centre_x += self.change_x
        self.centre_y += self.change_y

        # Check if the rectangle is in collision with the border
        # on the right or left border
        if self.centre_x + self.width/2 >= SCREEN_WIDTH:
            self.change_x *= -1
            self.centre_x = SCREEN_WIDTH - int(self.width/2)
        elif self.centre_x - self.width/2 <= 0:
            self.change_x *= -1
            self.centre_x = 0 + int(self.width/2)

        # On the top or bottom border
        if self.centre_y + self.height/2 >= SCREEN_HEIGHT:
            self.change_y *= -1
            self.centre_y = SCREEN_HEIGHT - int(self.height/2)
        elif self.centre_y - self.height/2 <= 0:
            self.change_y *= -1
            self.centre_y = 0 + int(self.height/2)


class MyGame(arcade.Window):
    """
    La classe principale de l'application

    NOTE: Vous pouvez effacer les méthodes que vous n'avez pas besoin.
    Si vous en avez besoin, remplacer le mot clé "pass" par votre propre code.
    """

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.AMAZON)

        # sprites lists :
        self.liste_balles = []
        self.liste_rectangles = []

    def setup(self):
        """
        Configurer les variables de votre jeu ici. Il faut appeler la méthode une nouvelle
        fois si vous recommencer une nouvelle partie.
        """
        # C'est ici que vous allez créer vos listes de sprites et vos sprites.
        # C'est aussi ici que vous charger les sons de votre jeu.

        # default balls and rectangles
        for _ in range(1):
            self.liste_balles.append(Balle.create(200, 200))
            self.liste_rectangles.append(Rectangle.create(100, 100))

    def on_draw(self):
        """
        C'est la méthode que Arcade invoque à chaque "frame" pour afficher les éléments
        de votre jeu à l'écran.
        """

        # Cette commande permet d'effacer l'écran avant de dessiner. Elle va dessiner l'arrière
        # plan selon la couleur spécifié avec la méthode "set_background_color".
        arcade.start_render()

        # Draw the circles
        for balle in self.liste_balles:
            balle.draw()

        # Draw the rectangles
        for rectangle in self.liste_rectangles:
            rectangle.draw()

    def on_update(self, delta_time):
        """
        Toute la logique pour déplacer les objets de votre jeu et de
        simuler sa logique vont ici. Normalement, c'est ici que
        vous allez invoquer la méthode "update()" sur vos listes de sprites.
        Paramètre:
            - delta_time : le nombre de milliseconde depuis le dernier update.
        """
        # Updates the circles
        for balle in self.liste_balles:
            balle.update()

        # Updates the rectangles
        for rectangle in self.liste_rectangles:
            rectangle.update()

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Méthode invoquée lorsque l'usager clique un bouton de la souris.
        Paramètres:
            - x, y: coordonnées où le bouton a été cliqué
            - button: le bouton de la souris appuyé
            - key_modifiers: est-ce que l'usager appuie sur "shift" ou "ctrl" ?
        """
        # Adds a circle when the left button is clicked
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.liste_balles.append(Balle.create(x, y))

        # Adds a rectangle when the left right is clicked
        if button == arcade.MOUSE_BUTTON_RIGHT:
            self.liste_balles.append(Rectangle.create(x, y))


def main():
    """ Main method """
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
