from KNNDistanceWeighted import *
from FileUtil import *

# totalCorrect = 0
# vecs = createFeatureVectors("../Feature Vectors/output.txt")
# totalVecs = len(vecs)
# k = 1
# for j in range(totalVecs):
#     totalCorrect = 0
#     for i in range(totalVecs):
#         vec = vecs[i]
#
#         correctAuthor = parseAuthor(vec)
#         predictedAuthor = KNN_Weighted_Distance(k, vec, vecs)
#
#
#         if correctAuthor == predictedAuthor:
#             totalCorrect += 1
#         vecs = createFeatureVectors("../Feature Vectors/output.txt")
#
#     percentageCorrect = totalCorrect / totalVecs
#     print("Percentage Correct when k is " + str(k) +
#         " on non-normalized set = " + str(percentageCorrect * 100) + "%")
#     k += 1
#
# k = 0
# totalCorrect = 0
# vecsNorm = createFeatureVectors("../Feature Vectors/outputNormalized.txt")
# totalVecs = len(vecsNorm)
#
# k = 1
#
# for j in range(totalVecs):
#     totalCorrect = 0
#     for i in range(totalVecs):
#         vec = vecsNorm[i]
#
#         correctAuthor = parseAuthor(vec)
#         predictedAuthor = KNN_Weighted_Distance(k, vec, vecsNorm)
#
#         vecsNorm = createFeatureVectors("../Feature Vectors/outputNormalized.txt")
#
#         if correctAuthor == predictedAuthor:
#             totalCorrect += 1
#
#     percentageCorrect = totalCorrect / totalVecs
#     print("Percentage Correct when k is " + str(k) +
#         " on normalized set = " + str(percentageCorrect * 100) + "%")
#     k += 1

x = ['J', 0, 1]
y = ['J', 1, 2]
print(manDistance(x, y))
