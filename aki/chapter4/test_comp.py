"""
aki/chapter4/test.pyとコードは同じです。
説明はaki/chapter4/test.pyのコメントを読んで。

ここからは具体的な使い方。
下の通り、ぶっちゃけ丸ごとコピってくれば良いです。
以上。
"""

# from graphics import *
from  util.graphics import *
from time import sleep


# code for checking graphics is working

def main():
    print("This program ")

    principal = eval(input("Enter the inital principal: "))
    apr = eval(input("Enter apr:"))

    win = GraphWin("Investment Growth Chart", 320, 240)
    win.setBackground("white")
    Text(Point(20, 230), "0.0K").draw(win)
    Text(Point(20, 230), "2.5K").draw(win)
    Text(Point(20, 230), "5.0K").draw(win)
    Text(Point(20, 200), "7.5K").draw(win)
    Text(Point(20, 230), "10.0K").draw(win)

    height = principal * 0.02
    bar = Rectangle(Point(40, 230), Point(65, 230 - height))
    bar.setFill("green")
    bar.setWidth(2)
    bar.draw(win)

    for year in range(1, 11):
        principal = principal * (1 + apr)
        x11 = year * 25 + 40
        height = principal * 0.02
        bar = Rectangle(Point(x11, 230), Point(x11 + 25, 230 - height))
        bar.setFill('green')
        bar.setWidth(2)
        bar.draw(win)

    input("Press enter to quit")
    win.close()


if __name__ == '__main__':
    main()

sleep(3)
