##rocket
##81
##YUKI_YAGI
##6-1-2018


def main():
    n = eval(input("<TYPE># you have: "))
    sum=0.0
    for i in range(n):
        x = eval(input ("enter # >> "))
        #sum = sum +1
        sum = sum + x
    print("\naverage #: ",sum/n)
main()