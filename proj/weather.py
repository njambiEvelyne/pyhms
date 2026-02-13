import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Sample weather dataset
data = {
    "Humidity": [30, 45, 60, 80, 50, 65, 70, 40],
    "WindSpeed": [5, 7, 6, 10, 4, 8, 9, 3],
    "Pressure": [1012, 1010, 1008, 1005, 1011, 1007, 1006, 1013],
    "Temperature": [35, 30, 28, 25, 32, 27, 26, 34]
}

df = pd.DataFrame(data)

# Features (X) and Target (y)
X = df[["Humidity", "WindSpeed", "Pressure"]]
y = df["Temperature"]

# Split data into training and testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create model
model = LinearRegression()

# Train model
model.fit(X_train, y_train)

# Make predictions
predictions = model.predict(X_test)

# Evaluate model
mse = mean_squared_error(y_test, predictions)

print("Predicted Temperatures:", predictions)
print("Actual Temperatures:", y_test.values)
print("Mean Squared Error:", mse)

# Predict new weather data
new_data = np.array([[55, 6, 1010]])  # Humidity, WindSpeed, Pressure
predicted_temp = model.predict(new_data)

print("Predicted Temperature for new data:", predicted_temp[0])
