def addInterest(balance, rate):
    newBalance = int(balance * (1+ rate))
    return newBalance

def test():
    amount = 1000
    rate = 0.05
    print( addInterest(amount, rate))

test()