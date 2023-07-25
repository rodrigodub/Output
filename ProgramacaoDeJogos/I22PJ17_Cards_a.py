#################################################
#                   INPUT 22
# Programacao de Jogos 17
# Programe um Carteado
#
# Usage:
# > python I22Pj17_Cards_a.py
#
# v.3.031
# 20230724
#
# https://en.wikipedia.org/wiki/Playing_card
# https://tekeye.uk/playing_cards/svg-playing-cards
# https://api.arcade.academy/en/latest/
#################################################
__author__ = 'Rodrigo Nobrega'
__title__ = "Cards"
__version__ = 3.031


# import
import arcade


# Global variables
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 576


class Deck(object):
    def __init__(self, pattern):
        self.pattern = pattern
        self.numbers = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "JOKER"]
        self.suits = ["clubs", "hearts", "spades", "diamonds"]
        self.colours = ["black", "red"]
        self.deck = self.config()

    def config(self):
        deck = []
        for suit in self.suits:
            for card in self.numbers[:-1]:
                deck.append({"card": card, "suit": suit, "value": self.numbers.index(card) + 1,
                             "colour": self.colours[0] if suit in ["clubs", "spades"] else self.colours[1],
                             "pattern": self.pattern})
        for colour in self.colours:
            deck.append({"card": self.numbers[-1], "suit": "", "value": 0,
                         "colour": colour, "pattern": self.pattern})
        return deck


class MyGame(arcade.Window):
    """
    Main application class.

    NOTE: Go ahead and delete the methods you don't need.
    If you do need a method, delete the 'pass' and replace it
    with your own code. Don't leave 'pass' in this program.
    """

    def __init__(self, width, height):
        super().__init__(width, height, title="Treasure Hunt")

        arcade.set_background_color(arcade.color.AMAZON)

        # If you have sprite lists, you should create them here,
        # and set them to None

    def setup(self):
        # Create your sprites and sprite lists here
        pass

    def on_draw(self):
        """
        Render the screen.
        """

        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        arcade.start_render()

        # Call draw() on all your sprite lists below

    def update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        pass

    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.

        For a full list of keys, see:
        http://arcade.academy/arcade.key.html
        """
        pass

    def on_key_release(self, key, key_modifiers):
        """
        Called whenever the user lets off a previously pressed key.
        """
        pass

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        """
        Called whenever the mouse moves.
        """
        pass

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        pass

    def on_mouse_release(self, x, y, button, key_modifiers):
        """
        Called when a user releases a mouse button.
        """
        pass


# main routine
def main():
    """ Main method """
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.setup()
    arcade.run()


def cards():
    # header --------------------------------------------------------------
    print(f'\n{75 * "="}')
    print(f'{f"{__title__} v.{__version__}":^75}')
    print(f'{75 * "="}\n')
    # ---------------------------------------------------------------------
    deck = Deck("blue hatch")
    #
    for card in deck.deck:
        print(f"{card['card']:<8}{card['suit']:^10}{card['value']:>5}{card['colour']:^10}{card['pattern']:^12}")
    print(len(deck.deck))
    #
    # footer --------------------------------------------------------------
    print(f'\n{34 * "="}  OK  {35 * "="}\n')


# execute main
if __name__ == "__main__":
    # main()
    cards()