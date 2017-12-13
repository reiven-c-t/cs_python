import math


def main():
    print("This program finds the real solutions to a quadratic\n")

    try:
        a, b, c = eval(input("Please enter the coefficients ( a, b , c): "))

        discRoot = math.squrt(b ** 2 - 4 * a * c)
        root1 = (-b + discRoot)/(2*a)
        root2 = (-b-discRoot)/(2*a)
        print("\nThe solutions are:", root1,root2)
    except ValueError as exc0bj:
        if str(exc0bj) == "math domain error":
            print("No real roots")
        else:
            print("You didn't give me right number of coefficients")
    except NameError:
        print("\nYou didn't enter three numbers")
    except TypeError:
        print("\nYour inputs were not all numbers")
    except SyntaxError:
        print("Your input was not in the correct form. Missing comma?")
    except:
        print("\nSomething went wrong, sorry.")

main()
