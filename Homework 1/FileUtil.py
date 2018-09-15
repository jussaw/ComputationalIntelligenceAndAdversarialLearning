import os.path

def writeFile(numVector=None, fileName=None):
    writePath = "../Feature Vectors/"

    completeName = os.path.join(writePath, fileName+".txt")
    with open(completeName, "w") as file:
        file.write(fileName)
        file.write(",")
        for num in numVector:
            file.write(str(num))
            file.write(",")
