#11-1-2018 venice
#209p

#回らん


#average4.py
def main():
    sum=0.0
    count = 0
    #print("negative to quit")
    xStr = eval(input("<<<TYPE>>> #(enter to quit): "))

    #more = "yes"
    while xStr != "":
        # x = eval(xStr)
        sum=sum+float(xStr)
        count=count+1
        xStr = input("<<<TYPE>>>(enter) #: ")
        #more=input("<<<TYPE>>> Y or N: ")



    print("\naverage #, ",sum/count)

main()