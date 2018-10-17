import os.path
from os.path import isfile, join
from os import listdir

#Returns all of the file names in the articles directory.
def getFileNames(directory=None):
    #Create empty list of file names
    fileNames = []
    onlyfiles = [file for file in listdir(directory) if isfile(join(directory, file))]
    for f in onlyfiles:
        #Add the files to the file names list.
        fileNames.append(f)
    return fileNames

#Writes data to to the Feature Vector folder
#numVector:  Vector data to be written
#filename: Name of the file to create and write to
#title: Name of the article the data comes from (Will be included with the feature
#vector data that is being written.)
def writeFile(numVector=None, fileName=None, title=None):
    writePath = "../Feature Vectors/"
    titleWithoutExtension = title[:-4]

    #Save the complete path of the write path + filename
    completeName = os.path.join(writePath, fileName+".txt")
    with open(completeName, "a") as file:
        file.write(titleWithoutExtension + ",") #Write title of article
        for num in numVector: #Write feature vector data
            file.write(str(num))
            file.write(",")
        file.write("\n")
