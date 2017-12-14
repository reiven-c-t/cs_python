import codecs

# large csv(have more than 5000 data in each csv)
# csv_1 = codecs.open("large1_shift-jis.csv", "r", "shift-jis")
# csv_2 = codecs.open("large2_shift-jis.csv", "r", "shift-jis")

# small csv
csv_1 = codecs.open("small1_shift-jis.csv", "r", "shift-jis")
csv_2 = codecs.open("small2_shift-jis.csv", "r", "shift-jis")

csv_1 = csv_1.read().split("\n")
csv_2 = csv_2.read().split("\n")


# 差演算
def difference(csv1, csv2):
    return list(set(set(csv1) - set(csv2)))  # should sort and add header but enough.


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
