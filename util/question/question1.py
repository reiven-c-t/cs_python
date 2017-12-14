"""
課題1:

csv_1とcsv_2について
次のような差演算, 共通演算, 和演算の関数を定義せよ

# 差演算
def difference(csv1, csv2):

# 共通部分演算
def intersect(csv1, csv2):


# 和演算
def union(csv1, csv2):

また、その関数を用いてlarge csvで3つの演算を試せ。
また、試した結果、それぞれの演算で生成されるcsvの行数を述べよ。
"""
import codecs

# large csv(have more than 5000 data in each csv)
# csv_1 = codecs.open("large1_shift-jis.csv", "r", "shift-jis")
# csv_2 = codecs.open("large2_shift-jis.csv", "r", "shift-jis")

# small csv
csv_1 = codecs.open("small1_shift-jis.csv", "r", "shift-jis")
csv_2 = codecs.open("small2_shift-jis.csv", "r", "shift-jis")

csv_1 = csv_1.read()
csv_2 = csv_2.read()

print("CSV1: \n", csv_1)
print("CSV2: \n", csv_2)


# 差演算
def difference(csv1, csv2):
    pass  # この行を消して書き始めてね


# 共通部分演算
def intersect(csv1, csv2):
    pass  # この行を消以下略


# 和集合演算
def union(csv1, csv2):
    pass  # この行以下略

if __name__ == '__main__':
    print(difference(csv_1, csv_2))
    print(intersect(csv_1, csv_2))
    print(union(csv_1, csv_2))
