import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

graphData = {'x': [], 'y': [], 'classType': []}


class Classifier:
    x = 0.5
    y = 0.75
    classType = 1

    df = pd.DataFrame(data={'x': [], 'y': [], 'classType': []})

    def __init__(self, x, y, classType):
        self.x = x
        self.y = y
        self.classType = classType

    def makeNewSamples(self, howMany):
        if howMany <= 0:
            print('\'howMany\' cannot be smaller or equal to 0')

        if howMany > 0:
            for i in range(howMany):
                tempX = np.random.normal(loc=self.x, scale=0.2)
                tempY = np.random.normal(loc=self.y, scale=0.2)

                self.df = self.df.append(
                    {'x': tempX, 'y': tempY, 'classType': self.classType}, ignore_index=True)


# making new classifiers
cl1 = Classifier(0.5, 0.75, 1)
cl1.makeNewSamples(30)

cl2 = Classifier(3, 3, 2)
cl2.makeNewSamples(30)


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
