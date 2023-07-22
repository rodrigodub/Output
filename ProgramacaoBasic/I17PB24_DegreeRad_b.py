#################################################
#                   INPUT 17
#
# Programacao Basic 24
# BÚSSOLAS E RELÓGIOS
#
# Usage:
# > python I17PB24_DegreeRad_b.py
#
# v.3.028
# 20230722
#
# Uses the Stub_SVG.py v.3.028
#################################################
__author__ = 'Rodrigo Nobrega'


# import
import math
import sys
sys.path.extend(['../Stub'])
import numpy as np
import drawsvg as dw
from Stub_SVG import *


# Convert degrees to radians
def degrees_to_radians(degrees):
    radians = degrees * (math.pi / 180)
    return radians

# Convert radians to degrees
def radians_to_degrees(radians):
    degrees = radians * (180 / math.pi)
    return degrees

def draw_compass(the_screen, x, y, size, needle=None):
    ticksize = int(size / 10)
    t = Text(the_screen)
    direction = ["N", "E", "S", "W"]
    # compass body
    compass = dw.Circle(x, y, size, stroke='darkblue', fill='none', stroke_width=2)
    the_screen.screen.append(compass)
    # tick marks
    for i in np.arange(0, 2 * np.pi, np.pi / 4):
        the_screen.screen.append(dw.Line(x + (size - ticksize) * math.sin(i),
                                         y - (size - ticksize) * math.cos(i),
                                         x + size * math.sin(i),
                                         y - size * math.cos(i),
                                         stroke="#ff4477", stroke_width=2
                                         ))
    # angles
    for i in np.arange(0, 2 * np.pi, np.pi / 4):
        t.write(f"{int(radians_to_degrees(i))}",
                x + (size - ticksize * 3) * math.sin(i) - ticksize / 2,
                y - (size - ticksize * 3) * math.cos(i) + ticksize / 2,
                int(ticksize),
                )
    # orientation
    di = 0
    for i in np.arange(0, 2 * np.pi, np.pi / 2):
        t.write(direction[di],
                x + (size + ticksize * 2) * math.sin(i) - ticksize / 2,
                y - (size + ticksize * 2) * math.cos(i) + ticksize / 2,
                int(ticksize * 1.5),
                )
        di += 1
    # center
    the_screen.screen.append(dw.Line(x - ticksize, y,
                                     x + ticksize, y,
                                     stroke="#ff4477", stroke_width=2
                                     ))
    the_screen.screen.append(dw.Line(x, y - ticksize,
                                     x, y + ticksize,
                                     stroke="#ff4477", stroke_width=2
                                     ))
    # needle
    if needle:
        needle_value = int(needle)
        the_screen.screen.append(dw.Line(x, y,
                                         x + (size - ticksize * 3) * math.sin(degrees_to_radians(needle_value)),
                                         y - (size - ticksize * 3) * math.cos(degrees_to_radians(needle_value)),
                                         stroke="#8A4F7D", stroke_width=4
                                         ))
    return

# main routine
def main():
    """ Main method """
    my_screen = Screen("#88d9e6")
    # p = Pen(400, 288, "blue")
    # d = DrawRelative(p, my_screen)

    angle = input("\nEnter angle in degrees: ")

    # draw_compass(my_screen, 512, 288, 200)
    draw_compass(my_screen, 512, 288, 200, angle)
    # draw_compass(my_screen, 300, 400, 100)
    # draw_compass(my_screen, 700, 288, 400)

    save(my_screen.screen, "./data/compass.svg")


# execute main
if __name__ == "__main__":
    main()