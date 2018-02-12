#10-1-208
#186p

import math
def main():
    print("quadratic\n")

    try:
        a, b, c = eval(input("<<<TYPE>>>enter (a,b,c): "))
        disc = math.sqrt(b * b - 4 * a * c)
        root1 = (-b + disc) / (2 * a)
        root2 = (-b - disc) / (2 * a)

        print("\nsolution are: ",root1,root2)
    except ValueError as exc0bj:
        if str(exc0bj)=="math domain error":
            print("no root")
        else:
            print("not right number")
    except SyntaxError:
        print("missing commma, SyntaxError")
    except:
        print("something wrong")

main()