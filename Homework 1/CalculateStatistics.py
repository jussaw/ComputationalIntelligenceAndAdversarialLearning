# Takes in an input of a feature vector
# Determines the number of senteces by calculating the total number
# of exclamation points, periods, and question marks.
# Returns the total number calculated
def calculateAmountOfSentences(featureVector=None):
    total = 0
    total += featureVector[33-32]
    total += featureVector[46-32]
    total += featureVector[63-32]

    return total

# Takes in an input of a feature vector.
# Determines the total number of characters by adding up all the values
# in the feature vector.
# Return the calculated total.
def calculateAmountOfChars(featureVector=None):
    total = 0
    for n in featureVector:
        total += n

    return total

# Takes in an input of feature vector.
# Determines the total number of words by calculating the number of spaces
# then adding 1.
# Returns that calculated total
def calculateAmountOfWords(featureVector=None):
    total = featureVector[32-32] + 1

    return total

# Takes in an input of total and number of feature vectors.
# Determines the average by dividing the the total by the number
# of feature vectors.
# Returns that average
def calculateAverage(total=None, numOfFeatureVectors=None):
    average = total / numOfFeatureVectors

    return average


def printTotals(featureVectorIn=None, fileName=None):
    print("File name: " + fileName)
    print("Char count: " + str(calculateAmountOfChars(featureVectorIn)))
    print("Word count: " + str(calculateAmountOfWords(featureVectorIn)))
    print("Sentence count: " + str(calculateAmountOfSentences(featureVectorIn)))
    print("\n")
