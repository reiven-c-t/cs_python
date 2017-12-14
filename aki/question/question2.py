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
        if row["weather"].find(weather) != -1 and row["condition"].find(condition) != -1 and float(
                row["climate"]) >= climate:
            result.append(row)
    return result


# 射影演算
def project(csv, header_list):
    result = []
    result.append(header_list)
    for row in csv:
        add_row = []
        for header in header_list:
            add_row.append(row[header])
        result.append(add_row)
    return result


if __name__ == '__main__':
    selected = select(csv_1, "雨", "soso", 0)
    print(project(selected, ["date", "weather", "condition", "random1"]))
