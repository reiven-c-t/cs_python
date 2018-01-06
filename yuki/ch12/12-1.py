##rocket
##12-1
##YUKI_YAGI
##6-1-2018

#332p

#theGame = RBallGame(proA,proB)
#theGame.play()

def main():
    #printIntro()
    print()
    proA,proB,n=getInputs()
    #
    stats=simStats()
    for i in range(n):
        theGame = RBallGame(proA, proB)
        theGame.play()
        stats.update(theGame)
    stats.printReport()


main()