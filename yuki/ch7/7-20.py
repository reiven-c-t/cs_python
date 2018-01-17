#10-1-2018
#180p

def main():
    import math
    print("quadratic\n")
    print("a*x^2 + b*x + c")

    a,b,c = eval(input("<<<TYPE>>>enter (a,b,c): "))
    disc=math.sqrt(b*b-4*a*c)
    root1=(-b+disc)/(2*a)
    root2=(-b-disc)/(2*a)

    print("\nsolution are: ",root1,root2)



main()

#181p
