import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

graphData = {'x': [], 'y': [], 'classType': []}


class Classification:
    x = 0.5
    y = 0.75
    classType = 1

    df = pd.DataFrame(data={'x': [], 'y': [], 'classType': []})

    def __init__(self, x, y, classType):
        self.x = x
        self.y = y
        self.classType = classType

    def makeNewSample(self, howMany):
        if howMany <= 0:
            print('\'howMany\' cannot be smaller or equal to 0')

        if howMany > 0:
            for i in range(howMany):
                tempX = np.random.normal(loc=self.x, scale=0.2)
                tempY = np.random.normal(loc=self.y, scale=0.2)

                self.df = self.df.append(
                    {'x': tempX, 'y': tempY, 'classType': self.classType}, ignore_index=True)

# def getAllTogether():


cl1 = Classification(0.5, 0.75, 1)
cl1.makeNewSample(30)

cl2 = Classification(3, 3, 2)
cl2.makeNewSample(30)

d = {'x': [0, 5], 'y': [0, 5], 'classType': [0, 0]}
df = pd.DataFrame(data=d)

# df = df.append({'x': 14, 'y': 14, 'class': 1}, ignore_index=True)

df = df.append(cl1.df)
df = df.append(cl2.df)

sns.scatterplot(data=df, x='x', y='y', hue='classType')

plt.show()
