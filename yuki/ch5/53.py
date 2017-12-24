print("hello world")
print([1,2]+[3,4])

print("gds")

def main():
    months="AaaBbbCccDddEeeFffGggHhhIiiJjjKkkLll"
    n = eval(input("Enter:"))
    pos=(n-1)*3
    monthAbbrev=months[pos:pos+3]
    print("answer", monthAbbrev+".")
main()