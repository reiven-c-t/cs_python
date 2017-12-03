from util.graphics import *
from time import sleep

win=GraphWin("Eye")
leftEye=Circle(Point(80,50),5)
leftEye.setFill("yellow")
leftEye.setOutline("red")
rightEye=Circle(Point(80,50),5)
leftEye.setFill("yellow")
leftEye.setOutline("red")
rightEye.move(20,0)
leftEye.draw(win)
rightEye.draw(win)