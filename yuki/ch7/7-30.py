#10-1-2018
#184p

#copy from 7-21
##############
import math
def main():
#    import math
    print("quadratic\n")
    print("a*x^2 + b*x + c")

    a, b, c = eval(input("<<<TYPE>>>enter (a,b,c): "))
    disc = math.sqrt(b * b - 4 * a * c)


    if disc < 0:
        print("no answer")







    else:
      if disc ==0:
          print("answer",-b/(2*a))


      else:

            root1 = (-b + disc) / (2 * a)
            root2 = (-b - disc) / (2 * a)

            print("\nsolution are: ", root1, root2)



main()