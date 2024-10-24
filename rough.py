import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error


import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('data.csv')
 
# Define the features and target variable
X = data[['bedrooms', 'sqrfeet', 'year_built']]  # Features
y = data['price']  # Target (house price)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)


new_house = 3
predicted_price = model.predict(new_house)

print(f'The predicted price for the house is: ${predicted_price[0]:.2f}')

