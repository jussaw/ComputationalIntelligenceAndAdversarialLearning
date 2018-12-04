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
import matplotlib.pyplot as mpl
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import cross_val_score

f = open("data2.txt", "w")

graphFitness = []
def geneticAlgorithms(CU_X, Y):
    d = dict()
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

    decisionFunc = lsvm.decision_function(CU_train_data)
    authorCount = len(decisionFunc[0])
    #print(decisionFunc)
    target = -1 * np.ones(authorCount)
    target[2] = 1
    target[3] = 1
    target[5] = 1
    #print (decisionFunc[0])
    #f.write(mean_squared_error(decisionFunc[0], target))
   # print(mean_squared_error(decisionFunc[0], target))
    val = mean_squared_error(decisionFunc[0], target)
    graphFitness.append(val)
    f.write(str(val)+"\n")
    d["graphFit"] = graphFitness
    #print(lsvm.predict(CU_train_data))

    rbfsvm_acc = rbfsvm.score(eval_data, eval_labels)
    lsvm_acc = lsvm.score(eval_data, eval_labels)
    mlp_acc = mlp.score(eval_data, eval_labels)

    fold_accuracy.append((lsvm_acc, rbfsvm_acc, mlp_acc))
    mean = np.mean(fold_accuracy[0], axis=0)
    d["mean"] = mean
    return d


main_indList = []
alpha = 0.05
popSize = 25
def genParents():
    for i in range(popSize):
        individual = np.random.choice([0, 1], size=(95,), p=[1. / 3, 2. / 3])
        name = "ind_" + str(i)
        ind_0 = individual.tolist()
        ind_list = []
        ind_list.append(name)
        CU_X, Y = Data_Utils.Get_Casis_CUDataset()
        CU_X = CU_X * ind_0
        fit = geneticAlgorithms(CU_X, Y)
        fitness = fit["mean"]
        ind_list.append(fitness)
        ind_list.append(ind_0)
        main_indList.append(ind_list)
    main_indList_sorted = sorted(main_indList, key=lambda x: x[1], reverse=True)
    return main_indList_sorted

#childrenFitness
def genChildrenPopAndFitness(children, alpha, key):
    #mutation
    main_child_list=[]
    for i in range(popSize):
        for j in range(95):
            if random.uniform(0, 1)<= alpha:
                num = children[i][j]
                children[i][j] = np.logical_not(num).astype(int)

    for i in range(popSize):
        child_list=[]
        name = "child_" + str(i)
        CU_X, Y = Data_Utils.Get_Casis_CUDataset()
        CU_X = CU_X * children[i]
        fit = geneticAlgorithms(CU_X,Y)
        fitness = fit["mean"]
        if key == 206 and i== popSize -1:
            ran = range(0,len(fit["graphFit"]))
            plotGraphs(ran,fit["graphFit"])
        child_list.append(name)
        child_list.append(fitness)
        child_list.append(children[i])
        main_child_list.append(child_list)
    main_child_list_sorted = sorted(main_child_list, key=lambda x: x[1], reverse=True)
    return main_child_list_sorted

# crossover

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
    for i in range(0, popSize - 1):
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


recordAccuracies = []
def main(alpha):
    sortedList = genParents()
    for j in range(207):
        print("Generation"+str(j))
        key = j
        if j == 0:
            intChildren = generatePopulation(sortedList)
            fitness = genChildrenPopAndFitness(intChildren, alpha, key = 0)
            newParent = fitness

        proChildren = generatePopulation(newParent)
        fitness = genChildrenPopAndFitness(proChildren, alpha, key)

        newParent = fitness
        if j == 206:
            op = []
            op.append(1)
            my_items = operator.itemgetter(*op)
            op_list = [my_items(x) for x in newParent]
            recordAccuracies.append(np.mean(op_list))
            with open('data2.txt') as infile:
                print("comes here")
                v = infile.read()
                print(v)

def plotGraphs(xArray, yArray):
    mpl.plot(xArray, yArray)
    mpl.show()


main(0.03)