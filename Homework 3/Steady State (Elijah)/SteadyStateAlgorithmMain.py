import SteadyStateAlgorithm
import FeatureExtractor
from sklearn import svm
import matplotlib.pyplot as plt

error_rates = []
fitness_scores = []
accuracies = []

post_fitness_scores = []
post_error_rates = []

set_labels = []

lsvm = svm.LinearSVC()

#Retrieve all feature vectors
#feature_vectors = SteadyStateAlgorithm.createFeatureVectors("../Feature Vectors/outputNormalized.txt")
feature_vectors = SteadyStateAlgorithm.createFeatureVectors("CASIS-25_CU.txt")

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
    print "Current Mask: " + str(curr_mask)
    new_training_set = SteadyStateAlgorithm.generateNewTrainingSet(curr_mask, original_training_set);
    set_data = new_training_set

    lsvm.fit(set_data, set_labels)
    #Send it to learner to get fitness
    accuracies.append(lsvm.score(set_data, set_labels)) #EXECUTE LEARNER INSIDE

print "Accuracies: " + str(accuracies)
sum = 0
for i in range(len(accuracies) - 1):
    sum  = sum + accuracies[i]

avg = (sum / len(accuracies))
print "avg: " + str(avg)


################## Run Steady State 4975 Times - Not sure what is supposed to happen here ###################
iterations = 0
iterations_plot = []
accuracies_plot = []
while (iterations <= 4975):
    #Send new training set to learner and retrieve fitness score(accuracy) and error_rate
    # Retrieve child
    child = SteadyStateAlgorithm.steadyStateAlgorithm(feature_mask, accuracies)

    #Calculate fitness
    child_prime = SteadyStateAlgorithm.generateNewTrainingSet(child, original_training_set);

    child_accuracy = lsvm.score(child_prime, set_labels)

    accuracies_plot.append(child_accuracy)
    iterations_plot.append(iterations)

    #Replace
    lowest_acc = 10000

    acc_spot = -1
    for i in range(25):
        if (accuracies[i] < lowest_acc):
            lowest_acc = accuracies[i]
        if (accuracies[i] <= child_accuracy and accuracies[i] < lowest_acc):
            acc_spot = i

    accuracies[acc_spot] = child_accuracy
    iterations = iterations + 1

plt.plot(accuracies_plot, iterations_plot)
plt.show()

sum = 0
highest = -1
for k in range(25):
    sum  = sum + accuracies[i]
    if (accuracies[i] > highest):
        highest = accuracies[i]

avg = (sum / len(accuracies))
print "avg: " + str(avg)
print "best: " + str(highest)
