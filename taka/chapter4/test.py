"""
aki/chapter4/test.pyとコードは同じです。
説明はaki/chapter4/test.pyのコメントを読んで。

ここからは具体的な使い方。
下の通り、ぶっちゃけ丸ごとコピってくれば良いです。
以上。
"""

# from graphics import *
import util.graphics as graphics
from time import sleep
# code for checking graphics is working
win = graphics.GraphWin()
sleep(3)# windowを描画して3秒待機(sleep)してその後windowをclose
win.close()