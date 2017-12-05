def main():
    print("This program converts a sequence of Unicode numbers into")
    print("the string of text that it represents.\n")

    inString = input("Please enter the Unicode-encoded message: ")

    chars = []
    for numStr in inString.split():
        codeNum = eval(numStr)
        chars.append(chr(codeNum))

    message = "".join(chars)
    print("\nThe decoded message is:", message)

main()