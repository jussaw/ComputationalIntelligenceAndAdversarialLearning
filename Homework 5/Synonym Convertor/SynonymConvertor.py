import nltk
import FileUtil as FU
from nltk.corpus import wordnet as wn
import random

def main():
    badWords = [".", ",", "!", "\'", "\"", "?", "a", "the", "an", "and", "to",
        "now", "in"]

    inputFileName0 = "Moody_wk6_Finished"
    inputFileName = "articles/" + inputFileName0 + ".txt"
    outputFileName = "output/" + inputFileName0 + "_Synonyms.txt"
    linesOriginal = FU.readFile(inputFileName)
    lines = []

    for line in linesOriginal:
        lines.append(removeNonAscii(line))

    outputLines = []

    for line in lines:
        replaceIndexes = []
        i = 0
        for word in line.split():
            wordInvalid = False
            for badWord in badWords:
                if word == badWord:
                    wordInvalid == True

            if wordInvalid == False:
                replaceIndexes.append(i)

            i += 1

        if len(replaceIndexes) > 0:
            indexToReplace = random.choice(replaceIndexes)
            lineArr = line.split()
            lineArr[indexToReplace] = getBestSynonym(lineArr[indexToReplace])
            line = " ".join(lineArr)
        outputLines.append(line)

    tokensArray = makeTokensArray(outputLines)

    writeToFile(outputLines, outputFileName)

def makeTokensArray(lines):
    tokensArray = []

    for line in lines:
        tokensArray.append(nltk.word_tokenize(removeNonAscii(line)))

    return tokensArray

def removeNonAscii(s):
    output = ""
    for i in s:
        if isinstance(i, str) and ord(i) < 128:
            output += i
    return output


def replaceWithSynonym(tokensArray):
    pass

def unTokenize(tokensArray):
    outputArray = []
    for tokens in tokensArray:
        output = ""
        for token in tokens:
            output += token + " "
        outputArray.append(output)

    return outputArray

def getBestSynonym(word):
    synonyms = []
    for syn in wn.synsets(word):
        for l in syn.lemmas():
            synonyms.append(l.name())

    if len(set(synonyms)) > 0:
        bestSynonym = set(synonyms).pop()
        return bestSynonym

    return word

def writeToFile(lines, fileName):
    with open(fileName, "w") as file:
        # file.writelines(lines)
        for line in lines:
            file.write("\n" + line)
