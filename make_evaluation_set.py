trainingData = open('TrainingData.txt', 'r')
training80Data = open('TrainingData80.txt', 'a')
training80Data.seek(0)
training80Data.truncate()

validation20Data = open('ValidationData20.txt', 'a')
validation20Data.seek(0)
validation20Data.truncate()

testing20Data = open('TestingData20.txt', 'a')
testing20Data.seek(0)
testing20Data.truncate()

Lines = trainingData.readlines()

counter = 0

for line in Lines:
    if counter != 20:
        training80Data.write(line)
    else:
        validation20Data.write(line)
        counter = 0

    counter += 1


trainingData.close()
training80Data.close()
validation20Data.close()
testing20Data.close()
