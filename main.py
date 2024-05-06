import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
from sklearn.svm import SVR


np.random.seed(42)
num_data_points = 100
days = np.arange(1, num_data_points + 1)
prices = 100 + np.cumsum(np.random.rand(num_data_points))

data = pd.DataFrame({"Days": days, "Prices": prices})
data['Days'] = data['Days'].astype(float)

X = data[['Days']]
Y = data['Prices']

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

scaler = MinMaxScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.fit_transform(X_test)

model = SVR(kernel="linear")
model.fit(X_train_scaled, Y_train)

Y_pred_train = model.predict(X_train_scaled)
Y_pred_test = model.predict(X_test_scaled)

mse_train = mean_squared_error(Y_train, Y_pred_train)
mse_test = mean_squared_error(Y_test, Y_pred_test)
print(f"mse_train: {mse_train:.2f}")
print(f"mse_test: {mse_test:.2f}")