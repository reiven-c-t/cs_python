# 2018-2-20
# at southeast library

#wrong_see ch11_21

# stats.py
#solvedTODO: failed to get mean, try again

from math import sqrt


def getNumbers():
    nums = []
    xStr = input("<<<TYPE>>>(ENTER to quit) number:")
    while xStr != "":
        x = eval(xStr)
        nums.append(x)
        xStr = input("<<<TYPE>>>(ENTER to quit) number:")
    return nums


def mean(nums):
    sum = 0.0
    for num in nums:
        sum = sum + num
        return sum / len(nums)


def stdDev(nums, xbar):
    sumDevSq = 0.0
    for num in nums:
        dev = num - xbar
        sumDevSq = sumDevSq + dev * dev
    return sqrt(sumDevSq / len(nums) - 1)


def median(nums):
    nums.sort()
    size = len(nums)
    midPos=size//2
    if size%2==0:
        median=(nums[midPos]+nums[midPos-1])/2.0
    else:
        median=nums[midPos]
    return median

def main():
    print("compute mean, median, standard deviation")
    data=getNumbers()
    xbar=mean(data)
    std=stdDev(data,xbar)
    med=median(data)

    print("mean median sd")
    print(xbar,med,std)






if __name__ =="__main__":main()











































    # TODO: yagi memo
    # nums.append() the meaning of this function
    # nums.sort()
