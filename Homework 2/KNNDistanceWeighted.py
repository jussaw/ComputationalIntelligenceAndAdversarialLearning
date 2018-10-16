

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

    # Calculates the numerator (summation of the distance * weight)
    for i in range(k):
        distanceWeightSum += weight[i] * eucDistance(query, trainingData[i])

    # Calculates the denominator (summation of the weights)
    for i in range(k):
        weightSum += weight[i]

    # Calculates and returns output
    output = distanceWeightSum/weightSum
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
    weight = eucDistance(q, t_i)**(-1)
    return weight

# Returns the k closest data
def determineClosestData(k=int, query=[], trainingData=[[]]):
    sortedData = sortDistances(query, trainingData)
    closesData = sortedData[0:k]

    return closestData

# Sorts the training data in terms of their distanc to the query
def sortDistances(query=[], trainingDataIn=[[]]):
    trainingData = trainingDataIn
    sortedData = []

    while len(trainingData) > 0:
        #shortestDistanceData = trainingData[0]
        indexRemove = 0

        for i in range(1, len(trainingData)):
            if eucDistance(query, trainingData[i]) < eucDistance(query, trainingData[indexRemove]):
                #shortestDistanceData = trainingData[i]
                indexRemove = i

        #sortedData.append(shortestDistanceData)
        sortedData.append(trainingData[indexRemove])
        del trainingData[indexRemove]

    return sortedData
