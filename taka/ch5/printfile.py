def main():
    fname = input("Put into file name")
    infile =open(fname,"r")
    data = infile.read()
    print(data)

main()