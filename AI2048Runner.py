from Twenty48ClassesAndMethods import *
from Twenty48Networks import Twenty48Network


#grid[][], Rows are the first brackets. collems are the second


def getAIPick(realGame: Twenty48Game,network : Twenty48Network):
    pick = network.calculateMove(realGame)
    network.moves += 1
    return pick


def runAIGame(network : Twenty48Network):
    testGame1 = Twenty48Game()
    testGame1.generateNewBlock()
    if __name__ == "__main__":
        print("\n"+str(testGame1)+"\n")
    running = True

    while running:
        pick : str = getAIPick(testGame1,network)
                
        match pick:
            case "d":
                testGame1.moveRight()
            case "a":
                testGame1.moveLeft()
            case "w":
                testGame1.moveUp()
            case "s":
                testGame1.moveDown()
        
        testGame1.generateNewBlock()
        if __name__ == "__main__":
            print(testGame1,"\n")
        if checkLoss(testGame1):
            running = False
    if __name__ == "__main__":
        print("\n\nAI LOST")
    network.score += testGame1.score
    network.realScore += testGame1.score
    return network.score, testGame1.score

if __name__ == "__main__":
    print(f"Final Score : {runAIGame(Twenty48Network())}")
