def main():
    fname = input("Put into file name")
    infile =open(fname,"r")
    for i in range(infile.readlines()):
        data = infile.readline()
        print(data,end="")
    infile.close()
main()