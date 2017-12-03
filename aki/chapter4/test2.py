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
    win = GraphWin("Tic-Tac-Toe")
    win.setCoords(0.0, 0.0, 3.0, 3.0)
    Line(Point(0,1), Point(1,3)).draw(win)
    input("Press enter to quit")
    win.close()


if __name__ == '__main__':
    main()

sleep(3)
