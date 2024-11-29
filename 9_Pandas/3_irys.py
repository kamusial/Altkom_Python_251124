import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('iris.csv')
# print(df.class.value_counts())
print(df['class'].value_counts())

species = {
    'Iris-setosa': 0, 'Iris-versicolor': 1, 'Iris-virginica': 2
}

df['class_values'] = df['class'].map(species)
# df['tmp'] = df['sepallength'] * df['sepalwidth'] - 1
print(df)
print(df.describe())

sample = np.array([5.6, 3.2, 5.2, 1.45])

sns.scatterplot(data=df, x='sepallength', y='sepalwidth', hue='class')
plt.scatter(5.6, 3.2, c='r')
plt.show()

sns.scatterplot(data=df, x='petallength', y='petalwidth', hue='class')
plt.scatter(5.2, 1.45, c='r')
plt.show()

df['distance'] = (df.sepallength-sample[0])**2 + (df.sepalwidth-sample[1])**2 +\
                 (df.petallength-sample[2])**2 + (df.petalwidth-sample[3])**2

print(df.sort_values(by='distance').to_string())