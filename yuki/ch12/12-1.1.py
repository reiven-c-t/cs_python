##6-1-2018

#

print()
#39p 2.5.2
#variable=input("prompt")

name=input("<TYPE>enter your name: ")
print(name)

x=eval(input("<TYPE> #: "))
print(x)
# x

#47p 2.7
def main():
    print("10 year rate")
    pri=eval(input("<TYPE>#:"))
    apr = eval(input( "< TYPE >  rate#:"))
    for i in range(10):
         pri = pri * (1 + apr)
    print("in 10 year",pri)
main()

#51p exercize
def main():
    print("start")
    for i in range(0):
        print("hello")
    print("end")
main()

for d in [1,6,5,8,9,4,4]:
    print(d, end=" ")
