import collections
import math
import re
import numpy as np
import pandas as pd

#returns prior probability
def prior_prob(y):
    y_dict = collections.Counter(y)
    prior_probab = np.ones(2)
    for i in range(0, 2):
        prior_probab[i] = y_dict[i]/y.shape[0]
    return prior_probab

#returns mean and variance of all features
def mean_var(X, y):
    features_count = X.shape[1]
    m = np.ones((2, features_count))
    v = np.ones((2, features_count))
    n_0 = np.bincount(y)[np.nonzero(np.bincount(y))[0]][0]
    x0 = np.ones((n_0, features_count))
    x1 = np.ones((X.shape[0] - n_0, features_count))
    
    k = 0
    for i in range(0, X.shape[0]):
        if y[i] == 0:
            x0[k] = X[i]
            k += 1
            
    k = 0
    for i in range(0, X.shape[0]):
        if y[i] == 1:
            x1[k] = X[i]
            k += 1
            
    for j  in range(0, features_count):
        m[0][j] = np.mean(x0.T[j])
        v[0][j] = np.var(x0.T[j])*(n_0/(n_0 - 1))
        m[1][j] = np.mean(x1.T[j])
        v[1][j] = np.var(x1.T[j])*((X.shape[0]-n_0)/((X.shape[0] -n_0) - 1))
        
    return m, v

def prob_feature_class(m, v, x):
    feature_count = m.shape[1]
    prob_fc = np.ones(2)
    for i in range(0, 2):
        product = 1
        for j in range(0, feature_count):
            product = product * (1/math.sqrt(2*3.14*v[i][j])) * math.exp(-0.5 * pow((x[j] - m[i][j]),2)/v[i][j])
        prob_fc[i] = product
    return prob_fc

def gaussian_naive_bayes(X, y, x):
    m, v = mean_var(X, y)
    prob_fc = prob_feature_class(m, v, x)
    prior_probab = prior_prob(y)
    prob_cf = np.ones(2)
    total_prob = 0
    for i in range(0, 2):
        total_prob = total_prob + (prob_fc[i] * prior_probab[i])
    for i in range(0, 2):
        prob_cf[i] = (prob_fc[i] * prior_probab[i])/total_prob
    prediction = int(prob_cf.argmax())
    return prediction

columns=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', 'output']

trainingData = pd.read_csv('TrainingData80.txt', sep = ',', header = None, names = columns)
targetOutput = np.asarray(trainingData.output)
trainingData = trainingData.drop(['output'], axis = 1)
trainingData = np.asarray(trainingData)
#trainingData = np.random.shuffle(trainingData)

validationData = pd.read_csv('ValidationData20.txt', sep = ',', header = None, names = columns)
validationTargetOutput = validationData.output
validationData = validationData.drop(['output'], axis = 1)
validationData = np.asarray(validationData)
validationCount = len(validationData[:, 0])

correct_count = 0
for guideline in range(validationCount):
    prediction = gaussian_naive_bayes(trainingData, targetOutput, validationData[guideline])
    if prediction == validationTargetOutput[guideline]:
        correct_count += 1
    
print("Percentage of correct classifications: " + str(correct_count*100/validationCount))

testingData = pd.read_csv('TestingData.txt', sep = ',', header = None)
testingData = np.asarray(testingData)
testingCount = len(testingData[:, 0])
testingResults = open('TestingResults.txt', 'a')
testingResults.seek(0)
testingResults.truncate()

for guideline in range(testingCount):
    prediction = gaussian_naive_bayes(trainingData, targetOutput, testingData[guideline])
    testingString = re.sub('( \[|\[|\])', '', str(testingData[guideline]))
    print(testingString)
    testingResults.write(testingString)
    
testingResults.close()