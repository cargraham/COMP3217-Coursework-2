from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import classification_report
import numpy as np
import pandas as pd

columns=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', 'output']

trainingData = pd.read_csv('TrainingData80.txt', sep = ',', header = None, names = columns)
targetOutput = trainingData.output
trainingData = trainingData.drop(['output'], axis = 1)
trainingData = np.asarray(trainingData)

validationData = pd.read_csv('ValidationData20.txt', sep = ',', header = None, names = columns)
validationTargetOutput = validationData.output
validationData = validationData.drop(['output'], axis = 1)
validationData = np.asarray(validationData)
validationCount = len(validationData[:, 0])

clf = GaussianNB()
clf.fit(trainingData, targetOutput)

results = clf.predict(validationData)
print(classification_report(validationTargetOutput, results))