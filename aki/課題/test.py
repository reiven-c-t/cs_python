from datetime import datetime, timedelta
from random import choice, uniform
import codecs


def generate_csv(length, colHeaderList):
    result = ""
    result += ", ".join(colHeaderList)
    result += "\n"

    date = datetime.now()
    day_list = ["日", "月", "火", "水", "木", "金", "土"]
    count = 0
    for i in range(length):
        col = []
        for item in colHeaderList:
            if item == "id":
                col.append(count)
            if item == "date":
                col.append(date.strftime("%Y-%m-%d"))
                date += timedelta(days=1)
            elif item == "day":
                col.append(day_list[count % 7])
            elif item == "weather":
                col.append(choice(["晴", "雲", "雨", "雷雨"]))
            elif item == "condition":
                col.append(choice(["good", "bad", "soso", "awesome", "tired", "exhausted"]))
            elif item == "climate":
                col.append("%.3f" % uniform(-10, 30))
            else:  # ミスってるけどまあいいや
                dummyList = [
                    ["りんご", "ぶどう", "なし", "オレンジ", "みかん", "パイナッポー", "ペン"],
                    ["ハンバーガー", "牛丼", "天丼", "とん丼", "トンカツ", "ししゃも"],
                    ["スキー", "テニス", "サッカー", "バレーボール", "バスケ", "野球", "ラクロス", "ラグビー"],
                    ["腹筋", "背筋", "ダンベルカール", "アームカール", "デッドリフト", "ラットプルダウン", "プルダウン"],
                    ["温泉", "登山", "海水浴", "ボートのり", "美術館巡り", "カフェ巡り"]
                ]
                col.append(choice(choice(dummyList)))
        result += ", ".join(col) + "\n"
        count += 1
    return result


if __name__ == '__main__':
    csv_header = ["date", "day", "weather", "condition", "climate", "random1", "random2", "random3"]
    csv_raw_data = generate_csv(10000,
                                ["date", "day", "wather", "condition", "climate", "random1", "random2", "random3"])

    csv_raw_data = csv_raw_data.split("\n")

    csv_first = "\n".join(csv_raw_data[0:6000])
    csv_last = [", ".join(csv_header)]
    for row in csv_raw_data[5000:]:
        csv_last.append(row)
    csv_last = "\n".join(csv_last)

    with codecs.open("large_test_1.csv", "w", "shift-jis") as file:
        file.write(csv_first)
    with codecs.open("large_test_2.csv", "w", "shift-jis") as file:
        file.write(csv_last)
"""
課題ラフ
- 共通演算(day一致検知から配列生成=>join()
- 差演算(データ - 共通部分のday不一致から配列生成=>join()
- 和集合演算(データ1の差演算集合+データ2)
- 選択演算(test_1にて気分等号X,気温Y以上,random_3食事等号条件Z)の行を選択する関数設計からの
    気分bad,気温0度以上、トンカツを食べた日の行数を出力
- 射影演算(csvの列の1部のみを抽出する関数を作成(headerは与える))その関数を使って選択演算での上記の際のdateとweatherのみのcsvを作成)

気分はbad,気温0度以上でトンカツを食べた日をlarge_test_1.csvの個数(22件)

"""
