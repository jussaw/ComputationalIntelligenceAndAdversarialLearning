from ElitistGeneticAlgorithm import *
from FileUtil import *
import random
from sklearn.model_selection import StratifiedKFold
from sklearn.preprocessing import StandardScaler, normalize
from sklearn import svm
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.model_selection import StratifiedKFold
from sklearn import preprocessing
import numpy as np
from sklearn.model_selection import cross_val_score
import Data_Utils

# print ("Hello world")

# dataSet = createFeatureVectors("../../Feature Vectors/output.txt")
# dataSet = createFeatureVectors("CASIS-25_CU.txt")
# #print(dataSet)
#
# individuals = createIndividuals()
# for individual in individuals:
#     print individual, "\n"
# print len(individuals)

#elitistGA(dataSet, 2)
###############################################################################
# dataSet = createFeatureVectors("../../Feature Vectors/output.txt")
# labels = []
#
# for i in range(len(dataSet)):
#     labels.append(dataSet[i].pop(0))
#
#
# print dataSet
# print labels
###############################################################################

# CU_X = dataSet
# Y = labels
#
# lsvm = svm.LinearSVC()
#
# skf = StratifiedKFold(n_splits=4, shuffle=True, random_state=0)
# fold_accuracy = []
#
# scaler = StandardScaler()
# tfidf = TfidfTransformer(norm=None)
# dense = Data_Utils.DenseTransformer()
#
# for train, test in skf.split(CU_X, Y):
#     #train split
#     CU_train_data = CU_X[train]
#     train_labels = Y[train]
#
#     #test split
#     CU_eval_data = CU_X[test]
#     eval_labels = Y[test]
#
#     # tf-idf
#     tfidf.fit(CU_train_data)
#     CU_train_data = dense.transform(tfidf.transform(CU_train_data))
#     CU_eval_data = dense.transform(tfidf.transform(CU_eval_data))
#
#     # standardization
#     scaler.fit(CU_train_data)
#     CU_train_data = scaler.transform(CU_train_data)
#     CU_eval_data = scaler.transform(CU_eval_data)
#
#     # normalization
#     CU_train_data = normalize(CU_train_data)
#     CU_eval_data = normalize(CU_eval_data)
#
#     train_data =  CU_train_data
#     eval_data = CU_eval_data
#
#     # evaluation
#     lsvm.fit(train_data, train_labels)
#
#     lsvm_acc = lsvm.score(eval_data, eval_labels)
#
#     fold_accuracy.append((lsvm_acc, rbfsvm_acc, mlp_acc))
#
# print(np.mean(fold_accuracy, axis = 0))
###############################################################################
# X = range(10)
# for x in range(10):
#     value = random.choice(X)
#     print value
#     X.remove(value)
#     print X
###############################################################################
# parent0 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# parent1 = [-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15]
#
# child1, child2 = uniformCrossover(parent0, parent1, 5)
#
# print (child1, len(child1))
# print (child2, len(child2))
###############################################################################
# parent1, parent2 = createFirstTwoParents(dataSet)
# print parent1
# print parent2
###############################################################################
# x = range(5)
# y = getAverage(x)
# print x
# print y
#
# print(y, "hi")
###############################################################################
X = range(1, 5001)
writeAccuraciesToFile("5000.txt", X)
