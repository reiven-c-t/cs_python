"""
すること:
1. testの0~9のフォルダの中から適当に1個csvを選ぶ
2. 選んだやつをadvancedフォルダに移動 or コピー
"""
import codecs
import os


# write your own csv_reader function that load csv, or use following function. Anyway result is same.
def csv_reader(csv_file):
    # simply load csv file and split it with return
    # or you could write your own loader.
    return codecs.open(csv_file, "r", "utf-8").read().split("\n")


# 共通部分演算
# use your own intersect() or use following function. Anyway, result is same.
def intersect(csv1, csv2):
    return list(set(csv1).intersection(set(csv2)))  # should sort and remove header but enough


# 和集合演算
# use your own union() or use following function. Anyway, result is same.
def union(csv1, csv2):
    return list(set(csv1).union(set(csv2)))  # should sort and fix header position but enough.


def jsc(csv1, csv2):
    # write your own jsc()
    #
    # But again, what you need to do is
    # divide amount of intersection component of csv1 and csv2
    # and amount of union component of csv1 and csv2
    #
    # Then, you know what to do?
    pass


def classifier(csv):
    for label in range(10):  # folder's label.
        top_dir_path = "train" + os.sep + "%d" % label
        for root, dirs, files in os.walk(top_dir_path):  # TODO: Might be OK. But I could not check on Windows.
            # if you need, remove comment below and check what the os.walk() do.
            # or see the document.
            #
            # print('-' * 10)
            # print('root:{}'.format(root))
            # print('dirs:{}'.format(dirs))
            # print('files:{}'.format(files))
            for file in files:
                # csv_path is the path for each csv file path in test/ folder.
                csv_path = top_dir_path + os.sep + file


if __name__ == '__main__':
    # copy one csv from test/ folder and put it in advanced/ and rename "test_num.csv"
    # example copy from test/1
    csv_1 = csv_reader("test_num.csv")
    result = classifier(csv_1)
    print(result)
