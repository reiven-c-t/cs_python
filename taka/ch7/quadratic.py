import math


def main():
    print("This program finds the real solutions to a quadratic\n")

    a, b, c = eval(input("Please enter the coefficients ( a, b , c) "))

    discrim = b ** 2 - 4 * a * c
    if discrim >= 0:
        discRoot = math.sqrt(discrim)
        root1 = (-b + discRoot) / (2 * a)
        root2 = (-b - discRoot) / (2 * a)

        print("\nThe solutions are:", root1, root2)
    if discrim < 0:
        print("The equation has no real roots!")


main()
