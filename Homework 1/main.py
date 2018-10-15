import os
import FeatureExtractor
import FileUtil
import CalculateStatistics

# Find article names in folder
articlesDirectory = "../ArticlesEx/"
fileNames = FileUtil.getFileNames(articlesDirectory)
fileNames.sort()
print ("\nNumber of files = " + str(len(fileNames)) + "\n")

# Delete output files
if os.path.isfile("../Feature Vectors/output.txt"):
    os.remove("../Feature Vectors/output.txt")
if os.path.isfile("../Feature Vectors/outputNormalized.txt"):
    os.remove("../Feature Vectors/outputNormalized.txt")

# Create a feature vector and normalized feature vector for each
# file then write both vectors to their corresponding files.
# We also calculate the average number of chars, words, and sentences
# in the feature vectors.
numOfFeatureVectors = len(fileNames)
totalChars = 0.0
totalWords = 0.0
totalSentences = 0.0
for file in fileNames:
    # fileArg is set to directory of each files
    # fVector is feature vector of each file then it is written to file
    fileArg = articlesDirectory + file
    fVector = FeatureExtractor.createFeatureVector(fileArg)
    FileUtil.writeFile(fVector, "output", file)
    print "Wrote to ../FeatureVectors/output.txt"

    # Calculates the total number of chars, words, and sentences on
    # every iteration
    totalChars += CalculateStatistics.calculateAmountOfChars(fVector)
    totalWords += CalculateStatistics.calculateAmountOfWords(fVector)
    totalSentences += CalculateStatistics.calculateAmountOfSentences(fVector)

    # Prints the total chars, words, and sentences for each feature vector
    CalculateStatistics.printTotals(fVector, file)

    # fNormalizedVector is noramlized version of fileFeatureVector
    # Then we write it to the normalized feature vector file
    fNormalizedVector = FeatureExtractor.normalize(fVector)
    FileUtil.writeFile(fNormalizedVector, "outputNormalized", file)


# Calculates the average number of chars, words, and sentences.
averageChars = CalculateStatistics.calculateAverage(totalChars, numOfFeatureVectors)
averageWords = CalculateStatistics.calculateAverage(totalWords, numOfFeatureVectors)
averageSentences = CalculateStatistics.calculateAverage(totalSentences, numOfFeatureVectors)


# Prints the average number of chars, words, and sentences.
print("Average amount of chararacters = " + str(averageChars))
print("Average amount of words = " + str(averageWords))
print("Average amount of sentences = " + str(averageSentences))
<<<<<<< HEAD
print "Wrote to ../FeatureVectors/outputNormalized.txt"
=======
<<<<<<< HEAD
print("")
=======
=======
    print "Wrote to ../FeatureVectors/outputNormalized.txt"
>>>>>>> 02d54e926cd60aef82836b0b09948d266203167f
>>>>>>> f915941d8decb875a3dcc15c1423ddde260d28ef
>>>>>>> 19511e3ccdb2deebb1fa57d102ba38c796af4039
