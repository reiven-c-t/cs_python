print("Test")


def test():
    print("s")
    for i in range(1, 100):
        if i % 3 == 0:
            print("fizz")
        if i % 5 == 0:
            print("buzz")
        print(i)

    return


if __name__ == '__main__':
    test()
