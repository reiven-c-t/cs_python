#10-1-2018
#164p

def add(bal,rate):
    newBal=bal*(1+rate)
    bal=newBal
#    print(bal)

add(100,0.5)
#print(bal): errorbeyond function


def eest():
    amount = 1000
    rate=0.05
    add(amount,rate)
#    print(amount)

#eest()

#add.eest()

#add.eest()

#162pにも同じ式ある


#163p
def add2(bal,rate):
    for i in range(len(bal)):
        bal[i]=bal[i]-(1+rate)
        #print(amount)

amounts=[645,8465,8465,45]
add2(amounts,0.05)
print(amounts)
