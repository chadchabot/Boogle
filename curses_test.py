import curses

stdscr = curses.initscr()
curses.noecho()
curses.curs_set(0)
stdscr.keypad(1)

WL_H = 10
WL_W = 16
WL_X_ORG = 16
WL_Y_ORG = 0

wordlist_win = curses.newwin(WL_H, WL_W, WL_Y_ORG, WL_X_ORG)
wordlist_win.box()

GB_H = 6
GB_W = 16
GB_X_ORG = 0
GB_Y_ORG = 0
gameboard_win = curses.newwin(GB_H, GB_W, GB_Y_ORG, GB_X_ORG)
gameboard_win.box()

TE_H = 4
TE_W = 16
TE_X_ORG = 0
TE_Y_ORG = 6 
textentry_win = curses.newwin(TE_H, TE_W, TE_Y_ORG, TE_X_ORG)
textentry_win.box()

gameboard_win.addstr(4,1,"gameboard?", curses.A_REVERSE)
wordlist_win.addstr(2,1,"another word!")
textentry_win.addstr(1,2,"enter text")

gameboard_win.refresh()
wordlist_win.refresh()
textentry_win.refresh()


stdscr.refresh()
textentry_win.getch()
curses.endwin()
