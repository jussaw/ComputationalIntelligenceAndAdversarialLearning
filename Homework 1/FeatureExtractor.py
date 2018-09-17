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
        if ord(letter) < 127 and ord(letter) >= 0:
            fileFeatureVector[ord(letter)] += 1

    # Close the file then return the fileFeatureVector
    file.close()

    # Remove the first 32 values of fileFeatureVector to match specs of assignment
    condensedFileFeatureVector = []
    for i in range(32,128):
        condensedFileFeatureVector.append(fileFeatureVector[i])

    return condensedFileFeatureVector

# Takes an input of a vector then returns the normalized version of that vector
def normalize(numVectorIn=None):
    # Create sum variable to keep up with the total sum of the values
    # and numVector which is equal to the input parameter
    sum = 0
    numVector = numVectorIn

    # Run through each value in numVector and add the square of each value to sum
    # then calculate the magnitude as such.
    # magnitude = sqrt(ssummation(num^2))
    for num in numVector:
        sum += (num**2)
    magnitude = math.sqrt(sum)

    # Run through each value in numVector and divide each by the magnitude
    i = 0
    for num in numVector:
        numVector[i] /= magnitude
        i += 1
    print ("Magnitude = " + str(magnitude))

    return numVector
