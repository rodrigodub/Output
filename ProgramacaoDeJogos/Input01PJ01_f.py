# INPUT
# Programacao de Jogos 01
#
# Satelite

# Implementacao em Python by RN
# com uso da biblioteca CURSES para 
# manipulacao da janela de texto (terminal)

# resource: https://docs.python.org/3.4/howto/curses.html#curses-howto
# resource: https://docs.python.org/3.4/library/curses.html?highlight=curses#module-curses

# v1.0
# 20150602

import time, curses
from curses import wrapper

class Satelite(object):
	def __init__(self, stdscr, posy, posx):
		self.position1(stdscr, posy, posx)

	def position1(self, stdscr, posy, posx):
		stdscr.addstr(posy+0, posx, 14 * chr(0x0020))
		stdscr.addstr(posy+1, posx, 2 * chr(0x0020) + chr(0x2588) + 7 * chr(0x0020) + chr(0x2588) + 3 * chr(0x0020))
		stdscr.addstr(posy+2, posx, 3 * chr(0x0020) + chr(0x2588) + 5 * chr(0x0020) + chr(0x2588) + 4 * chr(0x0020))
		stdscr.addstr(posy+3, posx, 4 * chr(0x0020) + 5 * chr(0x2588) + 5 * chr(0x0020))
		stdscr.addstr(posy+4, posx, chr(0x0020) + 11 * chr(0x2588) + 2 * chr(0x0020))
		stdscr.addstr(posy+5, posx, 6 * (chr(0x0020) + chr(0x2588)) + 2 * chr(0x0020))
		stdscr.addstr(posy+6, posx, 6 * (chr(0x0020) + chr(0x2588)) + 2 * chr(0x0020))
		stdscr.addstr(posy+7, posx, 2 * chr(0x0020) + 9 * chr(0x2588) + 3 * chr(0x0020))
		stdscr.addstr(posy+8, posx, chr(0x0020) + chr(0x2588) + 9 * chr(0x0020) + chr(0x2588) + 2 * chr(0x0020))
		stdscr.addstr(posy+9, posx, chr(0x2588) + 11 * chr(0x0020) + chr(0x2588) + chr(0x0020))

def main(stdscr):
	# disable blinking cursor
	curses.curs_set(False)
	# clear screen
	stdscr.clear()

	# main code
	a = Satelite(stdscr, 10, 2)

	# end main code
	stdscr.getkey()


if __name__ == '__main__':
	wrapper(main)