# INPUT
# Programacao de Jogos 2
#
# Dispare seu míssil

# Implementacao em Python by RN
# com uso da biblioteca CURSES para 
# manipulacao da janela de texto (terminal)

# resource: https://docs.python.org/3.4/howto/curses.html#curses-howto
# resource: https://docs.python.org/3.4/library/curses.html?highlight=curses#module-curses

# v2.0012
# 20150606

import time
import curses
import random
from curses import wrapper


# class Satelite(object):
# 	def __init__(self, stdscr, posy, posx):
# 		stdscr.refresh()
# 		self.position1(stdscr, posy, posx)
# 		time.sleep(0.2)
# 		stdscr.refresh()
# 		self.position2(stdscr, posy, posx)
# 		time.sleep(0.2)

# 	def position1(self, stdscr, posy, posx):
# 		stdscr.addstr(posy+0, posx, 15 * chr(0x0020))
# 		stdscr.addstr(posy+1, posx, 3 * chr(0x0020) + 1 * chr(0x2588) + 7 * chr(0x0020) + 1 * chr(0x2588) + 3 * chr(0x0020))
# 		stdscr.addstr(posy+2, posx, 4 * chr(0x0020) + 1 * chr(0x2588) + 5 * chr(0x0020) + 1 * chr(0x2588) + 4 * chr(0x0020))
# 		stdscr.addstr(posy+3, posx, 5 * chr(0x0020) + 5 * chr(0x2588) + 5 * chr(0x0020))
# 		stdscr.addstr(posy+4, posx, 2 * chr(0x0020) + 11 * chr(0x2588) + 2 * chr(0x0020))
# 		stdscr.addstr(posy+5, posx, 1 * chr(0x0020) + 6 * (chr(0x0020) + chr(0x2588)) + 2 * chr(0x0020))
# 		stdscr.addstr(posy+6, posx, 1 * chr(0x0020) + 6 * (chr(0x0020) + chr(0x2588)) + 2 * chr(0x0020))
# 		stdscr.addstr(posy+7, posx, 3 * chr(0x0020) + 9 * chr(0x2588) + 3 * chr(0x0020))
# 		stdscr.addstr(posy+8, posx, 2 * chr(0x0020) + 1 * chr(0x2588) + 9 * chr(0x0020) + 1 * chr(0x2588) + 2 * chr(0x0020))
# 		stdscr.addstr(posy+9, posx, 1 * chr(0x0020) + 1 * chr(0x2588) + 11 * chr(0x0020) + 1 * chr(0x2588) + 1 * chr(0x0020))
# 		stdscr.addstr(posy+10, posx, 15 * chr(0x0020))

# 	def position2(self, stdscr, posy, posx):
# 		stdscr.addstr(posy+0, posx, 15 * chr(0x0020))
# 		stdscr.addstr(posy+1, posx, 7 * chr(0x0020) + 1 * chr(0x2588) + 7 * chr(0x0020))
# 		stdscr.addstr(posy+2, posx, 7 * chr(0x0020) + 1 * chr(0x2588) + 7 * chr(0x0020))
# 		stdscr.addstr(posy+3, posx, 5 * chr(0x0020) + 6 * chr(0x2588) + 4 * chr(0x0020))
# 		stdscr.addstr(posy+4, posx, 2 * chr(0x0020) + 11 * chr(0x2588) + 2 * chr(0x0020))
# 		stdscr.addstr(posy+5, posx, 1 * chr(0x0020) + 6 * (chr(0x2588) + chr(0x0020)) + 1 * chr(0x2588) + 1 * chr(0x0020))
# 		stdscr.addstr(posy+6, posx, 1 * chr(0x0020) + 6 * (chr(0x2588) + chr(0x0020)) + 1 * chr(0x2588) + 1 * chr(0x0020))
# 		stdscr.addstr(posy+7, posx, 2 * chr(0x0020) + 11 * chr(0x2588) + 2 * chr(0x0020))
# 		stdscr.addstr(posy+8, posx, 7 * chr(0x0020) + 1 * chr(0x2588) + 7 * chr(0x0020))
# 		stdscr.addstr(posy+9, posx, 7 * chr(0x0020) + 1 * chr(0x2588) + 7 * chr(0x0020))
# 		stdscr.addstr(posy+10, posx, 15 * chr(0x0020))


# class Movimento(object):
# 	def __init__(self, stdscr):
# 		self.y = 10
# 		self.x = 10
# 		for i in range(0, 100):
# 			a = random.randint(-1, 1)
# 			b = random.randint(-1, 1)
# 			for j in range(0, 10):
# 				self.y += a
# 				self.x += b
# 				try:
# 					Satelite(stdscr, self.y, self.x)
# 				except:
# 					stdscr.clear()
# 					self.y = 10
# 					self.x = 10
# 					Satelite(stdscr, self.y, self.x)


def inkey(stdscr):
	fim = ''
	while fim != 'e':
		fim = stdscr.getkey()
		stdscr.addch(10, 10, fim)


def main(stdscr):
	# disable blinking cursor
	curses.curs_set(False)
	# clear screen
	stdscr.clear()

	# main code
	inkey(stdscr)

	# end main code
	stdscr.getkey()


if __name__ == '__main__':
	wrapper(main)