#################################################
#                   INPUT 22
# Programacao de Jogos 17
# Programe um Carteado
#
# Usage:
# > python I22Pj17_Cards_a.py
#
# 20230725
#
# https://en.wikipedia.org/wiki/Playing_card
# https://tekeye.uk/playing_cards/svg-playing-cards
# https://api.arcade.academy/en/latest/
#################################################
__author__ = 'Rodrigo Nobrega'
__title__ = "Cards"
__version__ = 3.032


# import
import random
import arcade
import pandas as pd


# Global variables
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 576
PATTERN_LIST = ["blue", "red", "amber", "green"]


class Deck(object):
    """
    Class for representing and manipulating a deck of cards.

    Attributes:
    - patterns: A list of patterns the deck will contain. It defaults to 1 pattern.
    - numbers: The possible numbers that each card in the deck can have.
    - suits: The possible suits that each card in the deck can have.
    - colours: The possible colours that each card in the deck can have.
    - deck: The list of cards that are currently in the deck.
    """

    def __init__(self, patterns: int = 1):
        """
        Initializer for the Deck class. Sets up the initial state of the deck.
        """
        self.patterns = PATTERN_LIST[:patterns]
        self.numbers = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "JOKER"]
        self.suits = ["clubs", "hearts", "spades", "diamonds"]
        self.colours = ["black", "red"]
        self.deck = self.config()  # Create the initial deck configuration

    def config(self):
        """
        Creates the initial deck configuration.
        """
        deck = []
        sequence = 0
        for pattern in self.patterns:
            for suit in self.suits:
                for card in self.numbers[:-1]:
                    # Append card details to deck
                    deck.append({"card": card, "suit": suit, "value": self.numbers.index(card) + 1,
                                 "colour": self.colours[0] if suit in ["clubs", "spades"] else self.colours[1],
                                 "pattern": pattern, "sequence": sequence})
                    sequence += 1
            for colour in self.colours:
                # Append Joker card details to deck
                deck.append({"card": self.numbers[-1], "suit": "", "value": 0,
                             "colour": colour, "pattern": pattern, "sequence": sequence})
                sequence += 1
        return deck

    def count_cards(self):
        """
        Returns the current count of cards in the deck.
        """
        return f"\nDeck of {len(self.deck)} Cards"

    def get_dataframe(self):
        """
        Returns the current deck of cards as a pandas DataFrame.
        """
        return pd.DataFrame(self.deck)

    def shuffle(self):
        """
        Shuffles the current deck of cards.
        """
        random.shuffle(self.deck)

    def cut(self, percent_from_top: int = 0):
        """
        Cuts the deck at the given percentage from the top.
        """
        if percent_from_top < 0:
            percent_from_top = 0
        elif percent_from_top > 100:
            percent_from_top = 100
        cut_index = int(len(self.deck) * percent_from_top / 100)
        self.deck = self.deck[cut_index:] + self.deck[:cut_index]

    def sort(self):
        """
        Sorts the deck based on the 'sequence' key in each card dictionary.
        """
        self.deck.sort(key=lambda x: x['sequence'])


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
    deck = Deck(2)
    #
    print(deck.count_cards())
    print(deck.get_dataframe())
    deck.shuffle()
    deck.shuffle()
    deck.cut(20)
    my_deck = deck.get_dataframe()
    #
    # footer --------------------------------------------------------------
    print(f'\n{34 * "="}  OK  {35 * "="}\n')
    return my_deck


# execute main
if __name__ == "__main__":
    # main()
    d = cards()