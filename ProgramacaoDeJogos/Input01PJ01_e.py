# INPUT
# Programacao de Jogos
#
# Inseto

# Implementacao em Python by RN
# com uso da biblioteca CURSES para 
# manipulacao da janela de texto (terminal)

# resource: https://docs.python.org/3.4/howto/curses.html#curses-howto
# resource: https://docs.python.org/3.4/library/curses.html?highlight=curses#module-curses

# v1.1
# 20150602

import time, curses
from curses import wrapper


def drawinsect(stdscr, posy, posx):
	# draws insect
	stdscr.addstr(posy, posx, ' )))')
	stdscr.addstr(posy+1, posx, ' OOO<')
	stdscr.addstr(posy+2, posx, ' )))')
	stdscr.refresh()
	time.sleep(0.2)
	stdscr.addstr(posy, posx, ' (((')
	stdscr.addstr(posy+1, posx, ' OOO<')
	stdscr.addstr(posy+2, posx, ' (((')
	stdscr.refresh()
	time.sleep(0.2)


def main(stdscr):
	# disable blinking cursor
	curses.curs_set(False)
	# clear screen
	stdscr.clear()

	# main code
	for i in range(0, 74):
		drawinsect(stdscr, 10, i)

	# end main code
	stdscr.getkey()

wrapper(main)