import os.path
from os.path import isfile, join
from os import listdir

def getFileNames(directory=None):
    fileNames = []
    onlyfiles = [file for file in listdir(directory) if isfile(join("../Articles/", file))]
    for f in onlyfiles:
        fileNames.append(f)
    return fileNames

def writeFile(numVector=None, fileName=None, title=None):
    writePath = "../Feature Vectors/"
    titleWithoutExtension = title[:-4]

    completeName = os.path.join(writePath, fileName+".txt")
    with open(completeName, "a") as file:
        file.write(titleWithoutExtension + ",")
        for num in numVector:
            file.write(str(num))
            file.write(",")
        file.write("\n")
