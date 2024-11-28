import pandas as pd
import numpy as np

df = pd.read_csv('diabetes.csv')
print(f'Ile danych: {df.shape}')
print(df.head().to_string())
print(df.describe().T.to_string())
print(df.isna().sum())

# wszędzie, gdzie są zera lub brak wartości - przypiszmy średnią
for col in ['glucose', 'bloodpressure', 'skinthickness', 'insulin',
       'bmi', 'diabetespedigreefunction', 'age']:
    df[col].replace(0, np.nan, inplace=True)
    mean_ = df[col].mean()
    df[col] = df[col].replace(np.nan, mean_)

print('Po czyszczeniu danych')
print(df.isna().sum())

# df.to_csv('cukrzyca.csv', index=False)

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

X = df.iloc[:, :-1]
y = df.outcome
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = LogisticRegression()
model.fit(X_train, y_train)
print(model.score(X_test, y_test))
print(pd.DataFrame(confusion_matrix(y_test, model.predict(X_test))))

print('sprawdźmy, czy klasy sa zbalansowane')
print(df.outcome.value_counts())

print('zmiana danych')
df1 = df.query('outcome == 0').sample(500)    # 500 zdrowych
df2 = df.query('outcome == 1').sample(500)    # 500 chorych
df3 = pd.concat([df1, df2])                   # łączenie

X = df3.iloc[:, :-1]
y = df3.outcome
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = LogisticRegression()
model.fit(X_train, y_train)
print(model.score(X_test, y_test))
print(pd.DataFrame(confusion_matrix(y_test, model.predict(X_test))))