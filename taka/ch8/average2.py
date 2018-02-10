def main():
    sum = 0.0
    count =0
    moredata = "yes"
    while moredata[0] == "y":
        x = eval(input("Enter a number >>"))
        sum = sum+x
        count = count +1
        moredata = input("Do you want more data?(yes or no)")
    print("\nThe number of the average is", sum / count)

main()
