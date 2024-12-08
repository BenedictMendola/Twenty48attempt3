import random
from Twenty48ClassesAndMethods import *
import math
import json

class Twenty48Network:

    def __init__(self):
        self.score = 0
        self.realScore = 0
        self.randomGuesses = 0
        self.moves = 0
        self.layer1 = createLayer(12,17) # layer 1 each node has 17 inputs, all layers exept final have 12 nodes
        self.layer2 = createLayer(12,12) 
        self.layer3 = createLayer(12,12)
        self.layer4 = createLayer(12,12) 
        self.layer5 = createLayer(4,12) # has only 4 nodes, each signfys the leaning toward one output
        self.layers = [self.layer1,self.layer2,self.layer3,self.layer4,self.layer5]
        
    def calculateMove(self, realGame: Twenty48Game,repeats: int = 0):
        imputs = getImputs(realGame.grid) + [repeats]
        
        # each node will equal the sigmoid of the sum of the weights of each node multiplied by the nodes of the last layer
        firstLayerCalculated = calculateLayer(imputs,self.layers[0])
        seconedLayerCalculated = calculateLayer(firstLayerCalculated,self.layers[1])
        thirdLayerCalculated = calculateLayer(seconedLayerCalculated,self.layers[2])
        fourthLayerCalculated = calculateLayer(thirdLayerCalculated,self.layers[3])
        fourFinalNodes = calculateLayer(fourthLayerCalculated,self.layers[4])

        pick = fourFinalNodes.index(max(fourFinalNodes))

        match pick:
            case 0:
                return "w"
            case 1:
                return "d"
            case 2:
                return "s"
            case 3:
                return "d"
            
    def __lt__(self,other):
        return self.score < other.score
        
    
def sigmoid(x): return 1/(1 + pow(math.e,-x))
        
def calculateLayer(layer1: list, layer2 : list): #gets sigmoided sums of each nodes weights mutlipled by evey node after

    calculatedValues = []

    for node in layer2:
        sumOfNode = 0
        for connectionNumber in range(len(node)):
            sumOfNode += node[connectionNumber] * layer1[connectionNumber]
        calculatedValues.append(sigmoid(sumOfNode/3))
    return calculatedValues


def createLayer(nodeAmount: int,nodeLength: int): # a layer is a list of nodes, each of which is a list of connections
    return [createNode(nodeLength) for i in range(nodeAmount)]

def createNode(connectionAmonnt: int): # nodes are a list of weights
    return [random.uniform(0,1) for i in range(connectionAmonnt)]

def getImputs(game:list):
    returnList = []
    for i in range(4):
        for j in range(4):
            returnList.append(game[i][j])
    return returnList

def SaveNetwork(networkNumber:int,network: Twenty48Network):
    with open(f"Network{networkNumber}.json",'w') as file:
        data = {"layers":network.layers}
        json.dump(data,file)

def LoadNetwork(networkNumber:int):
    with open(f"Network{networkNumber}.json",'r') as file:
        data = json.load(file)
        loadedNetwork: Twenty48Network = Twenty48Network()
        loadedNetwork.layers = data["layers"]
        return loadedNetwork