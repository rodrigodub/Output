#################################################
#                   INPUT # x
# Section
# Title
# UK : Input # y
# 
# Usage:
# > python filename.py
#
# v.3.022
# 20230707
#
# https://
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
    def __init__(self) -> None:
        self.screen = dw.Drawing(SCREEN_WIDTH, SCREEN_HEIGHT, id_prefix='screen')
        self.set_background()
    
    def set_background(self):
        canvas = dw.Rectangle(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT,
                      fill=BGCOLOUR, stroke='black',
                      stroke_width=1, stroke_opacity=1)
        self.screen.append(canvas)


class Draw(object):
    pass


def save(contents, filename):
    contents.save_svg(filename)


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