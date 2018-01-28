#10-1-2018
#165p
#not in use

from util.graphics import *

#?
def  drawBar(1,2,3):
    bar.setFill("green")
    bar.setWidth(2)
    bar.draw(win)


def main():


    print("<<<10 year investment>>>")
    #copied from 6-3
    #print("/n10 year investment")
    pri = eval(input("initial principal:"))
    apr = eval(input("anualized interest rate:"))

    win = GraphWin("Invest growth chart", 320.240)
    win.setBackground("white")
    win.setCoords(-1.75, -200, 11.5, 10400)
    Text(Point(-1, 0), ' 0.0K').draw(win)
    Text(Point(-1, 2500), ' 2.5K').draw(win)
    Text(Point(-1, 5000), ' 5.0K').draw(win)
    Text(Point(-1, 7500), ' 7.5K').draw(win)
    Text(Point(-1, 10000), ' 10.0K').draw(win)

    #
    drawBar(win,0,pri)


    bar = Rectangle(Point(0, 0), Point(1, pri))
    bar.setFill("green")
    bar.setWidth(2)
    bar.draw(win)

    for year in range(1, 11):
        pri = pri * (1 + apr)
       drawBar(win,year,pri)
    input("push enter")
    win.close()


main()
