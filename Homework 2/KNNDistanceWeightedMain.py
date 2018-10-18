from KNNDistanceWeighted import *
from FileUtil import *

totalCorrect = 0
vecs = createFeatureVectors("../Feature Vectors/output.txt")
totalVecs = len(vecs)
k = 1
for j in range(totalVecs):
    totalCorrect = 0
    totalRuns = 0
    for i in range(totalVecs):
        vec = vecs[i]
        del vecs[i]
        correctAuthor = parseAuthor(vec)
        predictedAuthor = KNN_Weighted_Distance(k, vec, vecs)


        if correctAuthor == predictedAuthor:
            totalCorrect += 1
        vecs = createFeatureVectors("../Feature Vectors/output.txt")
        totalRuns += 1

    percentageCorrect = totalCorrect / totalRuns
    print("Percentage Correct when k is " + str(k) +
        " on non-normalized set = " + str(percentageCorrect * 100) + "%")
    k += 1

totalCorrect = 0
vecsNorm = createFeatureVectors("../Feature Vectors/outputNormalized.txt")
totalVecs = len(vecsNorm)
k = 1

for j in range(totalVecs):
    totalCorrect = 0
    totalRuns = 0
    for i in range(totalVecs):
        vec = vecsNorm[i]
        del vecsNorm[i]
        correctAuthor = parseAuthor(vec)
        predictedAuthor = KNN_Weighted_Distance(k, vec, vecsNorm)


        if correctAuthor == predictedAuthor:
            totalCorrect += 1
        vecsNorm = createFeatureVectors("../Feature Vectors/outputNormalized.txt")
        totalRuns += 1

    percentageCorrect = totalCorrect / totalRuns
    print("Percentage Correct when k is " + str(k) +
        " on normalized set = " + str(percentageCorrect * 100) + "%")
    k += 1
