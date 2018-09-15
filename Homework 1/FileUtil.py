import os.path
from os.path import isfile, join
from os import listdir

def getFileNames():
    fileNames = []
    onlyfiles = [file for file in listdir("../Articles/") if isfile(join("../Articles/", file))]
    for f in onlyfiles:
        fileNames.append(f)
    return fileNames

def writeFile(numVector=None, fileName=None, title=None):
    writePath = "../Feature Vectors/"

    completeName = os.path.join(writePath, fileName+".txt")
    with open(completeName, "a") as file:
        file.write(title)
        file.write(",")
        for num in numVector:
            file.write(str(num))
            file.write(",")
        file.write("\n")
