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
        return self
    
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
        return self
    
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
        return self

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
        return self
    
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
        
    def checkSameGrid(self,other):
        for i in range(4):
            for j in range(4):
                if (self.grid[i][j] != other.grid[i][j]):
                    return False
        return True
    
def checkLoss(realGame : Twenty48Game): # create a new instance and see if any possible moves will change it

    return False

def getPlayerImput(playerGame):
    playerImput = input("w a s d?   ")
    while playerImput not in ["w","a","s","d"] or not checkMoveValidity(playerGame,playerImput):
        playerImput = input("enterValidImput:   ")
    return playerImput

def checkMoveValidity(realGame : Twenty48Game,move : str):
    match move:
        case "d":
            if checkMoveValidRight(realGame):
                return True
        case "a":
            if checkMoveValidLeft(realGame):
                return True
        case "w":
            if checkMoveValidUp(realGame):
                return True
        case "s":
            if checkMoveValidity(realGame):
                return True

    return False

def checkEmpty(realGame : Twenty48Game):
    for row in range(4):
        for col in range(4):
            if realGame.grid[col][row] == 0:
                return True
    return False

def checkMoveValidRight(realGame: Twenty48Game):
    for row in range(4):
        for col in range(3):
            if (realGame.grid[row][col] == realGame.grid[row][col + 1]):
                return True
    return False

def checkMoveValidLeft(realGame: Twenty48Game):
    for row in range(4):
        for col in range(1,4):
            if realGame.grid[row][col] == realGame.grid[row][col -1]:
                return True
    return False

def checkMoveValidUp(realGame : Twenty48Game):
    for row in range (3):
        for col in range(4):
            if realGame.grid[row][col] == realGame.grid[row+1][col]:
                return True
    return False

def checkMoveValidUp(realGame : Twenty48Game):
    for row in range (1,4):
        for col in range(4):
            if realGame.grid[row][col] == realGame.grid[row-1][col]:
                return True
    return False
        
def compareSpots(row1:int, col1: int, row2 : int, col2 : int):


