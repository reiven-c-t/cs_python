import math  # Makes the math library available.


def main():
    print("This program finds the real solutions to a quadratic")
    print()
    a, b, c = eval(input("Please enter the coefficients (a, b, c): "))
    disc_root = math.sqrt(b * b - 4 * a * c)
    root1 = (-b + disc_root) / (2 * a)
    root2 = (-b - disc_root) / (2 * a)
    print()
    print("The solutions are:", root1, root2)


if __name__ == '__main__':
    main()