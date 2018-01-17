##rocket
##11-1
##YUKI_YAGI
##6-1-2018

#292p

def main():
    sum=0.0
    count=0
    xStr=input("<TYPE># <enter to quit>>>")
    while xStr != "":
        x = eval(xStr)
        sum=sum+x
        count=count+1
        xStr=input("<TYPE># >> ")
    print("\nThe average of the # is ", sum/count)
main()