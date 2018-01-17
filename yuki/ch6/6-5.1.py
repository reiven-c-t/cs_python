#9-1-2018
#158p

import math
#from graphics import *
from util.graphics import *

#def1
def square(x):
    return x*x

#print(square(55))

#def2
def dis(p1, p2):
    dist = math.sqrt(square(p2.getX()-p1.getX())+square(p2.getY()-p1.getY()))
    return dist

#below did not run
#print(distance(5,5)


#def3
#みつからなかったんで(ぼくのとこでは)、すんません、たか君のところのトライアングルからコードもらいました
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

#    for i in[1,2,3]:
#         print(pi)

#    print(p1)
#    print(p2)
#    print(p3)

    triangle = Polygon(p1,p2,p3)
    triangle.setFill("peachpuff")
    triangle.setOutline("cyan")
    triangle.draw(win)

    #message.setText("Click anywhere to quit.")
    #win.getMouse()

    perim=dis(p1,p2)+dis(p3,p2)+dis(p1,p3)
    message.setText("perimeter: {0:0.2f}".format(perim))

    #
    win.getMouse()
    win.close()



main()


