 # decision tree classifier
from sklearn.datasets import load_iris

from sklearn.model_selection import train_test_split

from sklearn.tree import DecisionTreeClassifier

from sklearn.metrics import accuracy_score, confusion_matrix, classification_report


# Load the Iris dataset

iris = load_iris()

X, y = iris.data, iris.target


# Split the data into training and testing sets (70% train, 30% test)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)


# Initialize the Decision Tree Classifier

clf = DecisionTreeClassifier(random_state=42)


# Train the classifier

clf.fit(X_train, y_train)


# Predict the test set results

y_pred = clf.predict(X_test)


# Evaluate the performance


# 1. Accuracy

accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", accuracy)


# 2. Confusion Matrix

cm = confusion_matrix(y_test, y_pred)

print("\nConfusion Matrix:")

print(cm)


# 3. Classification Report (Precision, Recall, F1-score)

report = classification_report(y_test, y_pred, target_names=iris.target_names)

print("\nClassification Report:")

print(report)

