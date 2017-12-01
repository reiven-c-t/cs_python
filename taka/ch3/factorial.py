def main():
    n = eval(input("Please type the natural number you wanna compute factorial of: "))
    result=1
    for i in range(n):
        result=result*(i+1)
    print("factorial of",n,"is",result)

main()