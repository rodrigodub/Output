# INPUT
# Código de Máquina 3
#
# BIN, DEC, HEX

# Implementação em Python by RN

# v2.0031
# 20150614

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


class HexNumber(object):
    def __init__(self, num):
        b = BinaryNumber(num)
        self.result = conv.ConvertDecToBase(16, num).converted
        self.formatted = '{}  =  {}                     {}  =  {}'.format(b.result[0:4], self.result[0]
                                                                        , b.result[4:], self.result[1])


class Screen(object):
    def __init__(self, stdscr):
        stdscr.addstr(2, 1, '============================================================')
        stdscr.addstr(3, 1, '==                      BIN , DEC, HEX                    ==')
        stdscr.addstr(4, 1, '============================================================')
        stdscr.addstr(5, 1, '--                                                        --')
        stdscr.addstr(6, 1, '--                          BINÁRIO                       --')
        stdscr.addstr(7, 1, '--                                                        --')
        stdscr.addstr(9, 1, '------------------------------------------------------------')
        stdscr.addstr(10, 1, '--                                                        --')
        stdscr.addstr(11, 1, '--                          DECIMAL                       --')
        stdscr.addstr(12, 1, '--                                                        --')
        stdscr.addstr(14, 1, '--                                                        --')
        stdscr.addstr(16, 1, '------------------------------------------------------------')
        stdscr.addstr(17, 1, '--                                                        --')
        stdscr.addstr(18, 1, '--                        HEXADECIMAL                     --')
        stdscr.addstr(19, 1, '--                                                        --')
        stdscr.addstr(21, 1, '--                                                        --')
        stdscr.addstr(23, 1, '------------------------------------------------------------')
        stdscr.addstr(24, 1, '-        press [up / down]         |        x : exit       -')
        stdscr.addstr(25, 1, '------------------------------------------------------------')

    def updateNumbers(self, stdscr, num):
        # stdscr.addstr(8, 10, '{}'.format(bin.result))
        stdscr.addstr(8, 1, '                                                            ')
        stdscr.addstr(8, 3, BinaryNumber(num).formatted)
        stdscr.addstr(13, 1, '                                                            ')
        stdscr.addstr(13, 3, DecimalNumber(num).formatted)
        stdscr.addstr(15, 1, '                                                            ')
        stdscr.addstr(15, 32, DecimalNumber(num).result)
        stdscr.addstr(20, 1, '                                                            ')
        stdscr.addstr(20, 12, HexNumber(num).formatted)
        stdscr.addstr(22, 1, '                                                            ')
        stdscr.addstr(22, 32, HexNumber(num).result)
        stdscr.refresh()


def main(stdscr):
    # disable blinking cursor
    curses.curs_set(False)
    # clear screen
    stdscr.clear()

    # main code
    a = Screen(stdscr)
    num = 0
    a.updateNumbers(stdscr, num)
    k = ''
    while k != 'x':
        k = stdscr.getkey()
        if k == 'KEY_UP' and num < 255:
            num += 1
        elif k == 'KEY_DOWN' and num > 0:
            num -= 1
        a.updateNumbers(stdscr, num)

    # end main code
    # stdscr.getkey()


if __name__ == '__main__':
    wrapper(main)
