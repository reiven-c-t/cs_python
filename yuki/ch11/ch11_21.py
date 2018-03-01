
# stats.py


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
    return sqrt(sumDevSq / (len(nums) - 1))

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

    print("mean",xbar, "median",med, "sd",std)
    #print(xbar,med,std)






if __name__ =="__main__":main()
