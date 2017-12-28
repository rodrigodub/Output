# INPUT
# Programacao de Jogos

# Implementacao em Python by RN
# com uso da biblioteca CURSES para 
# manipulacao da janela de texto (terminal)

# resource: https://docs.python.org/3.4/howto/curses.html#curses-howto
# resource: https://docs.python.org/3.4/library/curses.html?highlight=curses#module-curses

from curses import wrapper

def main(stdscr):
    # clear screen
    stdscr.clear()

    # main code
    stdscr.addstr(5, 5, ')))')
    stdscr.addstr(6, 5, 'OOO<')
    stdscr.addstr(7, 5, ')))')
    stdscr.addstr(10, 0, '')

    # end main code

    stdscr.refresh()
    stdscr.getkey()

wrapper(main)