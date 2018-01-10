#10-1-2018
#166p

from util.graphics import *

def cre():
    #copied from 6.3
    ###############
    window = GraphWin("Invest growth chart", 320.240)
    window.setBackground("white")
    window.setCoords(-1.75, -200, 11.5, 10400)

    #
    Text(Point(-1, 0), ' 0.0K').draw(window)
    Text(Point(-1, 2500), ' 2.5K').draw(window)
    Text(Point(-1, 5000), ' 5.0K').draw(window)
    Text(Point(-1, 7500), ' 7.5K.').draw(window)
    Text(Point(-1, 10000), ' 10.0K').draw(window)
    ###############
    return window

def drawBar(window,year, height):
    bar = Rectangle(Point(year, 0), Point(year + 1, height))
    bar.setFill("green")
    bar.setWidth(2)
    bar.draw(window)

def main():
    print("<<<10 year interest program>>>")
    pri = eval(input("initial principal:"))
    apr = eval(input("annualized interest rate:"))

    win=cre()
    drawBar(win,0,pri)
    for year in range(1,11):
        pri=pri*(1+apr)
        drawBar(win, year, pri)

    input("enter to quit")
    win.close()

main()
