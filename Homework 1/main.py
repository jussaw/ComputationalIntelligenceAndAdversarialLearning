import os
import FeatureExtractor
import FileUtil

#Run web Crawler

#Find article names in folder
fileNames = FileUtil.getFileNames()

#Delete output file
if os.path.isfile("../Feature Vectors/output.txt"):
    os.remove("../Feature Vectors/output.txt")

for file in fileNames:
    fileArg = "../Articles/" + file
    fVector = FeatureExtractor.createFeatureVector(fileArg)
    FileUtil.writeFile(fVector, "output", file)
