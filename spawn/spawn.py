#################################################
#                   Spawn
# Conway's Game of Life  in Python Arcade
#################################################
__author__ = 'Rodrigo Nobrega'
__version__ = 0.15


# Imports
import arcade
import numpy as np
# import timeit


# Constants
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 576
RESOLUTION = 8
SCREEN_TITLE = 'Spawn - Game of Life'
LIFEFILE = 'life1.csv'
# BGCOLOUR = (220, 220, 220)  # GAINSBORO
# BGCOLOUR = (227, 218, 201)	 # BONE
BGCOLOUR = (27, 153, 139)	 # Persian Green
LIFECOLOUR = (74, 0, 31)  # Tyrian Purple


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
        self.keycount = None

    def setup(self, environment):
        # Create your sprites and sprite lists here
        self.board = environment
        self.keycount = 0

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
        if self.keycount % 2 == 0:
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
            # Clean
            self.board.cleanup()

        # Random grid
        if key == arcade.key.R:
            # Generate
            self.board.randomise()

        # Reset the Environment
        if key == arcade.key.H:
            # Generate
            self.board.setupenvironment()

        # Next generation, manual
        if key == arcade.key.N:
            # Next
            self.board.nextgeneration()

        # Toggle auto generation
        if key == arcade.key.A:
            # Toggle automatic/manual
            self.keycount += 1

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
        self.lifelist = self.readenvironment(LIFEFILE)
        self.cleanup()
        self.setupenvironment()

    def __repr__(self):
        return "\n==============================\n   Spawn   (version {})" \
               "\n==============================\n" \
               " < Q > : Quit\n" \
               " < C > : Clean up environment\n" \
               " < R > : Randomise board\n" \
               " < H > : recreate the Environment\n" \
               " < N > : Next generation\n" \
               " < A > : Toggle Automatic/Manual generation\n"

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
        if len(cells) > 0:
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

    def readenvironment(self, environmentfile):
        lifelist = []
        with open(environmentfile, 'r') as l:
            a = l.readlines()[1:]
        for line in a:
            elements = line.split(',')
            lifelist.append([elements[0], int(elements[1]), int(elements[2])])
        return lifelist

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
        for i in self.lifelist:
            self.insert(self.zoo[i[0]], i[1], i[2])
        # self.insert(self.zoo['blinker'], 10, 30)
        # self.insert(self.zoo['blinker'], 40, 80)
        # self.insert(self.zoo['block'], 20, 40)

    def nextgeneration(self):
        """
        Apply the Game of Life rules, and set the next generation
        """
        # 1. Duplicate the grid and add the borders
        # 1.1. duplicate
        oldgrid = self.grid.copy()
        # 1.2. insert the last line to the beginning, and append the first to the end
        oldgrid = np.vstack([self.grid[-1], oldgrid])
        oldgrid = np.vstack([oldgrid, self.grid[0]])
        # 1.3. insert the last column to the beginning, and append the first column to the end
        oldgrid = np.column_stack([oldgrid[:, -1], oldgrid])
        oldgrid = np.column_stack([oldgrid, oldgrid[:, 1]])
        # 2. Calculate the neighbours grid
        neighbours = np.zeros(self.grid.shape, dtype=int)
        for li in range(self.grid.shape[0]):
            for co in range(self.grid.shape[1]):
                neighbours[li, co] = 0
                neighbours[li, co] += oldgrid[li, co]
                neighbours[li, co] += oldgrid[li, co + 1]
                neighbours[li, co] += oldgrid[li, co + 2]
                neighbours[li, co] += oldgrid[li + 1, co]
                neighbours[li, co] += oldgrid[li + 1, co + 2]
                neighbours[li, co] += oldgrid[li + 2, co]
                neighbours[li, co] += oldgrid[li + 2, co + 1]
                neighbours[li, co] += oldgrid[li + 2, co + 2]
        # 3. Iterate lines and columns, compare with neighbours, and apply rules
        for li in range(self.lines):
            for co in range(self.columns):
                # Any live cell with fewer than two live neighbours dies, as if by underpopulation.
                # Any live cell with two or three live neighbours lives on to the next generation.
                # Any live cell with more than three live neighbours dies, as if by overpopulation.
                # Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
                if self.grid[li, co] == 1 and (neighbours[li, co] == 2 or
                                               neighbours[li, co] == 3):
                    self.grid[li, co] = 1
                elif self.grid[li, co] == 0 and neighbours[li, co] == 3:
                    self.grid[li, co] = 1
                else:
                    self.grid[li, co] = 0

    def insert(self, life, positionline, positioncolumn):
        """Insert a life at a given position, expressed in percentage of the screen size"""
        # li0 = positionline
        # li1 = positionline + life.shape[0]
        # co0 = positioncolumn
        # co1 = positioncolumn + life.shape[1]
        # self.grid[li0:li1, co0:co1] = life
        # test if position is in the range of 0-100%
        bottom = positionline + life.shape[0]
        if bottom > 100:
            positionline = bottom - (bottom // 100) * 100
        placeline = int(SCREEN_HEIGHT / RESOLUTION * positionline / 100)
        #
        left = positioncolumn + life.shape[1]
        if left > 100:
            positioncolumn = left - (left // 100) * 100
        placecol = int(SCREEN_WIDTH / RESOLUTION * positioncolumn / 100)
        # calculate life boundaries
        li0 = placeline
        li1 = li0+life.shape[0]
        co0 = placecol
        co1 = co0+life.shape[1]
        # place life in grid
        self.grid[li0:li1, co0:co1] = life


class Zoo(object):
    def __init__(self):
        self.fauna = {'blinker': np.array([[0, 0, 0],
                                           [1, 1, 1],
                                           [0, 0, 0]], dtype=int),
                      'block': np.array([[1, 1],
                                         [1, 1]], dtype=int),
                      'glider': np.array([[0, 1, 0],
                                          [0, 0, 1],
                                          [1, 1, 1]], dtype=int)
                      }


# main routine
def main():
    """ Main method """
    # from Rodrigo
    bo = Environment(SCREEN_WIDTH, SCREEN_HEIGHT, RESOLUTION)
    print(bo.__repr__().format(__version__))
    # from template
    game = Spawn(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup(bo)
    arcade.run()


# execute main
if __name__ == "__main__":
    main()

