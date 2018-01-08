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
import csv
import codecs

# large csv(have more than 5000 data in each csv)
# csv_1 = codecs.open("large1_shift-jis.csv", "r", "shift-jis")

# small csv
csv_1 = codecs.open("small1_shift-jis.csv", "r", "shift-jis")

csv_1 = csv_1
csv_1 = csv.DictReader(csv_1)


# 選択演算
def select(csv, weather, condition, climate):
    result = []
    for row in csv:
        pass
    return result
"aaa"


# 射影演算
def project(csv, header_list):
    result = []
    result.append(header_list)
    for row in csv:
        pass
    return result


if __name__ == '__main__':
    selected = select(csv_1, "雨", "soso", 0)
    print(project(selected, ["date", "weather", "condition", "random1"]))
