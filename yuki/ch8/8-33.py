# 11-1-2018
# 210p


# まわらん

# average5.py

def main():
    fileName = input("<<<TYPE>>>file name: ")
    infile = open(fileName, "r")

    sum = 0.0
    count = 0
    # print("negative to quit")
    # x = eval(input("<<<TYPE>>> #: "))

    # more = "yes"
    for line in infile:
        # x = eval(input("<<<TYPE>>> #: "))
        sum = sum + eval(line)
        count = count + 1
        # x = eval(input("<<<TYPE>>> #: "))
        # more=input("<<<TYPE>>> Y or N: ")

    print("\naverage #, ", sum / count)


main()

# C:\Users\pc-user\Desktop\book.xlsm

# 13-1-2018

#
#  commit test
# どうやら、「ずっとこみっとできないーーーーーー、って思ってたけど問題はなかったみたいだ
# 」
