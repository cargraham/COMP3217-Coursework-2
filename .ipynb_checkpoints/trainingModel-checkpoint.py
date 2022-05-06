import numpy as np
import pandas as pd    
    
def logisticSigmoid(x):
    return 1.0/(1 + np.exp(-x))

def logisticDerivative(x):
    return logisticSigmoid(x) * (1 - logisticSigmoid(x))

learningRate = 0.00005

inputDim = 24
hiddenDim = 10

epochCount = 10

#np.random.seed(1)
inputWeights = np.random.uniform(-1, 1, (inputDim, hiddenDim))
hiddenWeights = np.random.uniform(-1, 1, hiddenDim)

preActivation = np.zeros(hiddenDim)
postActivation = np.zeros(hiddenDim)

trainingData = pd.read_csv('TrainingData80.txt', sep = ',', header = None,
                           names = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', 'output'])
targetOutput = trainingData.output
trainingData = trainingData.drop(['output'], axis = 1)
trainingData = np.asarray(trainingData)
np.random.shuffle(trainingData)
trainingCount = len(trainingData[:, 0])

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

##########
#TRAINING#
##########
for epoch in range(epochCount):
    for sample in range(trainingCount):
        for node in range(hiddenDim):
            preActivation[node] = np.dot(trainingData[sample, :], inputWeights[:, node])
            postActivation[node] = logisticSigmoid(preActivation[node])

        preActivationOut = np.dot(postActivation, hiddenWeights)
        postActivationOut = logisticSigmoid(preActivationOut)

        finalError = postActivationOut - targetOutput[sample]

        #back propagation
        for hiddenNode in range(hiddenDim):
            error = finalError * logisticDerivative(preActivationOut)
            hiddenGradient = error * postActivation[hiddenNode]

            for inputNode in range(inputDim):
                inputValue = trainingData[sample, inputNode]
                inputGradient = error * hiddenWeights[hiddenNode] * logisticDerivative(preActivation[hiddenNode]) * inputValue

                inputWeights[inputNode, hiddenNode] -= learningRate * inputGradient

            hiddenWeights[hiddenNode] -= learningRate * hiddenGradient

print("TRAINING DONE")

############
#VALIDATION#
############
correctCount = 0
for sample in range(validationCount):
    for node in range(hiddenDim):
        preActivation[node] = np.dot(validationData[sample, :], inputWeights[:, node])
        postActivation[node] = logisticSigmoid(preActivation[node])

    preActivationOut = np.dot(postActivation, hiddenWeights)
    postActivationOut = logisticSigmoid(preActivationOut)

    print("postActivation ", postActivationOut)

    if postActivationOut > 0.5:
        output = 1
    else:
        output = 0

    if output == validationTargetOutput[sample]:
        correctCount += 1

print("EVALUATION DONE")
print("Percentage of correct classifications: " + str(correctCount*100/validationCount))

#########
#TESTING#
#########
for sample in range(testingCount):
    for node in range(hiddenDim):
        preActivation[node] = np.dot(testingData[sample, :], inputWeights[:, node])
        postActivation[node] = logisticSigmoid(preActivation[node])

    preActivationOut = np.dot(postActivation, hiddenWeights)
    postActivationOut = logisticSigmoid(preActivationOut)

    if postActivationOut > 0.5:
        output = 1
    else:
        output = 0

    testingResults.write("working")
    #print(testingData[sample, :], output)

#np.savetxt('TestingResults.txt', testingData, delimiter=',')
testingResults.close()
print("TESTING DONE")


