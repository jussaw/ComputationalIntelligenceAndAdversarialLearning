import ElitistGeneticAlgorithm
import FileUtil
from sklearn import svm
from numpy import array

bestKvalue = 0
bestKValueAcc = 0
highestKAccuracy = 0
highestk = 0

for p in range(1, 96, 10):
    NUM_OF_ITERATIONS = 5000
    K = p # num of points for uniform crossover
    print("K Value: " + str(K))

    errorRates = []
    accuracies = []
    labels = []
    lsvm = svm.LinearSVC()

    # Retrieve feature vectors
    featureVectors = FileUtil.createFeatureVectors("../../Feature Vectors/outputNormalized.txt")

    # Retrieve training set of random 25 population
    originalTrainingSet = ElitistGeneticAlgorithm.determineStartingPopulation(featureVectors)

    # Separate labels and data
    currentDataSet, labels = ElitistGeneticAlgorithm.separateLabels(originalTrainingSet)

    # create initial population
    population = ElitistGeneticAlgorithm.createIndividuals()
    populationLabels = ElitistGeneticAlgorithm.createIndividualLabels()


    highestAccuracies = []
    for i in range(NUM_OF_ITERATIONS):
        # create children
        children = []
        childrenLabels = []
        for j in range(12):
            parent1, parent2 = ElitistGeneticAlgorithm.createParents(population)
            child1, child2 = ElitistGeneticAlgorithm.uniformCrossover(parent1, parent2, K)

            childLabel1 = "Child" + str(i + (2*j))
            childLabel2 = "Child" + str(i + ((2*j) + 1))

            children.append(child1)
            children.append(child2)

            childrenLabels.append(childLabel1)
            childrenLabels.append(childLabel2)

        # determine the best fit in population
        tPrimes = []
        for individual in population:
            tPrime = ElitistGeneticAlgorithm.getTPrimes(individual, currentDataSet)
            if len(tPrime) != None:
                tPrimes.append(tPrime)
                # print tPrime

        accuracies = []
        for tPrime in tPrimes:
            tPrimeArray = array(tPrime)
            populationLabelsArray = array(populationLabels)

            # print ElitistGeneticAlgorithm.printSizeOfEachArray(tPrime)

            lsvm.fit(tPrime, populationLabels)
            acc = lsvm.score(tPrime, populationLabels)
            accuracies.append(acc)

        highestIndex = ElitistGeneticAlgorithm.getHighestAccuracy(accuracies)

        averageAcc = ElitistGeneticAlgorithm.getAverage(accuracies)
        print("Iteration " + str(i) + ": " + str(averageAcc))

        highestAccuracies.append(averageAcc)

        # replace the worst 24 with the children
        population = [population[highestIndex]]
        population.extend(children)


    averageHighestAccuracies = ElitistGeneticAlgorithm.getAverage(highestAccuracies)
    print("Average of all highest accuracies is: " + str(averageHighestAccuracies))

    highestAccuracy = ElitistGeneticAlgorithm.getHighestNumber(highestAccuracies)
    print("Highest of all highest accuracies is: " + str(highestAccuracy) + "\n\n")


    if averageHighestAccuracies > bestKValueAcc:
        bestKValueAcc = averageHighestAccuracies
        bestKvalue = K

    if highestAccuracy > highestKAccuracy:
        highestKAccuracy = highestAccuracy
        highestK = K
    # calculate baseline

print("Best k value is: " + str(bestKvalue))
print("Best accuracy is: " + str(bestKValueAcc))


print("Highest k value is: " + str(highestK))
print("Highest accuracy is: " + str(highestKAccuracy))
