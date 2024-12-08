import pygame
from Twenty48ClassesAndMethods import *
import random
from Twenty48Networks import Twenty48Network
import time
from Twenty48Networks import LoadNetwork

class Renderer():
    def __init__(self,screenSize:tuple):
        self.screenSize = screenSize
        self.screen = pygame.display.set_mode(screenSize)
        self.backgroundColor = pygame.Color(240, 240, 240)

        self.surfaceDict = {}
        self.surfaceDict["background"] = pygame.image.load("Assets/Background2048.png")
        self.surfaceDict["2"] = pygame.image.load("Assets/Block2.png")
        self.surfaceDict["4"] = pygame.image.load("Assets/Block4.png")
        self.surfaceDict["8"] = pygame.image.load("Assets/Block8.png")
        self.surfaceDict["16"] = pygame.image.load("Assets/Block16.png")
        self.surfaceDict["32"] = pygame.image.load("Assets/Block32.png")
        self.surfaceDict["64"] = pygame.image.load("Assets/Block64.png")
        self.surfaceDict["128"] = pygame.image.load("Assets/Block128.png")
        self.surfaceDict["256"] = pygame.image.load("Assets/Block256.png")
        self.surfaceDict["512"] = pygame.image.load("Assets/Block512.png")
        self.surfaceDict["1024"] = pygame.image.load("Assets/Block1024.png")
        self.surfaceDict["2048"] = pygame.image.load("Assets/Block2048.png")

        pygame.font.init()

        self.font1 = pygame.font.SysFont("wow",size =30)
        
    def renderFrame(self,game: Twenty48Game):
        self.screen.fill(self.backgroundColor)

        for row in range(4): # rendering each block
            for col in range(4):
                if game.grid[row][col] > 0:
                    surface : pygame.Surface = self.surfaceDict[str(game.grid[row][col])]
                    surface = pygame.transform.scale(surface,(surface.get_width() * 8,surface.get_height() *8))
                    xplacement = (col * 136 + 436) - surface.get_width() / 2
                    yPlacement = (row * 136 + 160) - surface.get_height() /2
                    self.screen.blit(surface,(xplacement,yPlacement))
        surface : pygame.Surface = self.surfaceDict['background']
        surface = pygame.transform.scale(surface,(surface.get_width() * 8,surface.get_height() *8))
        xplacement = self.screen.get_width()/2 - surface.get_width() / 2
        yPlacement = self.screen.get_height()/2 - surface.get_height() /2

        self.screen.blit(surface,(xplacement,yPlacement))
        
        textSurface = self.font1.render(f'Score: {game.score}', False, (0, 0, 0))
        self.screen.blit(textSurface,(self.screen.get_width()/2 - textSurface.get_width()/2,self.screen.get_height()*.9))

        

                    

def getAIPick(realGame: Twenty48Game,network : Twenty48Network):
    pick = network.calculateMove(realGame)
    repeats = 0
    while not checkMoveValidity(realGame,pick):
        repeats += 1
        pick = network.calculateMove(realGame,repeats)
        if repeats > 5:
            network.score -= 5
            network.randomGuesses += 1
            return getRandPick(realGame)
    network.moves += 1
    time.sleep(.05)
    return pick

def getRandPick(realGame: Twenty48Game): # ONLY FOR EXTREAM CASES WHERE AI CANNOT MOVE AND IS STUCK ON ONE MOVE
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
        return(getRandPick(realGame))

    return randLetter

def runAIGame(network : Twenty48Network,AIPlaying = True):
    realStop = False
    pygame.init()
    renderer = Renderer((1280,720))

    testGame1 = Twenty48Game()
    testGame1.generateNewBlock()
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

        if checkLoss(testGame1):
            running = False

        renderer.renderFrame(testGame1)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit(1)
                return "STOP"
        
        pygame.display.flip()


    while not realStop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit(1)
                return "STOP"
            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_SPACE: 
                    realStop = True
                elif event.key == pygame.K_ESCAPE: 
                    realStop = False
        pygame.display.flip()
    runAIGame(LoadNetwork(1))

    network.score += testGame1.score
    network.realScore = testGame1.score
    return network.score, testGame1.score

if __name__ == "__main__":
    print(f"Final Score : {runAIGame(LoadNetwork(1),True)}")
