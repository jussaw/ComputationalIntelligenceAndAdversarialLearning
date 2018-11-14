import random
import Data_Utils
from sklearn.model_selection import StratifiedKFold
from sklearn.preprocessing import StandardScaler, normalize
from sklearn import svm
from sklearn.neural_network import MLPClassifier
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.model_selection import StratifiedKFold
from sklearn import preprocessing
import numpy as np
from sklearn.model_selection import cross_val_score


def elitistGA(dataSet, numOfChildren, numOfStartingPopulation, numOfParents = 2):
    # Code from driver
    lsvm = svm.LinearSVC()

    skf = StratifiedKFold(n_splits=4, shuffle=True, random_state=0)
    fold_accuracy = []

    scaler = StandardScaler()
    tfidf = TfidfTransformer(norm=none)
    dense = Data_Utils.DenseTransformer()

    # Dataset
    dataSet = createFeatureVectors("../../Feature Vectors/output.txt")

    # K for uniform cross over
    k = 2

    # create individuals
    individuals = createIndividuals(numOfStartingPopulation)

    # Add Individuals
    children = []
    for i in range(numOfChildren):
        #create parents
        parent1, parent2 = createParents(individuals)

        #create children
        child1, child2 = uniformCrossover(parent1, parent2, k)

        #determine best child from two


        #Add best child to indivicuals





        pass

def determineAccuracy(dataSet, individual, lsvm):
    lsvm.fit
    pass


def createIndividuals(numOfStartingPopulation = 25):
    individuals = []
    numOfIndividuals = numOfStartingPopulation

    for i in range(numOfIndividuals):
        individual = []

        for j in range(94):
            individual.append(random.randint(0, 1))

        individuals.append(individual)

    return individuals

def createIndividualLabels(numOfStartingPopulation = 25):
    labels = []
    for i in range(numOfStartingPopulation):
        label = "Individual " + str(i)
        labels.append(label)

    return labels

def createParents(individuals):
    availableNumbers = range(len(individuals))

    parentIndex1 = random.choice(availableNumbers)
    availableNumbers.remove(parentIndex1)

    parentIndex2 = random.choice(availableNumbers)
    availableNumbers.remove(parentIndex2)

    return individuals[parentIndex1], individuals[parentIndex2]

def determineStartingPopulation(featureVectors):
    if len(featureVectors) < 25:
        return featureVectors

    startingPopulaton = []
    availableIndexes = range(len(featureVectors))

    for i in range(25):
        currentIndex = random.choice(availableIndexes)
        startingPopulaton.append(featureVectors[currentIndex])
        availableIndexes.remove(currentIndex)

    return startingPopulaton

def generateFeatureMasks():
    featureMasks = []

    for i in range(25):
        featureMask = []

        for j in range(95):
            featureMask.append(random.randint(0, 1))

        featureMasks.append(featureMask)

    return featureMasks

def multiplyLists(list1, list2):
    if len(list1) < len(list2):
        numOfIterations = len(list1)
    else:
        numOfIterations = len(list2)

    productList = []
    for i in range(numOfIterations):
        productList.append(list1[i] * list2[i])

    return productList

def separateLabels(dataSet):
    labels = []
    dataOut = []
    for data in dataSet:
        labels.append(data[0])
        dataOut.append(data[1:])

    return dataOut, labels

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
        if randNum <= 0.05:
            if child1[i] == 1:
                child1[i] = 0
            else:
                child1[i] == 1

        randNum = random.uniform(0.0, 1.0)
        if randNum <= 0.05:
            if child2[i] == 1:
                child2[i] = 0
            else:
                child2[i] = 1

    return child1, child2

def getTPrimes(individual, dataSet):
    tPrimes = []

    for data in dataSet:
        tPrimes.append(multiplyLists(individual, data))

    return tPrimes

def getHighestAccuracy(accuracies):
    highestIndex = 0

    for i in range(len(accuracies)):
        if accuracies[i] > accuracies[highestIndex]:
            highestIndex = i

    return highestIndex

def printSizeOfEachArray(twoDArray):
    for array in twoDArray:
        print len(array)

def getAverage(numbers):
    sum = 0.0
    for number in numbers:
        sum += number
    sum /= len(numbers)
    return sum

def getHighestNumber(numbers):
    highestNum = 0
    for num in numbers:
        if num > highestNum:
            highestNum = num

    return highestNum
