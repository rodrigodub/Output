#################################################
#                   INPUT 22
# Programacao de Jogos 17
# Programe um Carteado
#
# Usage:
# > python I22Pj17_Cards_a.py
# Follow up development on Cards.py, versions 3.034+
# 20230730
#
# https://en.wikipedia.org/wiki/Playing_card
# https://tekeye.uk/playing_cards/svg-playing-cards
# https://api.arcade.academy/en/latest/
#################################################
__author__ = 'Rodrigo Nobrega'
__title__ = "Cards"
__version__ = 3.034


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

        # Individual sprites
        self.clubs_ace_sprite = None
        self.clubs_2_sprite = None
        self.clubs_3_sprite = None
        self.clubs_4_sprite = None
        self.clubs_5_sprite = None
        self.clubs_6_sprite = None
        self.clubs_7_sprite = None
        self.clubs_8_sprite = None
        self.clubs_9_sprite = None
        self.clubs_10_sprite = None
        self.clubs_jack_sprite = None
        self.clubs_queen_sprite = None
        self.clubs_king_sprite = None
        self.hearts_ace_sprite = None
        self.hearts_2_sprite = None
        self.hearts_3_sprite = None
        self.hearts_4_sprite = None
        self.hearts_5_sprite = None
        self.hearts_6_sprite = None
        self.hearts_7_sprite = None
        self.hearts_8_sprite = None
        self.hearts_9_sprite = None
        self.hearts_10_sprite = None
        self.hearts_jack_sprite = None
        self.hearts_queen_sprite = None
        self.hearts_king_sprite = None
        self.spades_ace_sprite = None
        self.spades_2_sprite = None
        self.spades_3_sprite = None
        self.spades_4_sprite = None
        self.spades_5_sprite = None
        self.spades_6_sprite = None
        self.spades_7_sprite = None
        self.spades_8_sprite = None
        self.spades_9_sprite = None
        self.spades_10_sprite = None
        self.spades_jack_sprite = None
        self.spades_queen_sprite = None
        self.spades_king_sprite = None
        self.diamonds_ace_sprite = None
        self.diamonds_2_sprite = None
        self.diamonds_3_sprite = None
        self.diamonds_4_sprite = None
        self.diamonds_5_sprite = None
        self.diamonds_6_sprite = None
        self.diamonds_7_sprite = None
        self.diamonds_8_sprite = None
        self.diamonds_9_sprite = None
        self.diamonds_10_sprite = None
        self.diamonds_jack_sprite = None
        self.diamonds_queen_sprite = None
        self.diamonds_king_sprite = None
        self.joker_black_sprite = None
        self.joker_red_sprite = None
        self.clubs_ace_sprite = None
        self.clubs_2_sprite = None
        self.clubs_3_sprite = None
        self.clubs_4_sprite = None
        self.clubs_5_sprite = None
        self.clubs_6_sprite = None
        self.clubs_7_sprite = None
        self.clubs_8_sprite = None
        self.clubs_9_sprite = None
        self.clubs_10_sprite = None
        self.clubs_jack_sprite = None
        self.clubs_queen_sprite = None
        self.clubs_king_sprite = None
        self.hearts_ace_sprite = None
        self.hearts_2_sprite = None
        self.hearts_3_sprite = None
        self.hearts_4_sprite = None
        self.hearts_5_sprite = None
        self.hearts_6_sprite = None
        self.hearts_7_sprite = None
        self.hearts_8_sprite = None
        self.hearts_9_sprite = None
        self.hearts_10_sprite = None
        self.hearts_jack_sprite = None
        self.hearts_queen_sprite = None
        self.hearts_king_sprite = None
        self.spades_ace_sprite = None
        self.spades_2_sprite = None
        self.spades_3_sprite = None
        self.spades_4_sprite = None
        self.spades_5_sprite = None
        self.spades_6_sprite = None
        self.spades_7_sprite = None
        self.spades_8_sprite = None
        self.spades_9_sprite = None
        self.spades_10_sprite = None
        self.spades_jack_sprite = None
        self.spades_queen_sprite = None
        self.spades_king_sprite = None
        self.diamonds_ace_sprite = None
        self.diamonds_2_sprite = None
        self.diamonds_3_sprite = None
        self.diamonds_4_sprite = None
        self.diamonds_5_sprite = None
        self.diamonds_6_sprite = None
        self.diamonds_7_sprite = None
        self.diamonds_8_sprite = None
        self.diamonds_9_sprite = None
        self.diamonds_10_sprite = None
        self.diamonds_jack_sprite = None
        self.diamonds_queen_sprite = None
        self.diamonds_king_sprite = None
        self.joker_black_sprite = None
        self.joker_red_sprite = None
        self.blue_background_sprite = None
        self.red_background_sprite = None

        # My deck of cards
        self.deck = deck

    def setup(self):
        # Create your sprites and sprite lists here
        self.cards_list = arcade.SpriteList()
        self.player_hand_list = arcade.SpriteList()

        # Add cards sprites
        self.clubs_ace_sprite = arcade.Sprite(SPRITES_DIR + r"/clubs_ace.png", SPRITE_SCALING_CARDS)
        self.clubs_2_sprite = arcade.Sprite(SPRITES_DIR + r"/clubs_2.png", SPRITE_SCALING_CARDS)
        self.clubs_3_sprite = arcade.Sprite(SPRITES_DIR + r"/clubs_3.png", SPRITE_SCALING_CARDS)
        self.clubs_4_sprite = arcade.Sprite(SPRITES_DIR + r"/clubs_4.png", SPRITE_SCALING_CARDS)
        self.clubs_5_sprite = arcade.Sprite(SPRITES_DIR + r"/clubs_5.png", SPRITE_SCALING_CARDS)
        self.clubs_6_sprite = arcade.Sprite(SPRITES_DIR + r"/clubs_6.png", SPRITE_SCALING_CARDS)
        self.clubs_7_sprite = arcade.Sprite(SPRITES_DIR + r"/clubs_7.png", SPRITE_SCALING_CARDS)
        self.clubs_8_sprite = arcade.Sprite(SPRITES_DIR + r"/clubs_8.png", SPRITE_SCALING_CARDS)
        self.clubs_9_sprite = arcade.Sprite(SPRITES_DIR + r"/clubs_9.png", SPRITE_SCALING_CARDS)
        self.clubs_10_sprite = arcade.Sprite(SPRITES_DIR + r"/clubs_10.png", SPRITE_SCALING_CARDS)
        self.clubs_jack_sprite = arcade.Sprite(SPRITES_DIR + r"/clubs_jack.png", SPRITE_SCALING_CARDS)
        self.clubs_queen_sprite = arcade.Sprite(SPRITES_DIR + r"/clubs_queen.png", SPRITE_SCALING_CARDS)
        self.clubs_king_sprite = arcade.Sprite(SPRITES_DIR + r"/clubs_king.png", SPRITE_SCALING_CARDS)
        self.hearts_ace_sprite = arcade.Sprite(SPRITES_DIR + r"/hearts_ace.png", SPRITE_SCALING_CARDS)
        self.hearts_2_sprite = arcade.Sprite(SPRITES_DIR + r"/hearts_2.png", SPRITE_SCALING_CARDS)
        self.hearts_3_sprite = arcade.Sprite(SPRITES_DIR + r"/hearts_3.png", SPRITE_SCALING_CARDS)
        self.hearts_4_sprite = arcade.Sprite(SPRITES_DIR + r"/hearts_4.png", SPRITE_SCALING_CARDS)
        self.hearts_5_sprite = arcade.Sprite(SPRITES_DIR + r"/hearts_5.png", SPRITE_SCALING_CARDS)
        self.hearts_6_sprite = arcade.Sprite(SPRITES_DIR + r"/hearts_6.png", SPRITE_SCALING_CARDS)
        self.hearts_7_sprite = arcade.Sprite(SPRITES_DIR + r"/hearts_7.png", SPRITE_SCALING_CARDS)
        self.hearts_8_sprite = arcade.Sprite(SPRITES_DIR + r"/hearts_8.png", SPRITE_SCALING_CARDS)
        self.hearts_9_sprite = arcade.Sprite(SPRITES_DIR + r"/hearts_9.png", SPRITE_SCALING_CARDS)
        self.hearts_10_sprite = arcade.Sprite(SPRITES_DIR + r"/hearts_10.png", SPRITE_SCALING_CARDS)
        self.hearts_jack_sprite = arcade.Sprite(SPRITES_DIR + r"/hearts_jack.png", SPRITE_SCALING_CARDS)
        self.hearts_queen_sprite = arcade.Sprite(SPRITES_DIR + r"/hearts_queen.png", SPRITE_SCALING_CARDS)
        self.hearts_king_sprite = arcade.Sprite(SPRITES_DIR + r"/hearts_king.png", SPRITE_SCALING_CARDS)
        self.spades_ace_sprite = arcade.Sprite(SPRITES_DIR + r"/spades_ace.png", SPRITE_SCALING_CARDS)
        self.spades_2_sprite = arcade.Sprite(SPRITES_DIR + r"/spades_2.png", SPRITE_SCALING_CARDS)
        self.spades_3_sprite = arcade.Sprite(SPRITES_DIR + r"/spades_3.png", SPRITE_SCALING_CARDS)
        self.spades_4_sprite = arcade.Sprite(SPRITES_DIR + r"/spades_4.png", SPRITE_SCALING_CARDS)
        self.spades_5_sprite = arcade.Sprite(SPRITES_DIR + r"/spades_5.png", SPRITE_SCALING_CARDS)
        self.spades_6_sprite = arcade.Sprite(SPRITES_DIR + r"/spades_6.png", SPRITE_SCALING_CARDS)
        self.spades_7_sprite = arcade.Sprite(SPRITES_DIR + r"/spades_7.png", SPRITE_SCALING_CARDS)
        self.spades_8_sprite = arcade.Sprite(SPRITES_DIR + r"/spades_8.png", SPRITE_SCALING_CARDS)
        self.spades_9_sprite = arcade.Sprite(SPRITES_DIR + r"/spades_9.png", SPRITE_SCALING_CARDS)
        self.spades_10_sprite = arcade.Sprite(SPRITES_DIR + r"/spades_10.png", SPRITE_SCALING_CARDS)
        self.spades_jack_sprite = arcade.Sprite(SPRITES_DIR + r"/spades_jack.png", SPRITE_SCALING_CARDS)
        self.spades_queen_sprite = arcade.Sprite(SPRITES_DIR + r"/spades_queen.png", SPRITE_SCALING_CARDS)
        self.spades_king_sprite = arcade.Sprite(SPRITES_DIR + r"/spades_king.png", SPRITE_SCALING_CARDS)
        self.diamonds_ace_sprite = arcade.Sprite(SPRITES_DIR + r"/diamonds_ace.png", SPRITE_SCALING_CARDS)
        self.diamonds_2_sprite = arcade.Sprite(SPRITES_DIR + r"/diamonds_2.png", SPRITE_SCALING_CARDS)
        self.diamonds_3_sprite = arcade.Sprite(SPRITES_DIR + r"/diamonds_3.png", SPRITE_SCALING_CARDS)
        self.diamonds_4_sprite = arcade.Sprite(SPRITES_DIR + r"/diamonds_4.png", SPRITE_SCALING_CARDS)
        self.diamonds_5_sprite = arcade.Sprite(SPRITES_DIR + r"/diamonds_5.png", SPRITE_SCALING_CARDS)
        self.diamonds_6_sprite = arcade.Sprite(SPRITES_DIR + r"/diamonds_6.png", SPRITE_SCALING_CARDS)
        self.diamonds_7_sprite = arcade.Sprite(SPRITES_DIR + r"/diamonds_7.png", SPRITE_SCALING_CARDS)
        self.diamonds_8_sprite = arcade.Sprite(SPRITES_DIR + r"/diamonds_8.png", SPRITE_SCALING_CARDS)
        self.diamonds_9_sprite = arcade.Sprite(SPRITES_DIR + r"/diamonds_9.png", SPRITE_SCALING_CARDS)
        self.diamonds_10_sprite = arcade.Sprite(SPRITES_DIR + r"/diamonds_10.png", SPRITE_SCALING_CARDS)
        self.diamonds_jack_sprite = arcade.Sprite(SPRITES_DIR + r"/diamonds_jack.png", SPRITE_SCALING_CARDS)
        self.diamonds_queen_sprite = arcade.Sprite(SPRITES_DIR + r"/diamonds_queen.png", SPRITE_SCALING_CARDS)
        self.diamonds_king_sprite = arcade.Sprite(SPRITES_DIR + r"/diamonds_king.png", SPRITE_SCALING_CARDS)
        self.joker_black_sprite = arcade.Sprite(SPRITES_DIR + r"/joker_black.png", SPRITE_SCALING_CARDS)
        self.joker_red_sprite = arcade.Sprite(SPRITES_DIR + r"/joker_red.png", SPRITE_SCALING_CARDS)
        self.blue_background_sprite = arcade.Sprite(SPRITES_DIR + r"/blue.png", SPRITE_SCALING_CARDS)
        self.red_background_sprite = arcade.Sprite(SPRITES_DIR + r"/red.png", SPRITE_SCALING_CARDS)

        # Add cards sprites
        self.cards_list.append(self.clubs_ace_sprite)
        self.cards_list.append(self.clubs_2_sprite)
        self.cards_list.append(self.clubs_3_sprite)
        self.cards_list.append(self.clubs_4_sprite)
        self.cards_list.append(self.clubs_5_sprite)
        self.cards_list.append(self.clubs_6_sprite)
        self.cards_list.append(self.clubs_7_sprite)
        self.cards_list.append(self.clubs_8_sprite)
        self.cards_list.append(self.clubs_9_sprite)
        self.cards_list.append(self.clubs_10_sprite)
        self.cards_list.append(self.clubs_jack_sprite)
        self.cards_list.append(self.clubs_queen_sprite)
        self.cards_list.append(self.clubs_king_sprite)
        self.cards_list.append(self.hearts_ace_sprite)
        self.cards_list.append(self.hearts_2_sprite)
        self.cards_list.append(self.hearts_3_sprite)
        self.cards_list.append(self.hearts_4_sprite)
        self.cards_list.append(self.hearts_5_sprite)
        self.cards_list.append(self.hearts_6_sprite)
        self.cards_list.append(self.hearts_7_sprite)
        self.cards_list.append(self.hearts_8_sprite)
        self.cards_list.append(self.hearts_9_sprite)
        self.cards_list.append(self.hearts_10_sprite)
        self.cards_list.append(self.hearts_jack_sprite)
        self.cards_list.append(self.hearts_queen_sprite)
        self.cards_list.append(self.hearts_king_sprite)
        self.cards_list.append(self.spades_ace_sprite)
        self.cards_list.append(self.spades_2_sprite)
        self.cards_list.append(self.spades_3_sprite)
        self.cards_list.append(self.spades_4_sprite)
        self.cards_list.append(self.spades_5_sprite)
        self.cards_list.append(self.spades_6_sprite)
        self.cards_list.append(self.spades_7_sprite)
        self.cards_list.append(self.spades_8_sprite)
        self.cards_list.append(self.spades_9_sprite)
        self.cards_list.append(self.spades_10_sprite)
        self.cards_list.append(self.spades_jack_sprite)
        self.cards_list.append(self.spades_queen_sprite)
        self.cards_list.append(self.spades_king_sprite)
        self.cards_list.append(self.diamonds_ace_sprite)
        self.cards_list.append(self.diamonds_2_sprite)
        self.cards_list.append(self.diamonds_3_sprite)
        self.cards_list.append(self.diamonds_4_sprite)
        self.cards_list.append(self.diamonds_5_sprite)
        self.cards_list.append(self.diamonds_6_sprite)
        self.cards_list.append(self.diamonds_7_sprite)
        self.cards_list.append(self.diamonds_8_sprite)
        self.cards_list.append(self.diamonds_9_sprite)
        self.cards_list.append(self.diamonds_10_sprite)
        self.cards_list.append(self.diamonds_jack_sprite)
        self.cards_list.append(self.diamonds_queen_sprite)
        self.cards_list.append(self.diamonds_king_sprite)
        self.cards_list.append(self.joker_black_sprite)
        self.cards_list.append(self.joker_red_sprite)
        self.cards_list.append(self.blue_background_sprite)
        self.cards_list.append(self.red_background_sprite)

        # Set player hand
        # self.player_hand_list = [random.choice(self.cards_list) for _ in range(5)]
        # [self.player_hand_list.append(i) for i in random.choice(self.cards_list) for _ in range(5)]
        self.player_hand_list.append(self.clubs_ace_sprite)
        self.player_hand_list.append(self.clubs_2_sprite)

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