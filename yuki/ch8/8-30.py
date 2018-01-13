#11-1-2018 venice
#206p

def main():
    sum=0.0
    count = 0

    more = "yes"
    while more[0] =="y":
        x = eval(input("<<<TYPE>>> #: "))
        sum=sum+x
        count=count+1
        more=input("<<<TYPE>>> Y or N: ")

    print("\naverage #, ",sum/count)

main()

