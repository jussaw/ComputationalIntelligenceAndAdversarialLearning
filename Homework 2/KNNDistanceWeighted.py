

def KNN_Weighted_Distance(k=int, query=[], trainingData=[[]]):
    # Get k closest data sorted by distances
    closestKData = determineClosestData(k, query, trainingData)

    # Instantiate sum variables to 0
    weightSum = 0
    distanceWeightSum = 0

    # Calculate weights
    weights = []
    for i in range(k):
        weight = calculateWeight(query, closestKData[i])
        weights.append(weight)

    # Calculates the numerator (summation of (distance[i] * weight[i]))
    # Calculates the denominator (summation of the weights)
    for i in range(k):
        distanceWeightSum += weights[i] * eucDistance(query, closestKData[i])
        weightSum += weights[i]

    # Calculates and returns output
    output = distanceWeightSum/weightSum
    return output

def KNN_Weighted_Distance2(k=int, query=[], trainingData=[[]]):
    closestData = determineClosesData(k, query, trainingData)

    for data in closestData:
        pass

    return output

# Returns the Euclidean Distance between the two vectors
def eucDistance(q=[], t_i=[]):
    sum = 0
    for i in range(1, len(q)):
        sum += (q[i] - t_i[i])**2
    answer = sum**.5
    return answer

# Calculates the weight according to the KNN Distance Weighted
# specifications.
def calculateWeight(q=[], t_i=[]):
    if (eucDistance(q, t_i) == 0):
        return 0
    weight = eucDistance(q, t_i)**(-1)
    return weight

# Returns the k closest data
def determineClosestData(k=int, query=[], trainingData=[[]]):
    sortedData = sortDistances(query, trainingData)
    closestData = sortedData[0:k]

    return closestData

# Sorts the training data in terms of their distanc to the query
def sortDistances(query=[], trainingDataIn=[[]]):
    trainingData = trainingDataIn
    sortedData = []

    while len(trainingData) > 0:
        indexRemove = 0

        # This starts from 1 because the first element is the name of article
        for i in range(1, len(trainingData)):
            if eucDistance(query, trainingData[i]) < eucDistance(query, trainingData[indexRemove]):
                indexRemove = i

        sortedData.append(trainingData[indexRemove])
        del trainingData[indexRemove]

    return sortedData

def parseAuthor(featureVector=[]):
    featureInfo = featureVector[0]
    authorName = featureInfo.split('_')[1]
    return authorName
