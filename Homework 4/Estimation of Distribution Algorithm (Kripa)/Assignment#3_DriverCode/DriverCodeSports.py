import Data_Utils
from sklearn.model_selection import StratifiedKFold
from sklearn.preprocessing import StandardScaler, normalize
from sklearn import svm
from sklearn.neural_network import MLPClassifier
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.model_selection import StratifiedKFold
from sklearn import preprocessing
import numpy as np
import operator
import random
from sklearn.model_selection import cross_val_score


def geneticAlgorithms(CU_X, Y):
    rbfsvm = svm.SVC()
    lsvm = svm.LinearSVC()
    mlp = MLPClassifier(max_iter=2000)
    skf = StratifiedKFold(n_splits=4, shuffle=True, random_state=0)
    fold_accuracy = []
    scaler = StandardScaler()
    tfidf = TfidfTransformer(norm=None)
    dense = Data_Utils.DenseTransformer()
    for train, test in skf.split(CU_X, Y):
        CU_train_data = CU_X[train]
        train_labels = Y[train]

    # test split
    CU_eval_data = CU_X[test]
    eval_labels = Y[test]

    # tf-idf
    tfidf.fit(CU_train_data)
    CU_train_data = dense.transform(tfidf.transform(CU_train_data))
    CU_eval_data = dense.transform(tfidf.transform(CU_eval_data))

    # standardization
    scaler.fit(CU_train_data)
    CU_train_data = scaler.transform(CU_train_data)
    CU_eval_data = scaler.transform(CU_eval_data)

    # normalization
    CU_train_data = normalize(CU_train_data)
    CU_eval_data = normalize(CU_eval_data)

    train_data = CU_train_data
    eval_data = CU_eval_data

    # evaluation
    rbfsvm.fit(train_data, train_labels)
    lsvm.fit(train_data, train_labels)
    mlp.fit(train_data, train_labels)

    rbfsvm_acc = rbfsvm.score(eval_data, eval_labels)
    lsvm_acc = lsvm.score(eval_data, eval_labels)
    mlp_acc = mlp.score(eval_data, eval_labels)

    fold_accuracy.append((lsvm_acc, rbfsvm_acc, mlp_acc))

    return np.mean(fold_accuracy[0], axis=0)


main_indList = []
alpha = 0.05
def genParents():
    for i in range(25):
        individual = np.random.choice([0, 1], size=(95,), p=[1. / 3, 2. / 3])
        name = "ind_" + str(i)
        ind_0 = individual.tolist()
        ind_list = []
        ind_list.append(name)
        CU_X, Y = Data_Utils.Get_Casis_CUDataset()
        CU_X = CU_X * ind_0
        fitness = geneticAlgorithms(CU_X, Y)
        ind_list.append(fitness)
        ind_list.append(ind_0)
        main_indList.append(ind_list)
    main_indList_sorted = sorted(main_indList, key=lambda x: x[1], reverse=True)
    return main_indList_sorted

#childrenFitness
def genChildrenPopAndFitness(children, alpha):
    #mutation
    main_child_list=[]
    for i in range(25):
        for j in range(95):
            if random.uniform(0, 1)<= alpha:
                num = children[i][j]
                children[i][j] = np.logical_not(num).astype(int)

    for i in range(25):
        child_list=[]
        name = "child_" + str(i)
        CU_X, Y = Data_Utils.Get_Casis_CUDataset()
        CU_X = CU_X * children[i]
        fitness = geneticAlgorithms(CU_X,Y)
        child_list.append(name)
        child_list.append(fitness)
        child_list.append(children[i])
        main_child_list.append(child_list)
    main_child_list_sorted = sorted(main_child_list, key=lambda x: x[1], reverse=True)
    return main_child_list_sorted

# crossover

# print(main_indList_sorted[0][2])
#childCreationWithoutFitness
def generatePopulation(main_indList_sorted):
    parents = []
    top_parent = []
    for j in range(0, 13):
        if j != 0:
            parents.append(main_indList_sorted[j][2])
        else:
            top_parent.append(main_indList_sorted[j][2])

    children = []
    # crossover
    for i in range(0, 24):
        children_sub = []
        for j in range(95):
            op = []
            op.append(j)
            my_items = operator.itemgetter(*op)
            op_list = [my_items(x) for x in parents]
            children_sub.append(random.choice(op_list))
            if j == 94:
                 children.append(children_sub)
    children.insert(0, top_parent[0])
    return children

'''
sortedList = genParents()
initialChild = generatePopulation(sortedList) 
child_new = genChildrenPopAndFitness(initialChild)
'''
recordAccuracies = []
def main(alpha):
    sortedList = genParents()
    for j in range(207):
        print("Generation"+str(j))
        if j == 0:
            intChildren = generatePopulation(sortedList)
            fitness = genChildrenPopAndFitness(intChildren, alpha)
            newParent = fitness

        proChildren = generatePopulation(newParent)
        fitness = genChildrenPopAndFitness(proChildren, alpha)
        newParent = fitness
        if j == 206:
            op = []
            op.append(1)
            my_items = operator.itemgetter(*op)
            op_list = [my_items(x) for x in newParent]
            recordAccuracies.append(np.mean(op_list))
            print(recordAccuracies)

def cycle(type):
    if type =="baseline":
       main(0.05)
    else:
        main(0.03)

print ("baseline")
cycle("baseline")
print("innovation")
cycle("innovation=")
print(np.mean(recordAccuracies))