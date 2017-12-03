"""
多分必要ないけど、
Win/Mac/Linux+その他いかなるOSでも
cs_pythonフォルダ以下なら
どこからでもutilフォルダ内のモジュールをDLできるようにするためのゴタゴタ

最終的に
`from graphics import *`
はcs_python/util/フォルダの中にあるgraphics.pyを読み込んでいる。

以下余談:
おそらくPyCharmはcs_pythonをsys.pathに読み込んでいるので、
そこから辿って、
from util.grahics import *
で問題ないとは思うけど、保険としてsys.pathにutilフォルダを突っ込む。

おそらくここまでよんで,sys.pathってなに?ってなってると思うので、
それについて少しだけ補足。
説明しよう！sys.pathとは、pythonのプログラムを実行する時に、
pythonがあらかじめ基本的なモジュール(e.g. math)をimport mathだけでimportできるように
mathが含まれるpythonのコアフォルダまで読み込んでくれているみたいなものである。
早い話が、コマンドプロンプトとかのPATHと同じみたいな感じ。
その読み込みフォルダ指定はsys.pathで見れます。
見たけりゃ
print(sys.path)でcheck it out.
んで、今回私がイカソースでやったのは、sys.pathにcs_python/utilフォルダを突っ込むことで、
utilフォルダ以下のpythonコードXXをimport XXだけでimportできるようにしたという話です。
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