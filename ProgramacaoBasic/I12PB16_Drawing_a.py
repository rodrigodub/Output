#################################################
#                   INPUT 12
#
# Programacao Basic 16
# Recursos Gráficos Sofisticados
#
# Usage:
# > python3 I12PB16_Drawing_a.py
#
# v.3.024
# 20230709
#
# Uses the Stub_SVG.py v.3.023
#################################################
__author__ = 'Rodrigo Nobrega'


# import
import sys
from pathlib import Path
sys.path.extend(['../Stub'])
from Stub_SVG import *


# main routine
def main():
    """ Main method """
    a = "R28E2U3L6U1R6E2R5F2D3R3U2R7D2R4U9E2R4F2D5R3U2R4U6E3R5D8"
    b = "R3U24L3U1R8D1L4D24R1F2R5D4R4U4R6U9E3R5D10R4U2R4U14R1D10R3U2"
    c = "R4D11R7U3E2R4F2D3R1D8R3U5E2R8D2R6U2R7U1E2R6F2D4R4U4E2R5F2"
    e = "R6D1L6D3R24G12L195H4U5"

    my_screen = Screen()
    p = Pen(400, 288, "blue")
    d = DrawRelative(p, my_screen)

    d.draw(a)
    d.draw(b)
    d.draw(c)
    d.draw(e)

    save(my_screen.screen, "./data/ship.svg")


# execute main
if __name__ == "__main__":
    main()