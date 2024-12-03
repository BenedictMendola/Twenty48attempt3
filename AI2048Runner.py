from Twenty48ClassesAndMethods import *
import random
#grid[][], Rows are the first brackets. collems are the second

def runAIGame():
    testGame1 = Twenty48Game()
    testGame1.generateNewBlock()

    print("\n"+str(testGame1))
    running = True

    while running:
        rand = random.randint(1,4)
        match rand:
            case 1:
                testGame1.moveRight()
            case 2:
                testGame1.moveLeft()
            case 3:
                testGame1.moveUp()
            case 4:
                testGame1.moveDown()
        
        testGame1.generateNewBlock()
        print(testGame1,"\n")
        # if not checkLoss(testGame1):
        #     running = False

    print("\n\nYOU LOST")

runAIGame()