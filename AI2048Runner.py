from Twenty48ClassesAndMethods import *
import random
#grid[][], Rows are the first brackets. collems are the second
def getAIPick(realGame: Twenty48Game):
    rand = random.randint(1,4)
    randLetter = ""
    match rand:
        case 1:
            randLetter = "w"
        case 2:
            randLetter = "d"
        case 3:
            randLetter = "s"
        case 4:
            randLetter = "a"
    if not checkMoveValidity(realGame,randLetter):
        return(getAIPick(realGame))

    return randLetter

def runAIGame():
    testGame1 = Twenty48Game()
    testGame1.generateNewBlock()

    print("\n"+str(testGame1))
    running = True

    while running:
        rand : str = getAIPick(testGame1)
                
        match rand:
            case "d":
                testGame1.moveRight()
            case "a":
                testGame1.moveLeft()
            case "w":
                testGame1.moveUp()
            case "s":
                testGame1.moveDown()
        
        testGame1.generateNewBlock()
        print(testGame1,"\n")
        # if not checkLoss(testGame1):
        #     running = False
        if checkLoss(testGame1):
            running = False

    print("\n\nAI LOST")
    return testGame1.score

print(f"Final Score : {runAIGame()}")
