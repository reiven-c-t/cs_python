import math

def main():
    print("This program finds the real solutions to a quadratic")
    print()

    a,b,c=eval(input("Please enter the coeffficients(a,b,c,): "))

    discRoot=math.sqrt(b**2-4*a*c)
    root1=(-b+discRoot)/(2*a)
    root2=(-b-discRoot)/(2*a)

    print()
    print("The solutions are : ",root1,root2)

main()