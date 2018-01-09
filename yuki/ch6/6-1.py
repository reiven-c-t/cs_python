##import graphics.py
from util.graphics import *


def main():
    print("/n10 year investment")
    principal = eval(input("initial principal:"))
    apr = eval(input("anualized interest rate:"))

    win=GraphWin("Invest growth chart",320.240)
    win.setBackground("white")
    win.setCoords(-1.75,-200,11.5,10400)
    Text(Point(-1,0 ), ' 0.0K').draw(win)
    Text(Point(-1, 2500), ' 2.5K').draw(win)
    Text(Point(-1, 5000), ' 5.0K').draw(win)
    Text(Point(-1, 7500), ' 7.5K').draw(win)
    Text(Point(-1, 10000), ' 10.0K').draw(win)

    bar=Rectangle(Point(0,0),Point(1,principal))
    bar.setFill("green")
    bar.setWidth(2)
    bar.draw(win)

    for year in range(1,11):
        principal=principal*(1+apr)
        bar = Rectangle(Point(year, 0), Point(year+1, principal))
        bar.setFill("green")
        bar.setWidth(2)
        bar.draw(win)
    input("push enter")
    win.close()

main()
