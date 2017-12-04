def main():
    print("This program converts a textual message into a sequence")
    print("of numbers responding the Unicode encoding of the message.\n")

    message = input("Please enter the message to decode(Please divide the numbers with spaces): ")
    print("\nHere are the Unicode codes: ")
    for ch in message.split():
        print(chr(eval(ch)), end="")

main()
