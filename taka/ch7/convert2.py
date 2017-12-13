def main():
    celsius = eval(input("What is the Celsius temperature?: "))
    fahranheit = 9/5 * celsius + 32
    print("The temperature is ", fahranheit, "degrees Fahrenheit")

    if fahranheit > 90:
        print("It's really hot out there. Becareful")

    if fahranheit < 30:
        print("Brrrr. Be sure to dress warmly!")

main()