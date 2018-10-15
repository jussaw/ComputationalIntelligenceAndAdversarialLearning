import FileUtil
import FeatureExtractor

################## Notes #####################
# What is tq_0, t_q, and t_i?
# How do you obtan the desired output vectors?
##############################################

hfs = [] # List for fire strengths
t = [] # List for feature vectors
dq_0 = [] #List for output vectors
sigma = 4.796 #d_max

# Reads a list of file names, opens the files, and creates the appropriate
# feature vectors.
def append_vectors_to_t():
    #Get file names
    articlesDirectory = "../ArticlesExamples/"
    fileNames = FileUtil.getFileNames(articlesDirectory)

    #Create feature Vectors
    numOfFeatureVectors = len(fileNames)
    for file in fileNames:
        # fileArg is set to directory of each files
        # fVector is feature vector of each file then it is written to file
        fileArg = articlesDirectory + file
        fVector = FeatureExtractor.createFeatureVector(fileArg)
        t.append(fVector) #Append feature vectors to t.


# Compute the final outputs for the General Refression Neural Networks.
def compute_outputs(t, sigma): #Denoted as dq
  for i in range(0, len(t)):
    hfs.append(hf(tq_0, t[i], sigma))   # Compute  the kernels

  for i in range(0, len(t)):
    for j in range(0, len(dq_0)):
        dq_0[i] += hfs[i] * d[i][j] #First summation Unit

  sum_hfs = 0

  for i in range(0, len(t)):
        sum_hfs += hfs[i] #Second summation unit
        for j in range(0, 3):
            dq_0[j] = dq_0[j] / sum_hfs #Output vector in decicmal form


# Euclidean Distance Squared
def dist_sqrd(t_q, t_i):
    sum = 0.0
    for i in range(0, len(t_q)):
        sum += math.pow((t_q[i] - t_i[i]), 2.0)
    return sum


# Gaussian Kernel - (Denoted as hf in the noees)
def hf(t_q,t_i,sigma):
    return math.exp(-dist_sqrd(t_q, t_i) / pow((2.0 * sigma), 2.0))
