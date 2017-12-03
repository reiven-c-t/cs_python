from util.graphics import *

win=GraphWin("Tic-tac-toe")
win.setCoords(0,0,3,3)

Line(Point(1,0),Point(1,3)).draw(win)
Line(Point(2,0),Point(2,3)).draw(win)

Line(Point(0,1),Point(3,1)).draw(win)
Line(Point(0,2),Point(3,2)).draw(win)