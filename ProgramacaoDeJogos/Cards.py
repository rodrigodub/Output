#################################################
#                   INPUT 22
# Programacao de Jogos 17
# Programe um Carteado
#
# Usage:
# > python Cards.py
#
# 20230730
#
# https://en.wikipedia.org/wiki/Playing_card
# https://tekeye.uk/playing_cards/svg-playing-cards
# https://api.arcade.academy/en/latest/
#################################################
__author__ = 'Rodrigo Nobrega'
__title__ = "Cards"
__version__ = 3.035


# import
import random
from pathlib import Path
import arcade
import pandas as pd


# Constants
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 576
PATTERN_LIST = ["blue", "red", "amber", "green"]
SPRITE_SCALING_CARDS = 0.5
# SPRITES_DIR = Path("images/cards/png")
SPRITES_DIR = "images/cards/png"


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
        self.reserve = []

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
                                 "pattern": pattern, "sequence": sequence,
                                 "cardfile": f"{suit}_{card.replace('A', 'ace').replace('J', 'jack').replace('Q', 'queen').replace('K', 'king')}"})
                    sequence += 1
            for colour in self.colours:
                # Append Joker card details to deck
                deck.append({"card": self.numbers[-1], "suit": "", "value": 0,
                             "colour": colour, "pattern": pattern, "sequence": sequence,
                             "cardfile": f"{ self.numbers[-1].lower()}_{colour}"})
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

    def remove(self, card_number: str = None):
        if card_number:
            [self.reserve.append(i) for i in self.deck if i["card"] == card_number]
            [self.deck.remove(i) for i in self.deck if i["card"] == card_number]
        return

