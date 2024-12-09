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
        self.surfaceDict["4096"] = pygame.image.load("Assets/Block4096.png")
        self.surfaceDict["8192"] = pygame.image.load("Assets/Block8192.png")
        
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

        
def getPick(game):
    ready = False
    while not ready:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit(1)
            if event.type == pygame.KEYDOWN: 
                print("Keydown")
                if event.key == pygame.K_d: 
                    if checkMoveValidity(game,"d"):
                        return "d"
                elif event.key == pygame.K_a:
                    if checkMoveValidity(game,"a"):
                        return "a"
                elif event.key == pygame.K_s:
                    if checkMoveValidity(game,"s"):
                        return "s"
                elif event.key == pygame.K_w:
                    if checkMoveValidity(game,"w"):
                        return "w"
                elif event.key == pygame.K_ESCAPE: 
                    print("Escape key")
                    running = False
                    


def runGame():
    realStop = False
    pygame.init()
    renderer = Renderer((1280,720))

    testGame1 = Twenty48Game()
    testGame1.generateNewBlock()
    testGame1.generateNewBlock()
    running = True
    renderer.renderFrame(testGame1)
    pygame.display.flip()
    while running:

        pick : str = getPick(testGame1)
                
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
    runGame()

if __name__ == "__main__":
    runGame()
