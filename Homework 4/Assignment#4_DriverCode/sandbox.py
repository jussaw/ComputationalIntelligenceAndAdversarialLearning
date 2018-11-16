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

title = "247Sports_McNair_ALAvsARK_wk6"

brokenTitle = title.split('_')

print brokenTitle[1]


a = range(5)
b = a[:]
del b[0]

print a
print b

for _ in range(25):
    print random.randint(0,2)
