import collections
import math
import re
import numpy as np
import pandas as pd
from sklearn.metrics import classification_report

#returns prior probability of label in dataset
def prior_prob(target_labels):
    y_dict = collections.Counter(target_labels)
    prior_probab = np.ones(2)
    for i in range(0, 2):
        prior_probab[i] = y_dict[i]/target_labels.shape[0]
    return prior_probab

#returns mean and variance of all guideline in training data
def mean_var(training_data, target_labels):
    features_count = training_data.shape[1]
    mean = np.ones((2, features_count))
    var = np.ones((2, features_count))
    n_0 = np.bincount(target_labels)[np.nonzero(np.bincount(target_labels))[0]][0]
    x0 = np.ones((n_0, features_count))
    x1 = np.ones((training_data.shape[0] - n_0, features_count))
    
    k = 0
    for i in range(0, training_data.shape[0]):
        if target_labels[i] == 0:
            x0[k] = training_data[i]
            k += 1
            
    k = 0
    for i in range(0, training_data.shape[0]):
        if target_labels[i] == 1:
            x1[k] = training_data[i]
            k += 1
            
    for j in range(0, features_count):
        mean[0][j] = np.mean(x0.T[j])
        var[0][j] = np.var(x0.T[j])*(n_0/(n_0 - 1))
        mean[1][j] = np.mean(x1.T[j])
        var[1][j] = np.var(x1.T[j])*((training_data.shape[0]-n_0)/((training_data.shape[0] -n_0) - 1))
        
    return mean, var

#returns the array containing the probability that the given test data belongs to each class
def prob_feature_class(mean, var, guideline):
    feature_count = mean.shape[1]
    prob_fc = np.ones(2)
    for i in range(0, 2):
        product = 1
        for j in range(0, feature_count):
            product = product * (1/math.sqrt(2*3.14*var[i][j])) * math.exp(-0.5 * pow((guideline[j] - mean[i][j]),2)/var[i][j])
        prob_fc[i] = product
    return prob_fc

#returns an array containing the class with the highest probability for each guideline
def gaussian_naive_bayes(training_data, target_labels, testing_data):
    testing_results = []
    mean, var = mean_var(training_data, target_labels)
    prior_probab = prior_prob(target_labels)
    testing_count = len(testing_data[:, 0])
    for guideline in range(testing_count):
        prob_fc = prob_feature_class(mean, var, testing_data[guideline])
        prob_cf = np.ones(2)
        total_prob = 0
        for i in range(0, 2):
            total_prob = total_prob + (prob_fc[i] * prior_probab[i])
        for i in range(0, 2):
            prob_cf[i] = (prob_fc[i] * prior_probab[i])/total_prob
        prediction = int(prob_cf.argmax())
        testing_results.append(prediction)
    return testing_results


#reads in the whole training data set from 'TrainingData.txt' to train the model and shuffles the order
training_data = pd.read_csv('TrainingData.txt', sep = ',', header = None)
training_data = training_data.sample(frac = 1, random_state = 49).reset_index(drop=True)
target_labels = training_data.iloc[:, -1]

#splits 80% of the training data to train the model
training_data_80 = training_data.head(8000)
target_labels_80 = training_data_80.iloc[:, -1]
training_data_80 = training_data_80.iloc[:, :24]

#splits 20% of the training data to validate the model
validation_data = training_data.tail(2000)
validation_target_labels = validation_data.iloc[:, -1]

#converts the Pandas DataFrames to NumPy arrays
training_data = np.asarray(training_data.iloc[:, :24])
training_data_80 = np.asarray(training_data_80)
target_labels = np.asarray(target_labels)
validation_data = np.asarray(validation_data)
validation_target_labels = np.asarray(validation_target_labels)

#counts how many predictions were correct to produce an accuracy score
correct_count = 0
validation_count = len(validation_data[:, 0])
validation_results = gaussian_naive_bayes(training_data_80, target_labels_80, validation_data)
for guideline in range(validation_count):
    if validation_results[guideline] == validation_target_labels[guideline]:
        correct_count += 1

#prints the accuracy of the model
print("Percentage of correct classifications: " + str(correct_count*100/validation_count))
print(classification_report(validation_results, validation_target_labels))

#reads in the test data from 'TestingData.txt'
testing_data = pd.read_csv('TestingData.txt', sep = ',', header = None)
testing_data = np.asarray(testing_data)
testing_count = len(testing_data[:, 0])

#predict the labels for the testing data and write to file
testing_results = gaussian_naive_bayes(training_data, target_labels, testing_data)

#create a new array to store the guidelines with their predictions
testing_data_with_predictions = np.ones((testing_count, 25))

#for each guideline in the testing data, write the guideline and the predicted label in result file
for guideline in range(testing_count):
    prediction = testing_results[guideline]
    testing_data_with_predictions[guideline] = np.append(testing_data[guideline], prediction)

#write results to results file
formatter = (['%.15g'] * 24)
formatter = formatter + ['%i']
np.savetxt('TestingResults.txt', testing_data_with_predictions, delimiter=',', fmt=formatter)
print("DONE")
