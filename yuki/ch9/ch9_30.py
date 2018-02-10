# 13-1-2018 milano(ミラノ風ドリアのとこ) Italy, この度もあと二日
# 237p
# 2017-2-10
# 242p

from random import random


def main():
    printIntro()
    probA, probB, n = getInputs()
    winsA, winsB = simNGames(probA, probB, n)
    printSummary(winsA, winsB)
    # did


def printIntro():
    print("2 players simulation, ability is equal to the probability to win the point when serving")
    print("A always has first serve")
    # did


def getInputs():
    a = eval(input("<<<TYPE>>> pro A win serve: "))
    b = eval(input("<<<TYPE>>> pro B win serve: "))
    n = eval(input("<<<TYPE>>> how many game: "))
    return a, b, n
    # did


def simNGames(probA,probB,n):
    # kaiketsu:なぜかエラー
    winsA=winsB=0
    for i in range(n):
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
