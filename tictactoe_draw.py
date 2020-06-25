import stddraw
import math
import color

def setScales():
    stddraw.setXscale(-10.0,10.0)
    stddraw.setYscale(-10.0,10.0)

def clear():
    stddraw.clear()

def show(milliseconds = -1.0):
    if milliseconds < 0:
        stddraw.show()
    else:
        stddraw.show(milliseconds)

def drawCanvas():
    stddraw.setPenColor(stddraw.BLACK)
    stddraw.setPenRadius(0.5)
    stddraw.line(-3.33,-10.0,-3.33,10.0)
    stddraw.line(3.33,-10.0,3.33,10.0)
    stddraw.line(-10.0,-3.33,10.0,-3.33)
    stddraw.line(-10.0,3.33,10.0,3.33)

def drawX(x,y):
    stddraw.setPenRadius(0.1)
    stddraw.setPenColor(stddraw.BLACK)
    stddraw.line(x+2.5,y+2.5,x-2.5,y-2.5)
    stddraw.line(x-2.5,y+2.5,x+2.5,y-2.5)

def drawO(x,y):
    stddraw.setPenColor(stddraw.BLACK)
    stddraw.setPenRadius(0.01)
    stddraw.circle(x,y,2.5)

def win(winner,turn):
    stddraw.clear()
    stddraw.setFontSize(30)
    if winner == 'X' or winner == 'O':
        stddraw.text(0.0,0.0,"'"+ winner + "'" + " player wins")
    if turn >= 9 and winner != 'X' and winner != 'O':
        stddraw.text(0.0,0.0," It's a tie!")

def turnStatement(turn):
    stddraw.setFontSize(20)
    if turn % 2 == 0:
        stddraw.setPenColor(stddraw.WHITE)
        stddraw.text(0.0,0.0,"It's Player Two's Turn")
        stddraw.setPenColor(stddraw.RED)
        stddraw.text(0.0,0.0,"It's Player One's Turn")
    else:
        stddraw.setPenColor(stddraw.WHITE)
        stddraw.text(0.0,0.0,"It's Player One's Turn")
        stddraw.setPenColor(stddraw.RED)
        stddraw.text(0.0,0.0,"It's Player Two's Turn")
