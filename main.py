import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

graphData = {'x': [], 'y': [], 'classType': []}


class Classifier:
    classType = 1
    variance = 0

    df = pd.DataFrame(data={'x': [], 'y': [], 'classType': []})

    def __init__(self, variance, classType):
        self.variance = variance
        self.classType = classType

    def makeNewSamples(self, numberOfModes, numberOfSamplesPerMode):
        if numberOfModes <= 0 or numberOfSamplesPerMode <= 0:
            print(
                '\'numberOfModes\' nor \'numberOfSamplesPerMode\' cannot be smaller or equal to 0')

        for i in range(numberOfModes):
            meanXY = np.random.uniform(0, 1, 2)
            mode = Mode(meanXY[0], meanXY[1], self.classType)

            for j in range(numberOfSamplesPerMode):
                mode.generateSample(self.variance)

            for sample in mode.samples:
                self.df = self.df.append(
                    {'x': sample.x, 'y': sample.y, 'classType': self.classType}, ignore_index=True)


class Mode:
    meanX = 0
    meanY = 0

    samples = []

    def __init__(self, meanX, meanY, classType):
        self.meanX = meanX
        self.meanY = meanY
        self.samples = []

    def generateSample(self, variance):
        sample = Sample(self.meanX, self.meanY, variance)
        self.samples.append(sample)


class Sample:
    x = 0
    y = 0

    def __init__(self, meanX, meanY, variance):
        self.x = np.random.normal(loc=meanX, scale=variance)
        self.y = np.random.normal(loc=meanY, scale=variance)


# making new classifiers
cl1 = Classifier(0.02, 1)
cl1.makeNewSamples(6, 20)

cl2 = Classifier(0.02, 2)
cl2.makeNewSamples(6, 20)


# setting scope of the plot

d = {'x': [], 'y': [], 'classType': []}
df = pd.DataFrame(data=d)


# getting all the data altogether

df = df.append(cl1.df)
df = df.append(cl2.df)


# displaying the plot

sns.scatterplot(data=df, x='x', y='y', hue='classType')

plt.xlim(-0.1, 1.1)
plt.ylim(-0.1, 1.1)

plt.show()
