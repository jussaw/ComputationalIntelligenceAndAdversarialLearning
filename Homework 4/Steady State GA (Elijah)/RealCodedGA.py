import SteadyStateAlgorithm
import FeatureExtractor
from sklearn import svm
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error

import GeneralRegressionNeuralNetwork
import FileUtil
import FeatureExtractor

def meansquared(arr1, arr2):
    res = []
    for j in range(len(arr1)):
        a = arr1[j] - arr2[j]
        res.append(a)
    return res

error_rates = []
fitness_scores = []
accuracies = []

post_fitness_scores = []
post_error_rates = []

set_labels = []

target1_vector = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]

target2_vector = [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

target3_vector = [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]

lsvm = svm.LinearSVC()

zenitz = GeneralRegressionNeuralNetwork.getAverageVector('Zenitz')
moody = GeneralRegressionNeuralNetwork.getAverageVector('Moody')
mcnair = GeneralRegressionNeuralNetwork.getAverageVector('Mcnair')
black = GeneralRegressionNeuralNetwork.getAverageVector('Black')
potter = GeneralRegressionNeuralNetwork.getAverageVector('Potter')
zenor = GeneralRegressionNeuralNetwork.getAverageVector('Zenor')

setlabels = ['zenitz', 'Moody', 'Mcnair', 'Black', 'Potter', 'Zenor']

#Retrieve all feature vectors
feature_vectors = SteadyStateAlgorithm.createFeatureVectors("../Feature Vectors/outputNormalized.txt")
#feature_vectors = SteadyStateAlgorithm.createFeatureVectors("CASIS-25_CU.txt")

#Retrieve training set of random 25 population
original_training_set = SteadyStateAlgorithm.getPopulationOfRandom25(feature_vectors);

#Retrieve feature mask
feature_mask = SteadyStateAlgorithm.generateFeatureMask();
#print feature_mask

for j in range(25):
    label = original_training_set[j][0]
    set_labels.append(label)

################## Get fitness scores for all 25 #################
for i in range(25):
    #Retrieve NEW training set
    curr_mask = feature_mask[i]
    new_training_set = SteadyStateAlgorithm.generateNewTrainingSet(curr_mask, original_training_set);
    set_data = new_training_set

    lsvm.fit(set_data, set_labels)
    #Send it to learner to get fitness
    accuracies.append(lsvm.score(set_data, set_labels)) #EXECUTE LEARNER INSIDE

################## Run Steady State 4975 Times - Not sure what is supposed to happen here ###################
iterations = 0
iterations_plot = []
accuracies_plot = []
while (iterations <= 10):
    #Send new training set to learner and retrieve fitness score(accuracy) and error_rate
    # Retrieve child
    child = SteadyStateAlgorithm.steadyStateAlgorithm(feature_mask, accuracies)
    #Calculate fitness
    child_prime = SteadyStateAlgorithm.generateNewTrainingSet(child, original_training_set);


    dec_func = lsvm.decision_function(child_prime)
    pred = lsvm.predict(child_prime)
    new_vec = meansquared(dec_func[0], target1_vector)
    use_vec = []

    for j in range(len(new_vec)):
        use_vec.append(new_vec[j])

    accuracies_plot.append(use_vec)
    iterations_plot.append(iterations)

    iterations = iterations + 1

plt.plot(iterations_plot, accuracies_plot)
plt.show()

iterations = 0
iterations_plot = []
accuracies_plot = []
while (iterations <= 10):
    #Send new training set to learner and retrieve fitness score(accuracy) and error_rate
    # Retrieve child
    child = SteadyStateAlgorithm.steadyStateAlgorithm(feature_mask, accuracies)
    #Calculate fitness
    child_prime = SteadyStateAlgorithm.generateNewTrainingSet(child, original_training_set);


    dec_func = lsvm.decision_function(child_prime)
    pred = lsvm.predict(child_prime)
    new_vec = meansquared(dec_func[0], target2_vector)
    use_vec = []

    for j in range(len(new_vec)):
        use_vec.append(new_vec[j])

    accuracies_plot.append(use_vec)
    iterations_plot.append(iterations)

    iterations = iterations + 1

plt.plot(iterations_plot, accuracies_plot)
plt.show()

iterations = 0
iterations_plot = []
accuracies_plot = []
while (iterations <= 10):
    #Send new training set to learner and retrieve fitness score(accuracy) and error_rate
    # Retrieve child
    child = SteadyStateAlgorithm.steadyStateAlgorithm(feature_mask, accuracies)
    #Calculate fitness
    child_prime = SteadyStateAlgorithm.generateNewTrainingSet(child, original_training_set);


    dec_func = lsvm.decision_function(child_prime)
    pred = lsvm.predict(child_prime)
    new_vec = meansquared(dec_func[0], target3_vector)
    use_vec = []

    for j in range(len(new_vec)):
        use_vec.append(new_vec[j])

    accuracies_plot.append(use_vec)
    iterations_plot.append(iterations)

    iterations = iterations + 1

plt.plot(iterations_plot,accuracies_plot)
plt.show()
