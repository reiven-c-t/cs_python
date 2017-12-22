"""
aki/chapter4/test.pyとコードは同じです。
説明はaki/chapter4/test.pyのコメントを読んで。

ここからは具体的な使い方。
下の通り、ぶっちゃけ丸ごとコピってくれば良いです。
以上。
"""

# 1st
import util.graphics as graphics
from time import sleep
# code for checking graphics is working
win = graphics.GraphWin()
sleep(3)# windowを描画して3秒待機(sleep)してその後windowをclose
win.close()

# 2cd
# from graphics import *
from util.graphics import *
from time import sleep
# code for checking graphics is working
win = GraphWin()
p=Point(50, 60)
p.getX()

#win= GraphWin()
#p.draw(win)
#p2=Point(140,100)
#p2.draw(win)
#p.getY()

# ten sen
win=GraphWin('Shapes')
center=Point(100,100)
circ=Circle(center,30)
circ.setFill('red')
circ.draw(win)
label=Text(center, "Red Circle")
label.draw(win)
rect=Rectangle(Point(30,30),Point(70,70))
rect.draw(win)
line=Line(Point(20,30),Point(185,165))
line.draw(win)

p=Point(50,50)
p.draw(win)
p.move(0,10)

#73p
leftEye=Circle(Point(80,50),5)
leftEye.setFill('yellow')
leftEye.setOutline('red')
rightEye=leftEye
rightEye.move(20,0)

leftEye=Circle(Point(80,50),5)
leftEye.setFill('yellow')
leftEye.setOutline('red')
rightEye=Circle(Point(100,50),5)
rightEye.setFill('yellow')
rightEye.setOutline('red')









sleep(10)# windowを描画して3秒待機(sleep)してその後windowをclose
win.close()