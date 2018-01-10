#9-1-2018

#10-1-2018 year定義されてないおわた


from util.graphics import *
#from graphics import *
#↑、ようちぇく

def drawBar(window,year,height):
    #
    #bar=
    bar = Rectangle(Point(year, 0), Point(year+1, height))
    bar.setFill("green")
    bar.setWidth(2)
    bar.draw(window)



def main():
    print("<<<10 year interest program>>>")
    pri = eval(input("initial principal:"))
    apr = eval(input("annualized interest rate:"))

    #
    win = GraphWin("Invest growth chart", 320.240)
    win.setBackground("white")
    win.setCoords(-1.75, -200, 11.5, 10400)

    #
    Text(Point(-1, 0), ' 0.0K').draw(win)
    Text(Point(-1, 2500), ' 2.5K').draw(win)
    Text(Point(-1, 5000), ' 5.0K').draw(win)
    Text(Point(-1, 7500), ' 7.5K').draw(win)
    Text(Point(-1, 10000), ' 10.0K').draw(win)

    drawBar(win, year. pri)
    for year in range(1,11):
        pri=pri*(1+apr)
        drawBar(win,year,pri)

    input("enter to quit")
    win.close()

main()


#####################################
#6-1

from util.graphics import *

def main():
    print("/n10 year investment")
    pri = eval(input("initial principal:"))
    apr = eval(input("anualized interest rate:"))

    win=GraphWin("Invest growth chart",320.240)
    win.setBackground("white")
    win.setCoords(-1.75,-200,11.5,10400)
    Text(Point(-1,0 ), ' 0.0K').draw(win)
    Text(Point(-1, 2500), ' 2.5K').draw(win)
    Text(Point(-1, 5000), ' 5.0K').draw(win)
    Text(Point(-1, 7500), ' 7.5K').draw(win)
    Text(Point(-1, 10000), ' 10.0K').draw(win)

    bar=Rectangle(Point(0,0),Point(1,pri))
    bar.setFill("green")
    bar.setWidth(2)
    bar.draw(win)

    for year in range(1,11):
        pri=pri*(1+apr)
        bar = Rectangle(Point(year, 0), Point(year+1, pri))
        bar.setFill("green")
        bar.setWidth(2)
        bar.draw(win)
    input("push enter")
    win.close()

main()