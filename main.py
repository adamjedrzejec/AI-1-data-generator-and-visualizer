import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

graphData = {'x': [], 'y': [], 'classType': []}


class Classifier:
    x = 0
    y = 0
    classType = 1

    variance = 0

    modes = []

    df = pd.DataFrame(data={'x': [], 'y': [], 'classType': []})

    def __init__(self, x, y, variance, classType):
        self.x = x
        self.y = y
        self.variance = variance
        self.classType = classType

    def makeNewSamples(self, numberOfModes, numberOfSamplesPerMode):
        if numberOfModes <= 0 or numberOfSamplesPerMode <= 0:
            print(
                '\'numberOfModes\' nor \'numberOfSamplesPerMode\' cannot be smaller or equal to 0')

        for i in range(numberOfModes):
            mode = Mode(2 * i, i, self.classType)
            self.modes.append(mode)

        for mode in self.modes:
            for i in range(numberOfSamplesPerMode):
                mode.generateSample()

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

    def generateSample(self):
        sample = Sample(self.meanX, self.meanY, 0.2)
        self.samples.append(sample)


class Sample:
    x = 0
    y = 0

    def __init__(self, meanX, meanY, variance):
        self.x = np.random.normal(loc=meanX, scale=variance)
        self.y = np.random.normal(loc=meanY, scale=variance)


# making new classifiers
cl1 = Classifier(0.5, 0.75, 0.2, 1)
cl1.makeNewSamples(2, 30)

cl2 = Classifier(3, 3, 0.2, 2)
cl2.makeNewSamples(2, 30)


# setting scope of the plot

d = {'x': [], 'y': [], 'classType': []}
df = pd.DataFrame(data=d)


# getting all the data altogether

df = df.append(cl1.df)
df = df.append(cl2.df)


# displaying the plot

sns.scatterplot(data=df, x='x', y='y', hue='classType')

plt.xlim(0, 5)
plt.ylim(0, 5)

plt.show()
