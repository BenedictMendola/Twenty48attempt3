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
                if random.randint(0,3000) == 50:
                    weight = weight * random.uniform(.5,1.5)
                elif random.randint(0,100) < 20:
                    weight = weight * random.uniform(.9,1.1)


def mutateHalf(networkToMutate):
    newNetwork = deepcopy(networkToMutate)
    [mutate(network) for network in newNetwork]
    return newNetwork


networks = createRandomNetworks()

try: 
    for i in range(50):
        networks[i] = LoadNetwork(i+1)
    print("Loaded Networks")
except: 
    print("CouldNotLoadNetwork")

networks : list[Twenty48Network]

running = True
genNumber = 0
while running:
    genNumber += 1
    for i in range(10):
        runGames(networks)
    networks = sorted(networks,reverse=True)

    sumOfScores = 0
    sumOfRealScores = 0
    for network in networks:
        sumOfScores += network.score
        sumOfRealScores += network.realScore
        print(f"Avg Fitness: {network.score/10}, Avg RealScore:{network.realScore/10}")
    print(f"\nGen {genNumber} Average: {(sumOfScores/len(networks))/10}")
    print(f"Gen {genNumber} Real: {(sumOfRealScores/len(networks))/10}")
    print(f"Gen {genNumber} Median: {(networks[49].realScore+networks[50].realScore)/20}")
    print(f"Best Of Gen: {networks[0].realScore/10}")
    


    print("\n\n")

    otherHalf = mutateHalf(networks[int(len(networks)/2): len(networks)])

    networks = networks[0:int(len(networks)/2)] + otherHalf
    
    for i in range(50):
        SaveNetwork(i+1,networks[i])

    for network in networks:
        network.score = 0
        network.realScore = 0

