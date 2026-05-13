# NumPy Mini Project
# Student Performance Prediction System

import numpy as np

# Creating dataset for 10 students
data = np.array([
    [78, 85, 80, 90, 1],
    [45, 50, 40, 55, 0],
    [88, 92, 84, 91, 1],
    [60, 65, 58, 70, 1],
    [35, 40, 30, 45, 0],
    [95, 90, 93, 97, 1],
    [55, 60, 52, 58, 0],
    [72, 75, 70, 80, 1],
    [48, 42, 50, 46, 0],
    [82, 79, 85, 88, 1]
])

# Separating features and labels
X = data[:, 0:4]
y = data[:, 4]

print("Features:\n", X)
print("\nLabels:\n", y)

# Average, maximum, minimum marks
print("\nAverage Marks:", np.mean(X))
print("Maximum Marks:", np.max(X))
print("Minimum Marks:", np.min(X))

# Passed and failed students
passed = np.sum(y == 1)
failed = np.sum(y == 0)

print("\nPassed Students:", passed)
print("Failed Students:", failed)

# Students scoring above 80
above_80 = X[X > 80]
print("\nMarks Above 80:\n", above_80)

# Students scoring below 50
below_50 = X[X < 50]
print("\nMarks Below 50:\n", below_50)

# Normalization
normalized = (X - np.min(X)) / (np.max(X) - np.min(X))

print("\nNormalized Data:\n", normalized)

# Simple prediction logic
# If average marks >= 60 then Pass otherwise Fail

avg_marks = np.mean(X, axis=1)

predictions = np.where(avg_marks >= 60, 1, 0)

print("\nPredictions:\n", predictions)

# Accuracy calculation
accuracy = np.mean(predictions == y) * 100

print("\nAccuracy:", accuracy, "%")