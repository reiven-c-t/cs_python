#
#
#YUKI_YAGI
#3-12-2017

#75p 4.5

from util.graphics import *

def main():
    print("Hi world")
    principal=eval(input("initial principal:"))
    apr=eval(input("annualized interest rate:"))
    win = GraphWin("Investment chart, 320, 400")
    win.setBackground("blue")
    Text(Point(20, 230), "0.0k").draw(win)
    Text(Point(20,180),"2.5k").draw(win)
    Text(Point(20, 130), "5.0k").draw(win)
    Text(Point(20, 80), "7.5k").draw(win)
    Text(Point(20, 30), "10.0k").draw(win)
    height=principal*0.2
    bar=Rectangle(Point(40,230),Point(65,230-height))
    bar.setFill("blue")
    bar.setWidth(3)
    bar.draw(win)

    for year in range(1,11):
        principal=principal*(1+apr)
        x11=year*25+40
        height=principal*0.02
        bar=Rectangle(Point(x11,230),Point(x11+25,230-height))
        bar.setFill("blue")
        bar.setWidth(3)
        bar.draw(win)
    input("Press<Enter>to quit")
    win.close()
main()

