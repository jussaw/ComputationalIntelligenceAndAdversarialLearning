import GeneralRegressionNeuralNetwork
import FileUtil
import FeatureExtractor

hfs = [] # List for fire strengths
data = [] # List for feature vectors (training sets)
d = [] # List of desired output vectors
t = [] #queries
dq_i = [] #List for decision query output vectors

#Test run for first query
GeneralRegressionNeuralNetwork.append_vectors_to_t(data)
t = data[1:len(data)]
guess = data[0]
num = len(t)
GeneralRegressionNeuralNetwork.compute_outputs(t, data[0], hfs, d, num, dq_i)

print dq_i

#Grab the largest number for outputs
highest_num = -1
spot = -1
for i in range(len(dq_i)):
    if dq_i[i] > highest_num:
        highest_num = dq_i[i]
        spot = i


print "Highest Number: " + str(highest_num)
print "Spot: " + str(spot)
