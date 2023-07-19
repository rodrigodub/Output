#################################################
#                   INPUT 12
#
# Programacao Basic 16
# Recursos Gráficos Sofisticados
#
# Usage:
# > python3 I12PB16_Drawing_b.py
#
# v.3.026
# 20230714
#
# Uses the Stub_SVG.py v.3.025
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

    my_screen = Screen()
    # p = Pen(400, 288, "blue")
    # d = DrawRelative(p, my_screen)
    t = Text(my_screen)

    t.write("TESTING0123456789", 300, 200, 12)
    t.write("This is a longer, bigger text.", 300, 240, 18)
    t.write("And this is even bigger @ # $", 300, 400, 30)

    save(my_screen.screen, "./data/writing_messages.svg")


# execute main
if __name__ == "__main__":
    main()