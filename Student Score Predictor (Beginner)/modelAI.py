import numpy as np
import pandas as pd

data = pd.read_csv("student_performance.csv")

print(data.head())
print(data.describe())

x = data[["weekly_self_study_hours", "attendance_percentage", "class_participation"]]
y = data["total_score"]

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# training the model
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
model = LinearRegression()    #tells the model to use linear regression
model.fit(X_train, y_train)   #input & output of the training data to the model

from sklearn.metrics import mean_squared_error

# measuring error
predictions = model.predict(X_test)      
#makes the model predict 100 at max and 0 at min (clamps)
predictions = [min(100, max(0, p)) for p in predictions]    #predict test data
mse = mean_squared_error(y_test, predictions)               #compare predicted output with actual output, 
                                                            #it punishes the model more for larger errors
print("MSE:", mse)

#baseline prediction
print("\nBaseline Prediction (is my model better than the most basic?)")                 #a simple model that always predicts the average score of the training data
baseline = np.mean(y_train)                         #average score of the training data
baseline_predictions = [baseline] * len(y_test)     #predicts the average score for all test data
baseline_mse = mean_squared_error(y_test, baseline_predictions)   #calculate MSE for baseline

print("Baseline MSE:", baseline_mse)
print("better by:", (baseline_mse - mse) / baseline_mse * 100, "%")

# optimization ig?
print("\ncoefficient:", model.coef_)        #to evaluate how a feature affect the output
print("intercept:", model.intercept_)       #something like a constant i suppose,
                                            #something that the model will add to the output 
                                            #regardless of the input features

import matplotlib.pyplot as plt

#visualization
plt.scatter(y_test, predictions)
plt.xlabel("Actual Scores")
plt.ylabel("Predicted Scores")
plt.show()

#testing my own input
sample = [[5, 90, 8]]
sampleDataFrame = pd.DataFrame(sample, columns=["weekly_self_study_hours", "attendance_percentage", "class_participation"])
pred = model.predict(sample)[0]
pred = min(100, max(0, pred))
print("\nPredicted Score for Sample Input [5, 90, 8]:", pred)