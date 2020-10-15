import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

d = {'x': [1, 2], 'y': [3, 5], 'class': [1, 2]}
df = pd.DataFrame(data=d)

df = df.append({'x': 14, 'y': 14, 'class': 1}, ignore_index=True)

sns.scatterplot(data=df, x='x', y='y', hue='class')

plt.show()
