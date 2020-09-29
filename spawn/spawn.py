#################################################
#                   Spawn
# Conway's Game of Life  in Python Arcade
#################################################
__author__ = 'Rodrigo Nobrega'
__version__ = 0.11


# Imports
import arcade
import numpy as np
# import timeit


# Constants
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 576
SCREEN_TITLE = 'Spawn - Game of Life'
# BGCOLOUR = (220, 220, 220)  # GAINSBORO
# BGCOLOUR = (227, 218, 201)	 # BONE
BGCOLOUR = (27, 153, 139)	 # Persian Green
LIFECOLOUR = (74, 0, 31)  # Tyrian Purple
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

    def setup(self, environment):
        # Create your sprites and sprite lists here
        self.board = environment

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
        # pass
        # self.board.randomise()
        # self.board.drawboard()
        self.board.nextgeneration()

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

        # Reset the Environment
        if key == arcade.key.H:
            # Generate
            self.board.setupenvironment()

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


class Environment(object):
    """
    Environment defines the place where the life lives, and its rules
    """
    def __init__(self, width, height, size):
        # define initial state
        self.grid = None
        self.columns = int(width / size)
        self.lines = int(height / size)
        self.size = size
        # link the zoo
        self.zoo = Zoo().fauna
        # setup environment
        self.cleanup()
        self.setupenvironment()

    def __repr__(self):
        return "\n==============================\n Spawn" \
               "\n==============================\n" \
               " < Q > : Quit\n" \
               " < C > : Clean up environment\n" \
               " < R > : Randomise board\n" \
               " < H > : recreate the Environment\n"

    def drawboard(self):
        """
        Method to draw the contents of the environment
        """
        # iterate the array and draws a rectangle for each living cell
        cells = []
        for li in range(self.lines):
            for co in range(self.columns):
                if self.grid[li, co] == 1:
                    # arcade.draw_xywh_rectangle_filled(co * self.size,
                    #                                   (self.lines-1 - li) * self.size,
                    #                                   self.size, self.size, LIFECOLOUR)
                    cells.append(((co * self.size) + int(self.size / 2),
                                  ((self.lines-1 - li) * self.size) + int(self.size / 2)))
        arcade.draw_points(tuple(cells), LIFECOLOUR, self.size)

    def cleanup(self):
        """
        Clears up the environment
        """
        self.grid = np.zeros((self.lines, self.columns), dtype=int)

    def randomise(self):
        """
        Recreates the environment with random contents
        """
        self.grid = np.random.randint(2, size=(self.lines,
                                               self.columns))

    def cross(self):
        """
        Creates a specific environment with borders and cross
        """
        self.grid[0] = 1
        self.grid[-1] = 1
        self.grid[:, 0] = 1
        self.grid[:, -1] = 1
        self.grid[int(self.lines / 2)] = 1
        self.grid[:, int(self.columns / 2)] = 1

    def setupenvironment(self):
        """
        Run methods to setup a specific environment
        """
        # 1 clean up
        self.cleanup()
        # 2 randomise
        # self.randomise()
        # 3 draw cross
        # self.cross()
        # 4 populate
        # self.blinker(10, 20)
        # self.blinker(30, 70)
        self.insert(self.zoo['blinker'], 10, 30)
        self.insert(self.zoo['blinker'], 40, 80)
        self.insert(self.zoo['block'], 20, 40)

    # TODO: refactor the function to calculate the neighbours value
    def neighbours(self, li, co, oldgrid):
        """
        Calculates the sum of a cell neighbours,
        based on a previous copy of the grid
        """
        # Calculate the borders pre- and post- indexes
        if li == 0:
            preli = self.lines - 1
        else:
            preli = li - 1
        if li == self.lines - 1:
            posli = 0
        else:
            posli = li + 1
        if co == 0:
            preco = self.columns - 1
        else:
            preco = co - 1
        if co == self.columns - 1:
            posco = 0
        else:
            posco = co + 1
        neighbourstot = oldgrid[preli, preco] + oldgrid[preli, co] + oldgrid[preli, posco] + \
                        oldgrid[li, preco] + oldgrid[li, posco] + \
                        oldgrid[posli, preco] + oldgrid[posli, co] + oldgrid[posli, posco]
        return neighbourstot

    def nextgeneration(self):
        """
        Apply the Game of Life rules, and set the next generation
        """
        # duplicate the grid
        oldgrid = self.grid.copy()
        # iterate lines and columns
        for li in range(self.lines):
            for co in range(self.columns):
                # Any live cell with fewer than two live neighbours dies, as if by underpopulation.
                # Any live cell with two or three live neighbours lives on to the next generation.
                # Any live cell with more than three live neighbours dies, as if by overpopulation.
                # Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
                if self.grid[li, co] == 1 and (
                        self.neighbours(li, co, oldgrid) == 2 or
                        self.neighbours(li, co, oldgrid) == 3):
                    self.grid[li, co] = 1
                elif self.grid[li, co] == 0 and \
                        self.neighbours(li, co, oldgrid) == 3:
                    self.grid[li, co] = 1
                else:
                    self.grid[li, co] = 0

    def insert(self, life, positionline, positioncolumn):
        """Insert a life at a given position"""
        li0 = positionline
        li1 = positionline+life.shape[0]
        co0 = positioncolumn
        co1 = positioncolumn+life.shape[1]
        self.grid[li0:li1, co0:co1] = life


class Zoo(object):
    def __init__(self):
        self.fauna = {'blinker': np.array([[0, 0, 0],
                                           [1, 1, 1],
                                           [0, 0, 0]], dtype=int),
                      'block': np.array([[1, 1],
                                         [1, 1]], dtype=int)}

# main routine
def main():
    """ Main method """
    # from Rodrigo
    bo = Environment(SCREEN_WIDTH, SCREEN_HEIGHT, RESOLUTION)
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

