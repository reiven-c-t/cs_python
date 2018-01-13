#11-1-2018 venice
#206p

#11-1-2018 venice
#206p
#average3.py
def main():
    sum=0.0
    count = 0
    print("negative to quit")
    x = eval(input("<<<TYPE>>> #: "))

    #more = "yes"
    while x>=0:
        #x = eval(input("<<<TYPE>>> #: "))
        sum=sum+x
        count=count+1
        x = eval(input("<<<TYPE>>> #: "))
        #more=input("<<<TYPE>>> Y or N: ")

    print("\naverage #, ",sum/count)

main()




#############################################
#8-30

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

