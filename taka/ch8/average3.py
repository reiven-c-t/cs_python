def main():
    sum = 0.0
    count = 0
    x = eval(input("Enter a number (negative to quit) >>"))
    while x >= 0:
        count = count + 1
        sum = sum + x
        x = eval(input("Enter a number(negative to quit) >>"))
    print("\nTHe average of the numbers is", sum / count)

main()
