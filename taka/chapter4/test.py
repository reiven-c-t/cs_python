"""
aki/chapter4/test.pyとコードは同じです。
説明はaki/chapter4/test.pyのコメントを読んで。

ここからは具体的な使い方。
下の通り、ぶっちゃけ丸ごとコピってくれば良いです。
以上。
"""
# 以下コピー
import sys, os


dir_path = os.path.dirname(os.path.realpath(__file__))
sep = os.sep
split_length = 0
paths = str(dir_path).split(sep)
for dir_path in paths:
    if dir_path == "cs_python":
        break
    split_length += 1

util_path = os.path.join("/", *paths[0: split_length + 1], "util")

sys.path.append(util_path)
# 以上コピー

# from graphics import *
import graphics
from time import sleep
# code for checking graphics is working
win = graphics.GraphWin()
sleep(3)# windowを描画して3秒待機(sleep)してその後windowをclose
win.close()