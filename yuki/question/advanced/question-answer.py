"""
すること:
1. testの0~9のフォルダの中から適当に1個csvを選ぶ
2. 選んだやつをadvancedフォルダに移動 or コピー

"""
import codecs
import os


def csv_reader(csv_file):
    # simply load csv file and split it with return
    # or you could write your own loader.
    return codecs.open(csv_file, "r", "utf-8").read().split("\n")


# 共通部分演算
def intersect(csv1, csv2):
    return list(set(csv1).intersection(set(csv2)))  # should sort and remove header but enough


# 和集合演算
def union(csv1, csv2):
    return list(set(csv1).union(set(csv2)))  # should sort and fix header position but enough.


def jsc(csv1, csv2):
    return len(intersect(csv1, csv2)) / len(union(csv1, csv2))


def classifier(csv):
    max_jsc = 0
    current_label = 0
    for label in range(10):
        top_dir_path = "train" +os.sep +"%d" % label
        for root, dirs, files in os.walk(top_dir_path): # TODO: Mightbe
            # if you need, comment out below and check what the os.walk() do.
            # print('-' * 10)
            # print('root:{}'.format(root))
            # print('dirs:{}'.format(dirs))
            # print('files:{}'.format(files))
            for file in files:
                temp_jsc = jsc(csv, csv_reader(top_dir_path + os.sep + file))
                if max_jsc <= temp_jsc:
                    max_jsc = temp_jsc
                    current_label = label
    return current_label


if __name__ == '__main__':
    # copy one csv from test/ folder and put it in advanced/ and rename "test_num.csv"
    # example copy from test/1
    csv_1 = csv_reader("test_num.csv")
    result = classifier(csv_1)
    print(result)
