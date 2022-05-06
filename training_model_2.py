from sklearn.neural_network import MLPClassifier
import numpy as np
import pandas as pd

trainingData = pd.read_csv('TrainingData.txt', sep = ',', header = None,
                           names = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', 'output'])
targetOutput = trainingData.output
trainingData = trainingData.drop(['output'], axis = 1)
trainingData = np.asarray(trainingData)

validationData = pd.read_csv('ValidationData20.txt', sep = ',', header = None,
                             names = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', 'output'])
validationTargetOutput = validationData.output
validationData = validationData.drop(['output'], axis = 1)
validationData = np.asarray(validationData)
validationCount = len(validationData[:, 0])

testingData = pd.read_csv('TestingData.txt', sep = ',', header = None)
testingData = np.asarray(testingData)
testingCount = len(testingData[:, 0])
testingResults = open('TestingResults.txt', 'a')
testingResults.seek(0)
testingResults.truncate()

clf = MLPClassifier(solver='sgd', hidden_layer_sizes=(24, 10), random_state=1, activation='logistic', early_stopping=True, learning_rate_init=5e-2)
clf.fit(trainingData, targetOutput)
print("TRAINING DONE")
print("Mean Accuracy: " + str(clf.score(trainingData, targetOutput)))

results = clf.predict(testingData)

for sample in range(testingCount):
    guideline = testingData[sample, :]
    guidelineString = ",".join(guideline) + "," + str(results[sample])
    testingResults.write(guidelineString)                                    

testingResults.close()
