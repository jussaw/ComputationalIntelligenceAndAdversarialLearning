import Data_Utils
from sklearn.model_selection import StratifiedKFold
from sklearn.preprocessing import StandardScaler, normalize
from sklearn import svm
from sklearn.neural_network import MLPClassifier
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.model_selection import StratifiedKFold
from sklearn import preprocessing
import numpy as np
from sklearn.model_selection import cross_val_score
from FileUtil import *
import random

def main():
    # Code from driver
    lsvm = svm.LinearSVC()

    skf = StratifiedKFold(n_splits=4, shuffle=True, random_state=0)
    fold_accuracy = []

    scaler = StandardScaler()
    #tfidf = TfidfTransformer(norm=none)
    dense = Data_Utils.DenseTransformer()

    # Dataset
    dataSet = createFeatureVectors("../../Feature Vectors/output.txt")

    # Determin authors
    authors = getAuthors(dataSet)

    # Split test and training data
    trainingSet, testSet = splitData(dataSet, .25)

    



def getAuthors(dataSet):
    authors = []
    for data in dataSet:
        author = data[0].split('_')[1].lower()
        if author not in authors:
            authors.append(author)
    return authors


def splitData(dataSet, percentSizeTest):
    trainingSet = dataSet[:]
    testSet = []
    numOfTestSet = int(len(trainingSet) * percentSizeTest)
    for i in range(numOfTestSet):
        elementToRemove = random.randint(0, len(trainingSet) - 1)
        testSet.append(trainingSet.pop(elementToRemove))
    return trainingSet, testSet
