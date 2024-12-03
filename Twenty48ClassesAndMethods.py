import random

class Twenty48Game(): # this is what will contain all the data and have methods for the actual 2048
    
    def __init__(self):
        self.grid = Twenty48Game.blankGrid()

    def blankGrid(): # creates an empty grid for the game
        return [[0 for i in range(4)] for j in range(4)]
    
    def __str__(self):
        temp = ""
        for i in range(4):
            for j in range(4):
                temp2 = " " * (6 - len(str(self.grid[i][j])))
                temp += f"{self.grid[i][j]} {temp2}"
            temp+="\n\n"
        return temp[:-1]
    
    def generateNewBlock(self):
        cordinates = self.getEmpty()
        rand1 = random.randint(1,10)
        if(rand1 > 10):
            self.grid[cordinates[0]][cordinates[1]] = 4
        else:
            self.grid[cordinates[0]][cordinates[1]] = 2
    
    def getEmpty(self): # gets a random empty square
        randX = random.randint(0,3)
        randY = random.randint(0,3)
        ticker = 0
        while (self.grid[randX][randY] != 0):
            randX = random.randint(0,3)
            randY = random.randint(0,3)
            if(ticker > 1000000):
                print("Almost certainly the game has been lost, yet you are trying to create a new block")
                return 0,0
            ticker += 1
        return randX,randY
        
    def moveRight(self): # moves all the blocks Left across the x axis, if possible, merges values
        for i in range(4):
            for j in range(4):
                value = self.grid[i][3-j]
                if value != 0:
                    self.moveBlockRight(value,i,3-j)
    
    def moveBlockRight(self,blockValue:int,row:int,col:int):
        if(col + 1 > 3):
            return
        if 0 == self.grid[row][col + 1]:
            self.grid[row][col + 1] = blockValue
            self.grid[row][col] = 0
            return self.moveBlockRight(blockValue,row,col+1)
        elif blockValue == self.grid[row][col + 1]:
            self.grid[row][col + 1] = blockValue * 2
            self.grid[row][col] = 0

    def moveLeft(self):
        for i in range(4):
            for j in range(4):
                value = self.grid[i][j]
                if value != 0:
                    self.moveBlockLeft(value,i,j)
    
    def moveBlockLeft(self,blockValue:int,row:int,col:int):
        if (col < 1):
            return
        if 0 == self.grid[row][col - 1]:
            self.grid[row][col - 1] = blockValue
            self.grid[row][col] = 0
            return self.moveBlockLeft(blockValue,row,col-1)
        elif blockValue == self.grid[row][col - 1]:
            self.grid[row][col - 1] = blockValue * 2
            self.grid[row][col] = 0

    def moveUp(self):
        for i in range(4):
            for j in range(4):
                value = self.grid[i][j]
                if value != 0:
                    self.moveBlockUp(value,i,j)

    def moveBlockUp(self,blockValue:int,row:int,col:int):
        if (row < 1):
            return
        if 0 == self.grid[row-1][col]:
            self.grid[row-1][col] = blockValue
            self.grid[row][col] = 0
            return self.moveBlockUp(blockValue,row-1,col)
        elif blockValue == self.grid[row-1][col]:
            self.grid[row-1][col] = blockValue * 2
            self.grid[row][col] = 0
    
    def moveDown(self):
        for i in range(4):
            for j in range(4):
                value = self.grid[3-i][j]
                if value != 0:
                    self.moveBlockDown(value,3-i,j)
    
    def moveBlockDown(self,blockValue:int,row:int,col:int):
        if(row + 1 > 3):
            return
        if 0 == self.grid[row +1][col]:
            self.grid[row+1][col] = blockValue
            self.grid[row][col] = 0
            return self.moveBlockDown(blockValue,row+1,col)
        elif blockValue == self.grid[row + 1][col]:
            self.grid[row + 1][col] = blockValue * 2
            self.grid[row][col] = 0
        
def checkLoss(realGame : Twenty48Game): # create a new instance and see if any possible moves will change it
    tempGame : Twenty48Game = Twenty48Game()
    tempGame.grid = realGame.grid
    tempGame = tempGame.moveUp()
    if(tempGame != realGame):
        return True
    tempGame = tempGame.moveDown()
    if(tempGame != realGame):
        return True
    tempGame = tempGame.moveLeft()
    if(tempGame != realGame):
        return True
    tempGame = tempGame.moveRight()
    if(tempGame != realGame):
        return True
    return False

def getPlayerImput():
    playerImput = input("w a s d?   ")
    while playerImput not in ["w","a","s","d"] and not checkMoveValidity(playerImput):
        playerImput = input("enterValidImput:   ")
        print("\n")
    return playerImput

def checkMoveValidity(realGame : Twenty48Game,move:str):
    tempGame = Twenty48Game()
    tempGame.grid = realGame.grid

    match move:
        case "w":
            tempGame = tempGame.moveUp()
            if(tempGame.grid == realGame.grid):
                return False
        case "d":
            tempGame = tempGame.moveRight()
            if(tempGame.grid == realGame.grid):
                return False
        case "s":
            tempGame = tempGame.moveDown()
            if(tempGame.grid == realGame.grid):
                return False
        case "a":
            tempGame = tempGame.moveLeft()
            if(tempGame.grid == realGame.grid):
                return False
    return True
        



