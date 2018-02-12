# 28-1-2018
__date__ = "28-1-2018"
#7.pyaverage

def main():
    fileName = input("<<<TYPE>>>what file are the numbers in?:")
    infile = open(fileName,'r')
    sum = 0.0
    count = 0
    line = infile.readline()
    while line != "":
        for xStr in line.split(","):
            sum = sum + eval(xStr)
            count = count + 1
        line = infile.readline()
    print("\nThe average of the number is", sum / count)


main()
