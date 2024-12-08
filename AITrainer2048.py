import random
import AI2048Runner
from Twenty48Networks import Twenty48Network
from copy import deepcopy
from Twenty48Networks import SaveNetwork
from Twenty48Networks import LoadNetwork





def createRandomNetworks(): # creates 50 random AI networks to start the training with
    return [Twenty48Network() for i in range(100)]

def runGames(networks):
    for network in networks:
        AI2048Runner.runAIGame(network)

def mutate(network: Twenty48Network):
    for layer in network.layers:
        for node in layer:
            for weight in node:
                if random.randint(0,10) < 2:
                    weight = weight * random.uniform(.8,1.2)


def mutateHalf(networkToMutate):
    newNetwork = deepcopy(networkToMutate)
    [mutate(network) for network in newNetwork]
    return newNetwork

highscore = 0

networks = createRandomNetworks()

try: 
    for i in range(50):
        networks[i] = LoadNetwork(i+1)
except: 
    print("CouldNotLoadNetwork")

networks : list[Twenty48Network]

running = True
genNumber = 0
while running:
    genNumber += 1
    runGames(networks)
    networks = sorted(networks,reverse=True)

    sumOfScores = 0
    sumOfRealScores = 0
    for network in networks:
        if (highscore < network.realScore):
            highscore = network.realScore
        sumOfScores += network.score
        sumOfRealScores += network.realScore
        print(f"Fitness: {network.score}, RealScore:{network.realScore}, Random Guess Precent: {round(network.randomGuesses/network.moves * 100,2)}%")
    print(f"\nGen {genNumber} Average: {sumOfScores/len(networks)}")
    print(f"Gen {genNumber} Real: {sumOfRealScores/len(networks)}")
    print(f"Gen {genNumber} Median: {(networks[49].realScore+networks[50].realScore)/2}")
    print(f"Highscore: {highscore}")
    print(f"Best Of Gen: {networks[0].realScore}")
    


    print("\n\n")

    otherHalf = mutateHalf(networks[int(len(networks)/2): len(networks)])

    networks = networks[0:int(len(networks)/2)] + otherHalf
    
    for i in range(50):
        SaveNetwork(i+1,networks[i])

    for network in networks:
        network.score = 0
        network.randomGuesses = 0
        network.moves = 0

