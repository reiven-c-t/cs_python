#10-1-2018
#185p

import math
def main():
#    import math
    print("quadratic\n")
    print("a*x^2 + b*x + c")

    a, b, c = eval(input("<<<TYPE>>>enter (a,b,c): "))
    #discR = math.sqrt(b * b - 4 * a * c)
    disc = b * b - 4 * a * c


    if disc < 0:
        print("no answer")

    elif disc ==0:
          print("answer",-b/(2*a))

    else:
            discR = math.sqrt(b * b - 4 * a * c)
            root1 = (-b + discR) / (2 * a)
            root2 = (-b - discR) / (2 * a)

            print("\nsolution are: ", root1, root2)



main()