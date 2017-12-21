#
#
#YUKI_YAGI
#3-Dec-2017

from util.graphics import *

win=GraphWin("tic-tac-toe")
win.setCoords(0.0,0.0,3.0,3.0)
Line(Point(1,0),Point(1,3)).draw(win)
Line(Point(2,0),Point(2,3)).draw(win)
Line(Point(0,1),Point(3,1)).draw(win)
Line(Point(0,2),Point(3,2)).draw(win)

win=GraphWin("Investment Growth Chart", 320, 240)
win.setCoords(0.0,0.0,10.0,10000.0)

#bar=Rectangle(Point(year,0),Point(yeat+1,principal))

win=GraphWin("Investment Growth Chart", 320, 240)
win.setCoords(-1.75,-200,11.5,10400.0)


def main():
    win=GraphWin("Click")
    for i in range(10):
        p=win.getMouse()
        print("the point you touch:", p.getX(), p.getY())
main()


def main():
    win=GraphWin("Draw triangle")
    win.setCoords(0.0, 0.0, 10.0, 10.0)
    message=Text(Point(5,0.5),"Click on three point")
    message.draw(win)
    p1=win.getMouse()
    p1.draw(win)
    p2=win.getMouse()
    p2.draw(win)
    p3=win.getMouse()
    p3.draw(win)
    triangle=Polygon(p1,p2,p3)
    triangle.setFill("peachpuff")
    triangle.setOutline("cyan")
    triangle.draw(win)
    message.setText("Click anywhere")
    win.getMouse()
main()


def main471():
    for i in range(10):
        p=win.getMouse()
        print("the point you touch:", p.getX(), p.getY())
main()

def main472():
    win=GraphWin("Celsius Convert", 300, 400)
    win.setCoords(0.0,0.0,3.0,4.0)
    Text(Point(1,1),"  Celsius Temperature:").draw(win)
    Text(Point(1,3),"Fahrenhit Temperature:").draw(win)
    input=Entry(Point(2,3),5)
    input.setText("0.0")
    input.draw(win)
    output=Text(Point(2,1),"")
    output.draw(win)
    button=Text(Point(1.5,2.0),"Convert It")
    button.draw(win)
    Rectangle(Point(1,1.5),Point(2,2.5)).draw(win)
    win.getMouse()
    c=eval(input.getText())
    f=9.0/5.0*c+32
    output.setText(f)
    button.setText("quit")
    win.getMouse()
    win.close()
main()

