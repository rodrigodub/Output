from curses import wrapper

def main(stdscr):
    # clear screen
    stdscr.clear()

    # raises zerodivisionerror
    for i in range(1, 11):
        #v = i-10
        v = i
        stdscr.addstr(i, 0, '10 divided by {} is {}'.format(v, 10/v))

    stdscr.refresh()
    stdscr.getkey()

wrapper(main)
