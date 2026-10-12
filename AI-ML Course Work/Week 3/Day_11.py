import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression

df = pd.DataFrame({'height_cm':[170,180,160],
                   'weight_kg':[65,80,55]})

df['bmi'] = df['weight_kg'] / (df['height_cm']/100)**2
print(df)

new_df = pd.DataFrame({'price':[170,180,160],
                   'quantity':[65,80,55]})

new_df['total_cost'] = new_df['price'] * new_df['quantity']
print(new_df)

new_df = pd.DataFrame({'total_income':[110000,180000,80000],
                   'total_expenses':[100000,170000,90000]})

new_df['saving'] = new_df['total_income'] - new_df['total_expenses']
new_df['saving_rate'] = new_df['saving'] / new_df['total_income']
print(new_df)

new_df = pd.DataFrame({'study_hrs':[1,2,3,4,5],
                   'slepp_hrs':[8,7,6,8,7],'marks':[50,55,65,70,85]})
print(new_df.corr()['marks'])

ages = pd.Series([12,17,25,45,68,80])
print(pd.cut(ages, bins=[0,12,19,59,100], labels=['Child', 'Teen', 'Adult', 'Senior']))

new_df = pd.DataFrame({'study_hrs':[1,2,3,4,5],
                   'slepp_hrs':[8,7,6,8,7],'marks':[50,55,65,70,85]})
print(new_df.corr()['marks'])
scores = pd.Series([32,45,65,79,85,99])
print(pd.cut(scores, bins=[0,32,90,95,100], labels=['Fail', 'Pass', 'Merit', 'Distinction']))

# Task

X = np.array([[1],[2],[3],[4],[5],[6],[7],[8]])
y = np.array([40,45,52,60,68,75,82,90])

pipe = Pipeline ([
    ('scalar', StandardScaler()),
    ('model', LinearRegression())
])

pipe.fit(X, y)
print(pipe.predict([[9]]))