#11-1-2018
#193p

def main():
    n = eval(input("<<<TYPE>>> amount of #: "))
    max = eval(input("<<<TYPE>>> enter #: "))

    for i in range(n-1):
        x = eval(input("<<<TYPE>>> enter #: "))
        if x > max:
            max = x

    print("\nbiggest number: ",max)

main()
