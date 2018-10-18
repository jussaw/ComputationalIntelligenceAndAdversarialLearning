import FileUtil
import FeatureExtractor
import math

################## Notes #####################
# What is tq_0, t_q, and t_i?
# How do you obtan the desired output vectors?
##############################################

sigma = 3.5 #d_max
numOfFeatureVectors = 0

def getAverageVector(author):
    x = []

    articlesDirectory = "../Articles/"
    fileNames = FileUtil.getFileNames(articlesDirectory)

    for file in fileNames:
        if (author in file):
            fileArg = articlesDirectory + file
            fVector = FeatureExtractor.createFeatureVector(fileArg)
            fVectorNormalized = FeatureExtractor.normalize(fVector)
            x.append(fVectorNormalized)

    sumElement = 0
    avgVector = []
    for i in range(len(x[0])):
        for j in range(len(x)):
            sumElement += x[j][i]
        avgVector.append(sumElement/len(x[0]))
    return avgVector

# Compute the final outputs for the General Refression Neural Networks for some
# query tq_i.
# tq_i: query
# t: list of training sets
def compute_outputs(t, tq_i, hfs, d, numSpots, dq_i): #Denoted as dq
  result = 0
  numOfFeatureVectors = len(t)
  compute_desired_output_vectors(d, numSpots)

  for i in range(0, len(t)):
    hfs.append(hf(tq_i, t[i], sigma))   # Compute  the kernels for each training instance with query tq_i

  for i in range(0, len(t)):
    result = 0
    for j in range(0, len(t)):
        result += hfs[i] * d[i][j] #First summation Unit
    dq_i.append(result)

  sum_hfs = 0.0

  for i in range(0, len(t)):
    sum_hfs += hfs[i] #Second summation unit

  for j in range(0, len(t)):
    dq_i[j] = dq_i[j] / sum_hfs

# Reads a list of file names, opens the files, and creates the appropriate
# feature vectors.
def append_vectors_to_t(t):
    #Get file names
    articlesDirectory = "../Articles/"
    fileNames = FileUtil.getFileNames(articlesDirectory)

    #Create feature Vectors
    numOfFeatureVectors = len(fileNames)
    for file in fileNames:
        # fileArg is set to directory of each files
        # fVector is feature vector of each file then it is written to file
        fileArg = articlesDirectory + file
        fVector = FeatureExtractor.createFeatureVector(fileArg)
        fVectorNormalized = FeatureExtractor.normalize(fVector)
        t.append(fVectorNormalized) #Append feature vectors to t.

# Create a vector initialized with "numSpots" 0s.
def create_empty_vectors(numSpots):
    vector = [0] * numSpots
    return vector

# Create desired output vectors.
def compute_desired_output_vectors(d, numSpots):
    #Create an empty vector for how many training sets you have.
    for i in range(0, numSpots):
        d.append(create_empty_vectors(numSpots))

    #Mark the appropriate spot in the desired output vector with a 1.
    for j in range(0, len(d)):
        for k in range(0, len(d)):
            if (k == j):
                d[j][k] = 1

# Euclidean Distance Squared
def dist_sqrd(t_q, t_i):
    sum = 0.0
    for i in range(0, len(t_q)):
        sum += math.pow((t_q[i] - t_i[i]), 2.0)
    return sum

# Gaussian Kernel - (Denoted as hf in the noees)
def hf(t_q,t_i,sigma):
    return math.exp(-dist_sqrd(t_q, t_i) / pow((2.0 * sigma), 2.0))
