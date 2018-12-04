import FileUtil
import FeatureExtractor
import random
import os.path
from os.path import isfile, join
from os import listdir
from sklearn import svm

lsvm = svm.LinearSVC()

#Steady State Algorithm
#P <- generate a population of individuals randomly
#while stopping criterion has not been met:
#	parent1 <- tournament_selection(P)
#	parent2 <- tournament_selection(P)
#	child <- with probability cross_rate crossover parent1, parent2
#	child <- mutate child1
#   return child

#Get the total list of feature vectors
def createFeatureVectors(fileName):
    featureVectors = []
    with open(fileName) as fp:
        for line in fp:
            featureVectors.append(line)

    featureVectorsArrays = []
    i = 0
    for line in featureVectors:
        featureVectorsArrays.append(line.split(','))
        del featureVectorsArrays[i][-1]

        for j in range(1, len(featureVectorsArrays[i])):
            featureVectorsArrays[i][j] = float(featureVectorsArrays[i][j])

        i+=1
    return featureVectorsArrays

# Select Random 25 Population
def getPopulationOfRandom25(vectors):
    training_set = []
    for i in range(25):
        # Retrieve a feature vector at a random index
        vec = vectors[random.randint(0, len(vectors) - 1)]
        training_set.append(vec)
    return training_set

# Generate 25 feature mask
def generateFeatureMask():
    global_list = []
    for i in range(25):
        single_mask = []
        for j in range(95):
            ran_num = random.randint(0, 1)
            single_mask.append(ran_num)
        global_list.append(single_mask)
    return global_list

# Get accuracy of each individuals  []   [1,2,3,4,5,6]
def generateNewTrainingSet(feature_mask, original_training_set):
    t_prime = []
    for i in range(25):
        workable_set = original_training_set[i]
        workable_set = workable_set[1:]
        data = multiplyLists(feature_mask, workable_set)
        t_prime.append(data)
    return t_prime;

def multiplyLists(list1, list2):
    if len(list1) < len(list2):
        numOfIterations = len(list1)
    else:
        numOfIterations = len(list2)

    productList = []
    for i in range(numOfIterations):
        productList.append(list1[i] * list2[i])

    return productList

###################################### Steady State Algorithm Code #####################################

# Tournament Selection Algorithm
def tournamentSelectionAlgorithm(population, accuracies):
    highest_accuracy = -1
    parents_list = []

    pick1 = random.randint(0, len(population) - 1)
    pick2 = random.randint(0, len(population) - 1)
    for i in range(25):
        if(accuracies[pick1] >= accuracies[pick2]):
            parents_list.append(population[pick1])
            parents_list.append(population[pick2])
        else:
            parents_list.append(population[pick2])
            parents_list.append(population[pick1])
    return parents_list

def uniformCrossover(parent1, parent2, k = 1):
    if k >= len(parent1) - 1:
        k = len(parent1) - 2

    if k < 1:
        k = 1

    crossoverPoints = []
    availablePoints = range(1, len(parent1) - 1)

    for i in range(k):
        point = random.choice(availablePoints)
        crossoverPoints.append(point)
        availablePoints.remove(point)

    crossoverPoints.sort()

    child1 = []
    child2 = []

    child1.extend(parent1[0:crossoverPoints[0]])
    child2.extend(parent2[0:crossoverPoints[0]])

    for i in range(len(crossoverPoints) - 1):
        if i % 2 == 0:
            child1.extend(parent2[crossoverPoints[i]:crossoverPoints[i+1]])
            child2.extend(parent1[crossoverPoints[i]:crossoverPoints[i+1]])

        else:
            child1.extend(parent1[crossoverPoints[i]:crossoverPoints[i+1]])
            child2.extend(parent2[crossoverPoints[i]:crossoverPoints[i+1]])

    if len(crossoverPoints) % 2 == 0:
        child1.extend(parent1[crossoverPoints[-1]:len(parent1)])
        child2.extend(parent2[crossoverPoints[-1]:len(parent2)])

    else:
        child1.extend(parent2[crossoverPoints[-1]:len(parent2)])
        child2.extend(parent1[crossoverPoints[-1]:len(parent1)])

    # Mutation
    for i in range(len(child1)):
        randNum = random.uniform(0.0, 1.0)
        if randNum <= .05:
            if child1[i] == 1:
                child1[i] = 0
            else:
                child1[i] == 1
    return child1

# Steady State Genetic Genetic Algorithm
def steadyStateAlgorithm(population, accuracies):
    # Pick parents
    parents = tournamentSelectionAlgorithm(population, accuracies)
    parent1 = parents[0]
    parent2 = parents[1]

    # Crossover and mutation
    child = uniformCrossover(parent1, parent2)
    return child
