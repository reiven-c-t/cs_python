# import util.graphics as graphics
from util.graphics import *
from time import sleep


win = GraphWin('Shapes')
center = Point(100,100)
circle= Circle(center,30)
circle.setFill('red')
circle.draw(win)
lable=Text(center,"Red Circle")
lable.draw(win)
rect=Rectangle(Point(30,30),Point(70,70))
rect.draw(win)
line=Line(Point(20,30),Point(180,165))
line.draw(win)
oval=Oval(Point(20,150),Point(180,199))
oval.draw(win)
p=Point(50,50)
p.draw(win)
sleep(3)
p.move(10,0)
sleep(3)