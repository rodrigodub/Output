# INPUT
# Programação de Jogos 4
#
# Campo Minado / Movimento

# Implementação em Python by RN

# v2.0032
# 20150614

# import math
import curses
from curses import wrapper


class Tank(object):
    def __init__(self, stdscr):
        self.tank = chr(0x2588)
        self.clean = ' '
        self.coord = [39, 23]
        self.lastcoord = [0, 0]
        self.draw(stdscr)

    def setPos(self, x, y):
        self.lastcoord = self.coord
        self.coord = [x, y]

    def draw(self, stdscr):
        stdscr.addstr(self.lastcoord[1], self.lastcoord[0], self.clean)
        stdscr.addstr(self.coord[1], self.coord[0], self.tank)


def main(stdscr):
    # disable blinking cursor
    curses.curs_set(False)
    # clear screen
    stdscr.clear()

    # main code
    a = Tank(stdscr)

    # end main code
    stdscr.getkey()


if __name__ == '__main__':
    wrapper(main)
