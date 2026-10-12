import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler, MinMaxScaler

df = pd.DataFrame({'name':['Ali','Sara','Ali'],
                   'marks':[85,92,85]})
print(df.duplicated())
print(df.drop_duplicates())


df =pd.DataFrame({'name': ["Ali", "Sara", "Usman", "Sara", "Ahmad"],
                  'marks': [85, 92, 92, 92, 95]})


print(df.duplicated())
print(df.drop_duplicates())

prices = pd.Series([100, 500, 1000, 50000, 100000])
log_prices = np.log(prices)
print(log_prices)

sizes = ['Small', 'Medium', 'Large', 'Medium']
le = LabelEncoder()
print(le.fit_transform(sizes))

vals = np.array([[10],[20],[30],[40],[50]])
print(StandardScaler().fit_transform(vals).flatten())
print(MinMaxScaler().fit_transform(vals).flatten())