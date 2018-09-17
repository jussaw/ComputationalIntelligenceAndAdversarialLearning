import os
import FeatureExtractor
import FileUtil

#Run web Crawler

#Find article names in folder
fileNames = FileUtil.getFileNames()

#Delete output files
if os.path.isfile("../Feature Vectors/output.txt"):
    os.remove("../Feature Vectors/output.txt")
if os.path.isfile("../Feature Vectors/outputNormalized.txt"):
    os.remove("../Feature Vectors/outputNormalized.txt")

# Create a feature vector and normalized feature vector for each
# file then write both vectors to their corresponding files.
for file in fileNames:
    # fileArg is set to directory of each files
    # fVector is feature vector of each file then it is written to file
    fileArg = "../Articles/" + file
    fVector = FeatureExtractor.createFeatureVector(fileArg)
    FileUtil.writeFile(fVector, "output", file)

    # fNormalizedVector is noramlized version of fileFeatureVector
    # Then we write it to the normalized feature vector file
    fNormalizedVector = FeatureExtractor.normalize(fVector)
    FileUtil.writeFile(fNormalizedVector, "outputNormalized", file)
