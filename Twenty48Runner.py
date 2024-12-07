from Twenty48ClassesAndMethods import *
#grid[][], Rows are the first brackets. collems are the second

def runGame():
    testGame1 = Twenty48Game()
    testGame1.generateNewBlock()

    print("\n"+str(testGame1))
    running = True

    while running:
        playerInput = getPlayerImput(testGame1)
        match playerInput:
            case "d":
                testGame1.moveRight()
            case "a":
                testGame1.moveLeft()
            case "w":
                testGame1.moveUp()
            case "s":
                testGame1.moveDown()
        
        testGame1.generateNewBlock()
        print(testGame1)
        # if not checkLoss(testGame1):
        #     running = False

    print("\n\nYOU LOST")

runGame()