import GeneralRegressionNeuralNetwork
import FileUtil
import FeatureExtractor

def computeAverageAccuracy(runs):
    count = 0
    for k in range(len(runs)):
        if (runs[k] == 1):
            count = count + 1

    accuracy = (count / len(runs)) * 100
    print "The Average Accuracy is: " + str(accuracy)

t = []

zenitz = GeneralRegressionNeuralNetwork.getAverageVector('Zenitz')
moody = GeneralRegressionNeuralNetwork.getAverageVector('Moody')
mcnair = GeneralRegressionNeuralNetwork.getAverageVector('Mcnair')
black = GeneralRegressionNeuralNetwork.getAverageVector('Black')
potter = GeneralRegressionNeuralNetwork.getAverageVector('Potter')
zenor = GeneralRegressionNeuralNetwork.getAverageVector('Zenor')

t.append(zenitz)
t.append(moody)
t.append(mcnair)
t.append(black)
t.append(potter)
t.append(zenor)

for i in range(len(t)):
    run = i + 1
    print "Performing run number " + str(run) + " with query of element: " + str(run)
    runs = []
    hfs = []
    d = []
    dq_i = []
    guess = t[i]
    num = len(t)
    highest = 0

    GeneralRegressionNeuralNetwork.compute_outputs(t, guess, hfs, d, num, dq_i)

    for j in range(len(dq_i)):
       if (dq_i[j] > highest):
           highest = dq_i[j]
           spot = j

    if (spot == i):
       runs.append(1)

computeAverageAccuracy(runs)
