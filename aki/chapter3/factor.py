def main():
    n = eval(input("Please enter a whole number: "))
    fact = 1
    for factor in range(n,1,-1):
        fact *= factor
    print("The factorial of", n, "is", fact)

if __name__ == '__main__':
    main()