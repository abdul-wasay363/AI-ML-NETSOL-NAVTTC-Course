import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score


df = pd.read_csv("House Price Prediction Dataset.csv")
df_copy = df.copy()


print(df_copy.columns)
print(df_copy['Area'].value_counts())

df_copy['Area_in_marla'] = df_copy['Area'] / 272.3
print(df_copy['Area_in_marla'])
print(df_copy.columns)

# separte feature X and target y
X = df_copy[['Area_in_marla']]
y = df_copy['Price']

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size = 0.2,
    random_state = 42
)

model = LinearRegression()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

r2 = r2_score(y_test, y_pred)
print("R2 Score: ", r2)

mse = mean_squared_error(y_test, y_pred)
print("MSE: ", mse)

mae = mean_absolute_error(y_test, y_pred)
print("MAE: ", mae)

rmse = mean_squared_error(y_test, y_pred) ** 0.5
print("RMSE: ",rmse)

comparison = pd.DataFrame({
    "Actual Price": y_test.values,
    "Predicted Price": y_pred
})

comparison['Error'] = (
    comparison["Actual Price"] - comparison["Predicted Price"]
)
print(comparison)