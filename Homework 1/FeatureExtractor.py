import math

# Takes an input of a file name (string) then return the character unigram
# feature vector
def createFeatureVector(fileName=None):
    # If fileName is not a string then return error message
    if not isinstance(fileName, str):
        return "ERROR: fileName is not a string"

    # Open the file and set the body that file to a string
    # Create a int array with 128 0's to keep track of the count of each number
    file = open(fileName, "r")
    fileBody = file.read()#.lower()
    fileFeatureVector = [0] * 128

    # Check what each character is in the string then increment
    # that index in fileFeatureVector
    for letter in fileBody:
        fileFeatureVector[ord(letter)] += 1
        #print letter

    # Runs through each item in the fileFeatureVector and print how many
    # of each character was recorded
    i = 0
    for num in fileFeatureVector:
        print(chr(i) + " - " + str(num))
        #print(str(i) + " - " + str(num))
        i += 1

    # Close the file then return the fileFeatureVector
    file.close()
    return fileFeatureVector

# Takes an input of a vector then returns the normalized version of that vector
def normalize(numVectorIn=None):
    sum = 0
    numVector = numVectorIn

    for num in numVector:
        sum += (num**2)
    magnitude = math.sqrt(sum)

    i = 0
    for num in numVector:
        numVector[i] = num / magnitude
        i += 1

    return numVector

def termFrequency(numVectorIn=None):
    numVector = numVectorIn
    sum = 0
    for num in numVector:
        sum += num

    i = 0
    for num in numVector:
        frequency = num / sum
        numVector[i] = frequency
        print (chr(i) + " - " + str(frequency))
        i += 1

    return numVector;


ourFileName = "../Articles/1000_1.txt"
featureVector = createFeatureVector(ourFileName)
normalizedVector = normalize(featureVector)

for num in normalizedVector:
    print num

#frequencyVector = termFrequency(featureVector)
