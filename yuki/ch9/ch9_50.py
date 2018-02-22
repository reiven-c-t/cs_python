#2018-2-20
#southeast library
from random import random

#TODO:finish 9.5

def simNGames(probA,probB,n):

    winsA=winsB=0
    serving="A"
    for i in range(30):
        scoreA, scoreB = simOneGame(probA, probB)
        if scoreA > scoreB:
            winsA = winsA + 1
        else:
            winsB = winsB + 1
    return winsA, winsB


def simOneGame(probA, probB):
    serving = "A"
    scoreA = 0
    scoreB = 0
    while not gameOver(scoreA, scoreB):
        if serving == "A":
            if random() < probA:
                scoreA = scoreA + 1
            else:
                serving = "B"
        else:
            if random() < probB:
                scoreB = scoreB + 1
    return scoreA, scoreB


def gameOver(a, b):
    return a == 15 or b == 15


def printSummary(winsA, winsB):
    n = winsA + winsB
    n = winsA+winsB
    print("\nGames simulated:",n)
    print("Wins for A: {0} ({1:0.1%})".format(winsA,winsA/n))
    print("Wins for B: {0} ({1:0.1%})".format(winsB, winsB / n))


main()
