#################################################
#                   Draw SVG Stub
#
# v.3.023
# 20230709
#
# DrawSVG Quick Reference
# https://github.com/cduck/drawsvg/blob/master/docs/index.md
#################################################
__author__ = 'Rodrigo Nobrega'


# import
import sys
import os
from pathlib import Path
import drawsvg as dw


# Global variables
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 576
BGCOLOUR = "#5ae65a"
OUTPUT_FILE = Path("my_svg.svg")


class Screen(object):
    """
    Class representing a screen object.

    Attributes:
        screen (drawsvg.Drawing): SVG drawing object representing the screen.
    """
    # TODO: create screen with different sizes, colour
    def __init__(self) -> None:
        """
        Initialize the Screen object.

        This creates a new SVG drawing object with the specified width and height,
        and sets the background color.

        Args:
            None
        Returns:
            None
        """
        self.screen = dw.Drawing(SCREEN_WIDTH, SCREEN_HEIGHT, id_prefix='screen')
        self.set_background()

    def set_background(self):
        """
        Set the background of the screen.

        This creates a rectangle with the specified dimensions and color,
        representing the background of the screen, and appends it to the screen drawing.

        Args:
            None
        Returns:
            None
        """
        canvas = dw.Rectangle(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT,
                              fill=BGCOLOUR, stroke='black',
                              stroke_width=1, stroke_opacity=1)
        self.screen.append(canvas)
        return


class Pen(object):
    """
    Class representing a pen.

    Attributes:
        x (float): The x-coordinate of the pen.
        y (float): The y-coordinate of the pen.
        colour (str): The colour of the pen.
    """

    def __init__(self, startx=SCREEN_WIDTH / 2, starty=SCREEN_HEIGHT / 2, colour="black"):
        """
        Initialize the Pen object.

        Args:
            startx (float, optional): The starting x-coordinate of the pen. Defaults to SCREEN_WIDTH / 2.
            starty (float, optional): The starting y-coordinate of the pen. Defaults to SCREEN_HEIGHT / 2.
            colour (str, optional): The colour of the pen. Defaults to "black".
        """
        self.x = startx
        self.y = starty
        self.colour = colour

    def __repr__(self):
        """
        Return a string representation of the pen.

        Returns:
            str: The string representation of the pen.
        """
        return f"X: {self.x}     Y: {self.y}    Colour: {self.colour}"

    def set_x(self, new_value):
        """
        Set the x-coordinate of the pen.

        Args:
            new_value (float): The new value for the x-coordinate.
        """
        self.x = new_value

    def set_y(self, new_value):
        """
        Set the y-coordinate of the pen.

        Args:
            new_value (float): The new value for the y-coordinate.
        """
        self.y = new_value


class DrawRelative(object):
    """
    Class for drawing relative coordinates.

    Attributes:
        pen (Pen): The pen object used for drawing.
        screen (Screen): The screen object to draw on.
        x (float): The current x-coordinate.
        y (float): The current y-coordinate.
        draw_string (str): The string containing the drawing instructions.
        step_list (list): The list of individual drawing steps.
        coordinates_list (list): The list of coordinates for the drawing.

    Methods:
        process_draw: Process the draw string and extract individual drawing steps.
        process_coordinates: Process the drawing steps and update the coordinates.
        draw: Draw the coordinates on the screen.
    """

    def __init__(self, pen: Pen, screen: Screen):
        """
        Initialize the DrawRelative object.

        Args:
            pen (Pen): The pen object used for drawing.
            screen (Screen): The screen object to draw on.
        """
        self.pen = pen
        self.screen = screen
        self.x = self.pen.x
        self.y = self.pen.y
        self.draw_string = ""
        self.step_list = []
        self.coordinates_list = []

    def process_draw(self, draw_string: str):
        """
        Process the draw string and extract individual drawing steps.

        Args:
            draw_string (str): The string containing the drawing instructions.
        """
        # restarts a step_list
        self.step_list = []
        # if a draw_string is provided, process it by splitting individual direction/scalar pairs
        if draw_string:
            split_start = 0
            for i in range(1, len(draw_string)):
                # splits the string every time a new direction is found
                if draw_string[i].isalpha() and draw_string[i - 1].isdigit():
                    self.step_list.append(draw_string[split_start:i])
                    split_start = i
            self.step_list.append(draw_string[split_start:])

        return

    def process_coordinates(self):
        """
        Process the drawing steps and update the coordinates.
        """
        # TODO: process colour (C), moves (M) and blank moves (BM)
        # TODO: when direction has no scalar use 1
        # restart a coordinates list, and start with the current pen position
        self.coordinates_list = []
        self.coordinates_list.append(self.x)
        self.coordinates_list.append(self.y)
        direction = ""
        scalar = float()

        # iterate the steps list
        for step in self.step_list:
            for i in range(1, len(step)):
                # for each step, split the string between its direction and its magnitude/amount/scalar
                if step[i].isdigit() and step[i - 1].isalpha():
                    direction = step[:i]
                    scalar = float(step[i:])
            # calculate the new coordinates
            if direction.upper() == "U":
                self.y -= scalar
            elif direction.upper() == "D":
                self.y += scalar
            elif direction.upper() == "L":
                self.x -= scalar
            elif direction.upper() == "R":
                self.x += scalar
            elif direction.upper() == "E":
                self.y -= scalar
                self.x += scalar
            elif direction.upper() == "F":
                self.y += scalar
                self.x += scalar
            elif direction.upper() == "G":
                self.y += scalar
                self.x -= scalar
            elif direction.upper() == "H":
                self.y -= scalar
                self.x -= scalar
            # add the new coordinates to the coordinates list, and update pen position
            self.coordinates_list.append(self.x)
            self.coordinates_list.append(self.y)
            self.pen.set_x(self.x)
            self.pen.set_y(self.y)

        return

    def draw(self, draw_string: str):
        """
        Draw the coordinates on the screen.

        Args:
            draw_string (str): The string containing the drawing instructions.
        """
        # interpret the drawing string, and calculate the polyline coordinates
        self.process_draw(draw_string)
        self.process_coordinates()

        # draw the polylines to screen, unpacking the coordinates list
        lines = dw.Lines(*self.coordinates_list, fill='none', stroke=self.pen.colour)
        self.screen.screen.append(lines)

        return


def save(contents, filename):
    contents.save_svg(filename)
    return


# main routine
def main():
    """ Main method """
    # Setup screen
    my_screen = Screen()
    # Draw elements
    # 
    # Save SVG file
    save(my_screen.screen, OUTPUT_FILE)
    if sys.platform.startswith('win'):
        os.startfile(OUTPUT_FILE)
    elif sys.platform.startswith('darwin'):
        os.open(OUTPUT_FILE, os.O_RDWR)


# execute main
if __name__ == "__main__":
    main()