def main():
    printIntro()
    probA, probB, n = getInputs()
    winsA, winsB = simNgames(n, probA, probB)
    printSummary(winsA,winsB)

def printIntro():
    print("THis program simulates a game of racquetball between two")
    print