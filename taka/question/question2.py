"""
課題2:

csv_1とcsv_2について
Question2.pdfの通りの選択演算,射影演算の関数を定義せよ

# 選択演算

def select(csv, weather, condition, climate)
を定義せよ。

# 射影演算

def project(csv, header_list)
を定義せよ。

また、その関数を用いてlarge csvで2つの演算を試せ。
また、selectの出力結果の行数を調べよ。
ついでに、select後にdate, weather, condition, random1でprojectした
csvを作成せよ。

"""
import codecs

# large csv(have more than 5000 data in each csv)
# csv_1 = codecs.open("large1_shift-jis.csv", "r", "shift-jis")

# small csv
csv_1 = codecs.open("small1_shift-jis.csv", "r", "shift-jis")

csv_header = ["date", "day", "weather", "condition", "climate", "random1", "random2", "random3"]
csv_1 = csv_1.read()

print("CSV1: \n", csv_1)


# 選択演算
def select(csv, weather, condition, climate):
    pass


# 射影演算
def project(csv, header_list):
    pass  # この行を消して書き始めてね



if __name__ == '__main__':
    pass
