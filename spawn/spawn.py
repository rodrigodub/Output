#################################################
#                   Spawn
# Conway's Game of Life  in Python Arcade
#################################################
__author__ = 'Rodrigo Nobrega'
__version__ = 0.06


# Imports
import arcade
import numpy as np
# import timeit


# Constants
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 576
SCREEN_TITLE = 'Spawn - Game of Life'
# BGCOLOUR = (220, 220, 220)  # GAINSBORO
BGCOLOUR = (227, 218, 201)	 # BONE
RESOLUTION = 10


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

    def setup(self, habitat):
        # Create your sprites and sprite lists here
        self.board = habitat

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
        # self.board.randomise()
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

        # Clean up
        if key == arcade.key.C:
            # Quit immediately
            self.board.cleanup()

        # Random grid
        if key == arcade.key.R:
            # Generate
            self.board.randomise()

        # Reset the Habitat
        if key == arcade.key.H:
            # Generate
            self.board.setuphabitat()

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
    """
    Habitat defines the place where the life lives, and its rules
    """
    def __init__(self, width, height, size):
        # define initial state
        self.grid = None
        self.columns = int(width / size)
        self.lines = int(height / size)
        self.size = size
        # setup habitat
        self.cleanup()
        self.setuphabitat()

    def __repr__(self):
        return "\n==============================\n Spawn" \
               "\n==============================\n" \
               " < Q > : Quit\n" \
               " < C > : Clean up habitat\n" \
               " < R > : Randomise board\n" \
               " < H > : recreate the Habitat\n"

    def drawboard(self):
        """
        Method to draw the contents of the habitat
        """
        # iterate the array and draws a rectangle for each living cell
        for li in range(self.grid.shape[0]):
            for co in range(self.grid.shape[1]):
                if self.grid[li, co] == 1:
                    arcade.draw_xywh_rectangle_filled(co * self.size,
                                                      (self.grid.shape[0]-1 - li) * self.size,
                                                      self.size, self.size, (0, 0, 0))

    def cleanup(self):
        """
        Clears up the habitat
        """
        self.grid = np.zeros((self.lines, self.columns))

    def randomise(self):
        """
        Recreates the habitat with random contents
        """
        self.grid = np.random.randint(2, size=(self.lines,
                                               self.columns))

    def crosshabitat(self):
        """
        Creates a specific habitat with borders and cross
        """
        self.grid[0] = 1
        self.grid[-1] = 1
        self.grid[:, 0] = 1
        self.grid[:, -1] = 1
        self.grid[int(self.lines / 2)] = 1
        self.grid[:, int(self.columns / 2)] = 1

    def setuphabitat(self):
        """
        Run methods to setup a specific habitat
        """
        # 1 clean up
        # self.cleanup()
        # 2 randomise
        # self.randomise()
        # 3 draw cross
        self.crosshabitat()


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

