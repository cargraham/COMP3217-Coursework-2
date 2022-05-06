import numpy as np
import pandas as pd
from sklearn.metrics import classification_report
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC

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
validation_data = validation_data.iloc[:, :24]

#converts the DataFrames to NumPy arrays
training_data = np.asarray(training_data.iloc[:, :24])
training_data_80 = np.asarray(training_data_80)
target_labels = np.asarray(target_labels)
validation_data = np.asarray(validation_data)
validation_target_labels = np.asarray(validation_target_labels)

MLP_clf = MLPClassifier()
MLP_clf.fit(training_data_80, target_labels_80)
MLP_results = MLP_clf.predict(validation_data)
print(MLP_results)
print(validation_target_labels)
print("Multilayer Perceptron Classifier")
print(classification_report(MLP_results, validation_target_labels))
