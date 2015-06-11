# INPUT
# Código de Máquina 3
#
# BIN, DEC, HEX

# Implementação em Python by RN

# v2.0023
# 20150611

import math
import Input02CM02_a as conv
import curses
from curses import wrapper


class BinaryNumber(object):
    def __init__(self):
        pass


class DecimalNumber(object):
    def __init__(self):
        pass


class HexNumber(object):
    def __init__(self):
        pass


class Screen(object):
    def __init__(self, stdscr):
        stdscr.addstr(2, 1, '============================================================')
        stdscr.addstr(3, 1, '==                      BIN , DEC, HEX                    ==')
        stdscr.addstr(4, 1, '============================================================')


def main(stdscr):
    # disable blinking cursor
    curses.curs_set(False)
    # clear screen
    stdscr.clear()

    # main code
    Screen(stdscr)
    # a = input('Enter Base (up to 36) : ')
    # b = input('Enter Number : ')
    # if int(a) <= 36:
    #     x = conv.ConvertBaseToDec(a, b)
    #     y = conv.ConvertDecToBase(a, x.decimal)
    #     x.verbose()
    #     y.verbose()

    # end main code
    stdscr.getkey()



if __name__ == '__main__':
    wrapper(main)
