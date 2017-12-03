from util.graphics import *


def main472():
    win = GraphWin("Celsius Convert", 300, 400)
    win.setCoords(0.0, 0.0, 3.0, 4.0)
    Text(Point(1, 1), "  Celsius Temperature:").draw(win)
    Text(Point(1, 3), "Fahrenhit Temperature:").draw(win)
    input = Entry(Point(2, 3), 5)
    input.setText("0.0")
    input.draw(win)
    output = Text(Point(2, 1), "")
    output.draw(win)
    button = Text(Point(1.5, 2.0), "Convert It")
    button.draw(win)
    Rectangle(Point(1, 1.5), Point(2, 2.5)).draw(win)
    win.getMouse()
    c = eval(input.getText())
    f = (9.0 / 5.0) * c + 32
    output.setText(f)
    button.setText("quit")
    win.getMouse()
    win.close()


main472()
