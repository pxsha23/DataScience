# 14. Implement a logistic regression model using scikit-learn to classify
# the following dataset.
# a. Heart.csv
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('heart.csv')

# Display basic info and first few rows
print("Dataset Info:")
print(df.info())
print("\nFirst 5 rows:")
print(df.head())

# Preprocessing
# Drop missing values if any
df = df.dropna()

# Separating features (X) and target (y)
# Assuming the target column is 'target' or a similar name
# Update the column name as per your dataset
X = df.drop(columns=['target'])  # Replace 'target' with the actual target column name
y = df['target']                 # Replace 'target' with the actual target column name

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a logistic regression model
model = LogisticRegression(max_iter=1000)  # Increase max_iter if convergence issues occur
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
report = classification_report(y_test, y_pred)

print(f"Accuracy: {accuracy:.2f}")
print("\nConfusion Matrix:")
print(conf_matrix)
print("\nClassification Report:")
print(report)

# # Visualize the confusion matrix
# plt.figure(figsize=(6, 4))
# sns.heatmap(conf_matrix, annot=True, cmap='Blues', fmt='d')
# plt.title('Confusion Matrix')
# plt.xlabel('Predicted')
# plt.ylabel('Actual')
# plt.show()
