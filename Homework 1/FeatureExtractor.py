import math
ourFileName = "../Articles/1000_1.txt"

def createFeatureVector(fileName=None):
    file = open(fileName, "r")
    fileBody = file.read()#.lower()
    fileFeatureVector = [0] * 128

    for letter in fileBody:
        fileFeatureVector[ord(letter)] = fileFeatureVector[ord(letter)] + 1
        print letter

    i = 0
    for num in fileFeatureVector:
        print(chr(i) + " - " + str(num))
        #print(str(i) + " - " + str(num))
        i = i + 1
    #print fileBody
    return fileFeatureVector


def normalize(numVectorIn=None):
    sum = 0
    numVector = numVectorIn
    for num in numVector:
        sum = sum + (num**2)
    magnitude = math.sqrt(sum)
    i = 0
    for num in numVector:
        numVector[i] = num / magnitude
        i = i + 1

    return numVector




createFeatureVector(ourFileName)
