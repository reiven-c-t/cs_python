"""
すること:
1. testの0~9のフォルダの中から適当に1個csvを選ぶ
2. 選んだやつをadvancedフォルダに移動 or コピー

Jaccard Similarity Coefficientを計算

JSCとは

"""
import codecs


# small csv
csv_1 = codecs.open("small1_shift-jis.csv", "r", "shift-jis")
csv_2 = codecs.open("small2_shift-jis.csv", "r", "shift-jis")

csv_1 = csv_1.read().split("\n")
csv_2 = csv_2.read().split("\n")


# 共通部分演算
def intersect(csv1, csv2):
    return list(set(csv1).intersection(set(csv2)))  # should sort and remove header but enough


# 和集合演算
def union(csv1, csv2):
    return list(set(csv1).union(set(csv2)))  # should sort and fix header position but enough.



if __name__ == '__main__':
    print(len(difference(csv_1, csv_2)))
    print(len(intersect(csv_1, csv_2)))  # return 3 when testing small data set because it has header.
    print(len(union(csv_1, csv_2)))
