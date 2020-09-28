#################################################
#                   Spawn
# Conway's Game of Life  in Python Arcade
#################################################
__author__ = 'Rodrigo Nobrega'
__version__ = 0.05


# Imports
import arcade
import numpy as np
import timeit


# Constants
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 576
SCREEN_TITLE = 'Spawn - Game of Life'
# BGCOLOUR = (220, 220, 220)  # GAINSBORO
BGCOLOUR = (227, 218, 201)	 # BONE
RESOLUTION = 20


# Classes
class Spawn(arcade.Window):
    """
    Main application class.

    NOTE: Go ahead and delete the methods you don't need.
    If you do need a method, delete the 'pass' and replace it
    with your own code. Don't leave 'pass' in this program.
    """

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        # arcade.set_background_color(arcade.color.AMAZON)
        arcade.set_background_color(BGCOLOUR)

        # If you have sprite lists, you should create them here,
        # and set them to None
        self.board = None

    def setup(self, board):
        # Create your sprites and sprite lists here
        self.board = board

    def on_draw(self):
        """
        Render the screen.
        """

        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        arcade.start_render()

        # Call draw() on all your sprite lists below
        self.board.drawboard()

    def update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        pass
        # self.board.newrandomgrid()
        # self.board.drawboard()

    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.

        For a full list of keys, see:
        http://arcade.academy/arcade.key.html
        """
        # Quit
        if key == arcade.key.Q:
            # Quit immediately
            arcade.close_window()

        # Random grid
        if key == arcade.key.R:
            # Generate
            self.board.randomise()

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


class Habitat(object):
    def __init__(self, width, height, size):
        # define random initial state
        self.grid = None
        self.width = width
        self.height = height
        self.size = size
        # self.randomise()
        self.hardcode()

    def __repr__(self):
        return "\n==============================\n Spawn\n==============================\n" \
               " <Q> to quit\n" \
               " <R> to randomise board\n"

    def drawboard(self):
        for li in range(self.grid.shape[0]):
            for co in range(self.grid.shape[1]):
                if self.grid[li, co] == 1:
                    arcade.draw_xywh_rectangle_filled(co * RESOLUTION,
                                                      (self.grid.shape[0]-1 - li) * RESOLUTION,
                                                      RESOLUTION, RESOLUTION, (0, 0, 0))
                # else:
                #     arcade.draw_xywh_rectangle_outline(co * RESOLUTION, li * RESOLUTION,
                #                                        RESOLUTION, RESOLUTION, (0, 0, 0))

    def randomise(self):
        self.grid = np.random.randint(2, size=(int(self.height/self.size),
                                               int(self.width/self.size)))

    def hardcode(self):
        self.grid = np.zeros((int(self.height/self.size), int(self.width/self.size)))
        self.grid[-1] = 1
        self.grid[-10] = 1
        self.grid[0] = 1
        self.grid[:, 0] = 1
        self.grid[:, -1] = 1


# main routine
def main():
    """ Main method """
    # from Rodrigo
    bo = Habitat(SCREEN_WIDTH, SCREEN_HEIGHT, RESOLUTION)
    print(bo)
    # from template
    game = Spawn(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup(bo)
    arcade.run()


# execute main
if __name__ == "__main__":
    # print('\n==============================\n Spawn\n==============================\n')
    # print(' <Q> to quit')
    # print('\n')
    main()