class MyGame(arcade.Window):
    """
    Main application class.

    NOTE: Go ahead and delete the methods you don't need.
    If you do need a method, delete the 'pass' and replace it
    with your own code. Don't leave 'pass' in this program.
    """

    def __init__(self, width, height, deck):
        super().__init__(width, height, title="Cards")

        arcade.set_background_color(arcade.color.AMAZON)

        # If you have sprite lists, you should create them here,
        # and set them to None
        self.cards_list = None
        self.player_hand_list = None

        # Individual cards as a dictionary of sprites
        self.cards_sprite_dictionary = None

        # My deck of cards
        self.deck = deck

    def setup(self):
        # Create your sprites and sprite lists here
        self.cards_list = arcade.SpriteList()
        self.player_hand_list = arcade.SpriteList()

        # Add cards sprites dictionary
        self.cards_sprite_dictionary = {
            "clubs_ace": arcade.Sprite(SPRITES_DIR + r"/clubs_ace.png", SPRITE_SCALING_CARDS),
            "clubs_2": arcade.Sprite(SPRITES_DIR + r"/clubs_2.png", SPRITE_SCALING_CARDS),
            "clubs_3": arcade.Sprite(SPRITES_DIR + r"/clubs_3.png", SPRITE_SCALING_CARDS),
            "clubs_4": arcade.Sprite(SPRITES_DIR + r"/clubs_4.png", SPRITE_SCALING_CARDS),
            "clubs_5": arcade.Sprite(SPRITES_DIR + r"/clubs_5.png", SPRITE_SCALING_CARDS),
            "clubs_6": arcade.Sprite(SPRITES_DIR + r"/clubs_6.png", SPRITE_SCALING_CARDS),
            "clubs_7": arcade.Sprite(SPRITES_DIR + r"/clubs_7.png", SPRITE_SCALING_CARDS),
            "clubs_8": arcade.Sprite(SPRITES_DIR + r"/clubs_8.png", SPRITE_SCALING_CARDS),
            "clubs_9": arcade.Sprite(SPRITES_DIR + r"/clubs_9.png", SPRITE_SCALING_CARDS),
            "clubs_10": arcade.Sprite(SPRITES_DIR + r"/clubs_10.png", SPRITE_SCALING_CARDS),
            "clubs_jack": arcade.Sprite(SPRITES_DIR + r"/clubs_jack.png", SPRITE_SCALING_CARDS),
            "clubs_queen": arcade.Sprite(SPRITES_DIR + r"/clubs_queen.png", SPRITE_SCALING_CARDS),
            "clubs_king": arcade.Sprite(SPRITES_DIR + r"/clubs_king.png", SPRITE_SCALING_CARDS),
            "hearts_ace": arcade.Sprite(SPRITES_DIR + r"/hearts_ace.png", SPRITE_SCALING_CARDS),
            "hearts_2": arcade.Sprite(SPRITES_DIR + r"/hearts_2.png", SPRITE_SCALING_CARDS),
            "hearts_3": arcade.Sprite(SPRITES_DIR + r"/hearts_3.png", SPRITE_SCALING_CARDS),
            "hearts_4": arcade.Sprite(SPRITES_DIR + r"/hearts_4.png", SPRITE_SCALING_CARDS),
            "hearts_5": arcade.Sprite(SPRITES_DIR + r"/hearts_5.png", SPRITE_SCALING_CARDS),
            "hearts_6": arcade.Sprite(SPRITES_DIR + r"/hearts_6.png", SPRITE_SCALING_CARDS),
            "hearts_7": arcade.Sprite(SPRITES_DIR + r"/hearts_7.png", SPRITE_SCALING_CARDS),
            "hearts_8": arcade.Sprite(SPRITES_DIR + r"/hearts_8.png", SPRITE_SCALING_CARDS),
            "hearts_9": arcade.Sprite(SPRITES_DIR + r"/hearts_9.png", SPRITE_SCALING_CARDS),
            "hearts_10": arcade.Sprite(SPRITES_DIR + r"/hearts_10.png", SPRITE_SCALING_CARDS),
            "hearts_jack": arcade.Sprite(SPRITES_DIR + r"/hearts_jack.png", SPRITE_SCALING_CARDS),
            "hearts_queen": arcade.Sprite(SPRITES_DIR + r"/hearts_queen.png", SPRITE_SCALING_CARDS),
            "hearts_king": arcade.Sprite(SPRITES_DIR + r"/hearts_king.png", SPRITE_SCALING_CARDS),
            "spades_ace": arcade.Sprite(SPRITES_DIR + r"/spades_ace.png", SPRITE_SCALING_CARDS),
            "spades_2": arcade.Sprite(SPRITES_DIR + r"/spades_2.png", SPRITE_SCALING_CARDS),
            "spades_3": arcade.Sprite(SPRITES_DIR + r"/spades_3.png", SPRITE_SCALING_CARDS),
            "spades_4": arcade.Sprite(SPRITES_DIR + r"/spades_4.png", SPRITE_SCALING_CARDS),
            "spades_5": arcade.Sprite(SPRITES_DIR + r"/spades_5.png", SPRITE_SCALING_CARDS),
            "spades_6": arcade.Sprite(SPRITES_DIR + r"/spades_6.png", SPRITE_SCALING_CARDS),
            "spades_7": arcade.Sprite(SPRITES_DIR + r"/spades_7.png", SPRITE_SCALING_CARDS),
            "spades_8": arcade.Sprite(SPRITES_DIR + r"/spades_8.png", SPRITE_SCALING_CARDS),
            "spades_9": arcade.Sprite(SPRITES_DIR + r"/spades_9.png", SPRITE_SCALING_CARDS),
            "spades_10": arcade.Sprite(SPRITES_DIR + r"/spades_10.png", SPRITE_SCALING_CARDS),
            "spades_jack": arcade.Sprite(SPRITES_DIR + r"/spades_jack.png", SPRITE_SCALING_CARDS),
            "spades_queen": arcade.Sprite(SPRITES_DIR + r"/spades_queen.png", SPRITE_SCALING_CARDS),
            "spades_king": arcade.Sprite(SPRITES_DIR + r"/spades_king.png", SPRITE_SCALING_CARDS),
            "diamonds_ace": arcade.Sprite(SPRITES_DIR + r"/diamonds_ace.png", SPRITE_SCALING_CARDS),
            "diamonds_2": arcade.Sprite(SPRITES_DIR + r"/diamonds_2.png", SPRITE_SCALING_CARDS),
            "diamonds_3": arcade.Sprite(SPRITES_DIR + r"/diamonds_3.png", SPRITE_SCALING_CARDS),
            "diamonds_4": arcade.Sprite(SPRITES_DIR + r"/diamonds_4.png", SPRITE_SCALING_CARDS),
            "diamonds_5": arcade.Sprite(SPRITES_DIR + r"/diamonds_5.png", SPRITE_SCALING_CARDS),
            "diamonds_6": arcade.Sprite(SPRITES_DIR + r"/diamonds_6.png", SPRITE_SCALING_CARDS),
            "diamonds_7": arcade.Sprite(SPRITES_DIR + r"/diamonds_7.png", SPRITE_SCALING_CARDS),
            "diamonds_8": arcade.Sprite(SPRITES_DIR + r"/diamonds_8.png", SPRITE_SCALING_CARDS),
            "diamonds_9": arcade.Sprite(SPRITES_DIR + r"/diamonds_9.png", SPRITE_SCALING_CARDS),
            "diamonds_10": arcade.Sprite(SPRITES_DIR + r"/diamonds_10.png", SPRITE_SCALING_CARDS),
            "diamonds_jack": arcade.Sprite(SPRITES_DIR + r"/diamonds_jack.png", SPRITE_SCALING_CARDS),
            "diamonds_queen": arcade.Sprite(SPRITES_DIR + r"/diamonds_queen.png", SPRITE_SCALING_CARDS),
            "diamonds_king": arcade.Sprite(SPRITES_DIR + r"/diamonds_king.png", SPRITE_SCALING_CARDS),
            "joker_black": arcade.Sprite(SPRITES_DIR + r"/joker_black.png", SPRITE_SCALING_CARDS),
            "joker_red": arcade.Sprite(SPRITES_DIR + r"/joker_red.png", SPRITE_SCALING_CARDS),
            "blue": arcade.Sprite(SPRITES_DIR + r"/blue.png", SPRITE_SCALING_CARDS),
            "red": arcade.Sprite(SPRITES_DIR + r"/red.png", SPRITE_SCALING_CARDS),
        }

        # Set player hand
        self.player_hand_list.append(self.cards_sprite_dictionary["clubs_4"])
        self.player_hand_list.append(self.cards_sprite_dictionary["hearts_7"])
        # Cards position on screen
        self.player_hand_list[0].center_x = 250
        self.player_hand_list[0].center_y = 250
        self.player_hand_list[1].center_x = 500
        self.player_hand_list[1].center_y = 250

    def on_draw(self):
        """
        Render the screen.
        """
        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        arcade.start_render()

        # Call draw() on all your sprite lists below
        self.player_hand_list.draw()

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
    # Create my deck of cards
    deck = Deck()
    # Create arcade
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, deck)
    game.setup()
    #
    # print(game.player_hand_list)
    #
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
    # deck.shuffle()
    # deck.shuffle()
    # deck.cut(20)
    # my_deck = deck.get_dataframe()
    # deck.remove("JOKER")
    #
    # footer --------------------------------------------------------------
    print(f'\n{34 * "="}  OK  {35 * "="}\n')
    return deck


# execute main
if __name__ == "__main__":
    main()
    # d = cards()