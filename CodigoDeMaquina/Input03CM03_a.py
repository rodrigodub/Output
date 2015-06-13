# INPUT
# Código de Máquina 3
#
# BIN, DEC, HEX

# Implementação em Python by RN

# v2.0025
# 20150613

import math
import Input02CM02_a as conv
import curses
from curses import wrapper


class BinaryNumber(object):
    def __init__(self, num):
        self.result = ('00000000' +  conv.ConvertDecToBase(2, num).converted)[-8:]
        self.formatted = '       '.join([i for i in self.result])


class DecimalNumber(object):
    def __init__(self, num):
        b = BinaryNumber(num)
        d = []
        self.result = '{}'.format(num)
        for i in range(0, 8):
            if int(b.result[i]) == 1:
                d.append('{}'.format(pow(2, 7-i)))
            else:
                d.append('0')
        self.formatted = '   +  '.join([i for i in d])
        # self.formattedtest = ' 0       0       0       1       1       0       0       1'
        # self.formatted = ' 0 ' + '  +   0   +   0   +   1   +   1   +   0   +   0   +   1'


class HexNumber(object):
    def __init__(self):
        pass


class Screen(object):
    def __init__(self, stdscr):
        stdscr.addstr(2, 1, '============================================================')
        stdscr.addstr(3, 1, '==                      BIN , DEC, HEX                    ==')
        stdscr.addstr(4, 1, '============================================================')
        stdscr.addstr(6, 1, '==                          BINÁRIO                       ==')
        stdscr.addstr(14, 1, '==                          DECIMAL                       ==')
        stdscr.addstr(22, 1, '==                        HEXADECIMAL                     ==')

    def updateNumbers(self, stdscr, num):
        # stdscr.addstr(8, 10, '{}'.format(bin.result))
        stdscr.addstr(10, 3, BinaryNumber(255).formatted)
        stdscr.addstr(17, 3, DecimalNumber(255).formatted)
        stdscr.addstr(19, 30, DecimalNumber(255).result)


def main(stdscr):
    # disable blinking cursor
    curses.curs_set(False)
    # clear screen
    stdscr.clear()

    # main code
    a = Screen(stdscr)
    a.updateNumbers(stdscr, 25)
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
