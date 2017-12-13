from datetime import datetime, timedelta
from random import choice, uniform, seed
import codecs

seed(1)


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
            elif item.find("random") != -1:  # ミスってるけどまあいいや
                dummyList = [
                    ["りんご", "ぶどう", "なし", "オレンジ", "みかん", "パイナッポー", "ペン"],
                    ["ハンバーガー", "牛丼", "天丼", "とん丼", "トンカツ", "ししゃも"],
                    ["スキー", "テニス", "サッカー", "バレーボール", "バスケ", "野球", "ラクロス", "ラグビー"],
                    ["腹筋", "背筋", "ダンベルカール", "アームカール", "デッドリフト", "ラットプルダウン", "プルダウン"],
                    ["温泉", "登山", "海水浴", "ボートのり", "美術館巡り", "カフェ巡り"]
                ]
                col.append(choice(dummyList[int(item.replace("random", ""))]))
        result += ", ".join(col) + "\n"
        count += 1
    return result


if __name__ == '__main__':
    csv_header = ["date", "day", "weather", "condition", "climate", "random1", "random2", "random3"]
    csv_raw_data = generate_csv(10000,
                                ["date", "day", "weather", "condition", "climate", "random1", "random2", "random3"])

    csv_raw_data = csv_raw_data.split("\n")

    csv_first = "\n".join(csv_raw_data[0:6000])
    csv_last = [", ".join(csv_header)]
    for row in csv_raw_data[5000:]:
        csv_last.append(row)
    csv_last = "\n".join(csv_last)

    with codecs.open("large1_shift-jis.csv", "w", "shift-jis") as file:
        file.write(csv_first)
        print("success")
    with codecs.open("large2_shift-jis.csv", "w", "shift-jis") as file:
        file.write(csv_last)

    with codecs.open("large_test_1_utf-8.csv", "w", "utf-8") as file:
        file.write(csv_first)
        print("success")
    with codecs.open("large_test_2_utf-8.csv", "w", "utf-8") as file:
        file.write(csv_last)


    # small data
    csv_header = ["date", "day", "weather", "condition", "climate", "random1", "random2", "random3"]
    csv_raw_data = generate_csv(20,
                                ["date", "day", "weather", "condition", "climate", "random1", "random2", "random3"])

    csv_raw_data = csv_raw_data.split("\n")

    csv_first = "\n".join(csv_raw_data[0:12])
    csv_last = [", ".join(csv_header)]
    for row in csv_raw_data[10:]:
        csv_last.append(row)
    csv_last = "\n".join(csv_last)

    with codecs.open("small1_shift-jis.csv", "w", "shift-jis") as file:
        file.write(csv_first)
        print("success")
    with codecs.open("small2_shift-jis.csv", "w", "shift-jis") as file:
        file.write(csv_last)

    with codecs.open("small_test_1_utf-8.csv", "w", "utf-8") as file:
        file.write(csv_first)
        print("success")
    with codecs.open("small_test_2_utf-8.csv", "w", "utf-8") as file:
        file.write(csv_last)

