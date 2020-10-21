import pandas as pd
import numpy as np


class Classifier:
    # self.df = pd.DataFrame(data={'x': [], 'y': [], 'classType': []})

    def __init__(self, numberOfModes, numberOfSamplesPerMode):
        self.modes = []
        self.variance = np.random.uniform(0.01, 0.04)
        self.generateModes(numberOfModes, numberOfSamplesPerMode)
        self.x = []
        self.y = []

    def generateModes(self, numberOfModes, numberOfSamplesPerMode):
        for i in range(numberOfModes):
            mode = Mode()
            mode.generateSamples(numberOfSamplesPerMode, self.variance)
            self.modes.append(mode)

    def getAllSamples(self):
        for mode in self.modes:
            for sample in mode.samples:
                self.x.append(sample.x)
                self.y.append(sample.y)
        return self.x, self.y
    # def makeNewSamples(self, numberOfModes, numberOfSamplesPerMode):
    #     self.df = self.df[0:0]
    #     if numberOfModes <= 0 or numberOfSamplesPerMode <= 0:
    #         print(
    #             '\'numberOfModes\' nor \'numberOfSamplesPerMode\' cannot be smaller or equal to 0')

    #     for i in range(numberOfModes):
    #         meanXY = np.random.uniform(0, 1, 2)
    #         mode = Mode(meanXY[0], meanXY[1], self.classType)

    #         for j in range(numberOfSamplesPerMode):
    #             mode.generateSample(self.variance)

    #         for sample in mode.samples:
    #             self.df = self.df.append(
    #                 {'x': sample.x, 'y': sample.y, 'classType': self.classType}, ignore_index=True)
    #     print(self.df)


class Mode:
    def __init__(self):
        meanXY = np.random.uniform(0, 1, 2)
        self.meanX = meanXY[0]
        self.meanY = meanXY[1]
        self.samples = []

    def generateSamples(self, numberOfSamplesPerMode, variance):
        for i in range(numberOfSamplesPerMode):
            sample = Sample(self.meanX, self.meanY, variance)
            self.samples.append(sample)


class Sample:
    x = 0
    y = 0

    def __init__(self, meanX, meanY, variance):
        self.x = np.random.normal(loc=meanX, scale=variance)
        self.y = np.random.normal(loc=meanY, scale=variance)
