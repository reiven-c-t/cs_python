#9-1-2018

import math
#from graphics import *
from util.graphics import *

#def1
def square(x):
    return x*x

#def2
def distance(p1, p2):
    dist = math.sqrt(square(p2.getX()-p1.getX())+square(p2.getY()-p1.getY()))
    return dist

#def3
#みつからなかったんでぼくのとこでは、すんません、たか君のところのトライアングルからコードもらいました
#（こういうのってあんまりしないほうがいいんか？ ）

def main():
    win = GraphWin("Draw a Triangle")
    win.setCoords(0,0,10,10)
    message = Text(Point(5,0.5),"Click on three points")
    message.draw(win)

    p1= win.getMouse()
    p1.draw(win)
    p2=win.getMouse()
    p2.draw(win)
    p3=win.getMouse()
    p3.draw(win)

    triangle = Polygon(p1,p2,p3)
    triangle.setFill("peachpuff")
    triangle.setOutline("cyan")
    triangle.draw(win)

    #message.setText("Click anywhere to quit.")
    #win.getMouse()



