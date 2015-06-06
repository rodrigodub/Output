# INPUT
# Programacao de Jogos 2
#
# Dispare seu míssil

# Implementacao em Python by RN
# com uso da biblioteca CURSES para 
# manipulacao da janela de texto (terminal)

# resource: https://docs.python.org/3.4/howto/curses.html#curses-howto
# resource: https://docs.python.org/3.4/library/curses.html?highlight=curses#module-curses

# v2.0013
# 20150606

import time
import curses
import random
from curses import wrapper


class Cannon(object):
	def __init__(self, stdscr):
		stdscr.addstr(47, 38, chr(0x2584)+chr(0x2588)+chr(0x2584))

	def fire(self, stdscr):
		for n in range(45, 0, -1):
			stdscr.addstr(n, 39, chr(0x25B2))
			stdscr.addstr(n+1, 39, ' ')
			time.sleep(0.025)
			stdscr.refresh()


def fireloop(stdscr, cannon):
	fim = ''
	while fim != 'x':
		fim = stdscr.getkey()
		if fim == 'f':
			cannon.fire(stdscr)


def main(stdscr):
	# disable blinking cursor
	curses.curs_set(False)
	# clear screen
	stdscr.clear()

	# main code
	a = Cannon(stdscr)
	fireloop(stdscr, a)

	# end main code
	#stdscr.getkey()


if __name__ == '__main__':
	wrapper(main)
	