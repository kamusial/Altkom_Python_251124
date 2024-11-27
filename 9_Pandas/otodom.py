import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from seaborn import heatmap

# pd.set_option('display.max_rows', 500)

df = pd.read_csv('otodom.csv')
print(type(df))
print(df)
print(df.describe().T.to_string())

print(df.iloc[ 1:5 , 2:4 ])

print(df.describe().T.loc['price', '25%'])
sns.heatmap(df.iloc[:, 1:].corr(), annot=True)
plt.show()

sns.histplot(df.price)
plt.show()
q3 = df.describe().T.loc['price', '75%']
print(q3)

df1 = df[(df.price > 0) & (df.price < q3)]
sns.histplot(df1.price)
plt.show()