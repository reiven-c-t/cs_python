# 2018 3 12

def main():
    printIntro()
    probA, probB, n = getInputs()

    stats = SimStats()
    for i in range(n):
        theGame = RBallGame(probA, probB)
    theGame.play()
    stats.update(theGame)
    stats.printReport()
