import sys
from Tkinter import *

import tkMessageBox
import tkFileDialog

active_game = 0

def callback():
    print "called the callback!"

def generate_board(value):
    print '\t entered generate_board - value = (%d)' % value
    if value == 0:
        print "\tnew board created"
#        active_game = 1
        return 1

    else:
        print "\tnew board not created"
#        active_game = 0
        return 0

def new_game(input):
    global active_game
    print 'entered new_game( (%d) ) -- active_game = (%d)' % (input, active_game)

    if active_game == 1:
        print "game active. end this one first"
#    if active_game == 0:
    else:
        result = generate_board(input)
        print '\t\t result = generate_board( (%d) )' % input
        print '\t\t result = (%d)' % result
        if result == 1:
            print "new game created"
            active_game = 1
        else:
            print "unable to create new game"


#def open_menu_item(filename="noFile.txt"):
def open_menu_item():
    filename = tkFileDialog.askopenfilename()
    try:
        fp = open(filename)
        print "(%s) opened" % filename
        fp.close()
        print "(%s) closed" % filename
    except:
        tkMessageBox.showerror(
            "Open file (%s) - failed" % filename,
            "Cannot open this file\n(%s)" % filename
        )

def end_game():
    global active_game
    if active_game == 1:
        print "ending game"
        active_game = 0
    else:
        print "no game to end"


window = Tk()


# create a menu
menu = Menu(window)
window.config(menu=menu)

filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New Game", command=( lambda: new_game(active_game)) )
#filemenu.add_command(label="New [1]", command=(lambda: new_game(1)) )
filemenu.add_command(label="End Game", command=end_game)
filemenu.add_command(label="Open...", command=open_menu_item)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=callback)

helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)

window.mainloop()

# rightFrame = Frame()
# leftFrame = Frame()
# 
# boardFrame = Frame()
# 
# 
# Label(rightFrame, text='text area')
# Label(leftFrame, text='left frame')
# 
# Label(boardFrame, text='game area')
# 
# newGame_btn = Button( None, text='New game' )
# newGame_btn.pack( side=LEFT )
# 
# pauseGame_btn = Button(None, text='Pause game', command=pause)
# pauseGame_btn.pack(side=RIGHT)
# 
# Label(window, text='a Tkinter label').pack(side=TOP, expand=YES, fill=BOTH)
# 
# 
# #window.title('Boogle. For Lise.')
# window.pack()
# window.mainloop()
# 

#def main():
    