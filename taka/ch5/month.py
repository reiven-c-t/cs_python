def main():
    month="JanFebMarAprMayJunJulAugSepOctNoxDec"

    n= eval(input("Enter a month number (1-12): "))

    pos = (n-1)*3
    monthAbbrev=month[pos:pos+3]

    print("The month abbreviation is",monthAbbrev+".")

main()