from util.graphics import *

def main():
    win=GraphWin("Celsius Converter",400,300)
    win.setCoords(0,0,3,4)

    Text(Point(1,3),"Celsius Temperature:").draw(win)
    Text(Point(1,1),"Fahrenheit Temperature:").draw(win)
    input= Entry(Point(2,3),5)
    input.setText("0.0")
    input.draw(win)
    output=Text(Point(2,1),"")
    output.draw(win)
    button=Text(Point(1.5,2),"Convert it")
    button.draw(win)
    Rectangle(Point(1,1.5),Point(2,2.5)).draw(win)

    win.getMouse()

    celsius=eval(input.getText())
    fahrenheit=9/5*celsius+32

    output.setText(fahrenheit)
    button.setText("Quit")

    win.getMouse()
    win.close()

main()