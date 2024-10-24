import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('data.csv')

# Define the features and target variable
X = data[['bedrooms', 'bathrooms','sqft_living','sqft_lot','floors','condition','sqft_above','sqft_basement']]  # Features
y = data['price']  # Target (house price)

# Split the data into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a Linear Regression model
model = LinearRegression()

# Train the model on the training data
model.fit(X_train, y_train)

# Make predictions on the test data
y_pred = model.predict(X_test)

# Display model coefficients (weights assigned to each feature)
coefficients = pd.DataFrame(model.coef_, X.columns, columns=['Coefficient'])
print(coefficients)


# Example: Predict price for a house with 3 bedrooms, 1500 sq feet, built in 2010
# new_house = np.array([[3, 1340, 1955]])
new_house = np.array([[3, 1.50,1340,7912,1.5,3,1340,0]])
# Use the model to predict the price
predicted_price = model.predict(new_house)

print(f'The predicted price for the house is: ${predicted_price[0]:.2f}')

# Calculate Mean Squared Error (MSE)
mse = mean_squared_error(y_test, y_pred)

# Calculate Root Mean Squared Error (RMSE)
rmse = np.sqrt(mse)

# Calculate Mean Absolute Error (MAE)
mae = mean_absolute_error(y_test, y_pred)

# Calculate R² Score
r2 = r2_score(y_test, y_pred)

# Print the evaluation metrics
print(f"Mean Squared Error (MSE): {mse:.2f}")
print(f"Root Mean Squared Error (RMSE): {rmse:.2f}")
print(f"Mean Absolute Error (MAE): {mae:.2f}")
print(f"R² Score: {r2:.2f}")

x = data['sqft_living']
y = data['price']

'''plt.scatter(x, y, alpha=0.5)
plt.title('Scatter plot of sqft_living vs price')
plt.xlabel('sqft_living')
plt.ylabel('price')

plt.show()''' # scatter plot

sns.lmplot(x='sqft_living', y='price', data=data)
