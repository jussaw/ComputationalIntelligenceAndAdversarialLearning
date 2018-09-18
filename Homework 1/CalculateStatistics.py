

def calculateAmountOfSentences(featureVector=None):
    total = 0
    total += featureVector[33-32]
    print ("num of ! = " + str(featureVector[33-32]))
    total += featureVector[46-32]
    print ("num of . = " + str(featureVector[46-32]))
    total += featureVector[63-32]
    print ("num of ? = " + str(featureVector[63-32]))

    return total


def calculateAmountOfChars(featureVector=None):
    total = 0
    for n in featureVector:
        total += n

    return total


def calculateAmountOfWords(featureVector=None):
    total = featureVector[32-32] + 1
    return total


def calculateAverage(total, numOfFeatureVectors):
    return total / numOfFeatureVectors
