# 12. 
# For the given dataset, calculate the correlation matrix and visualize it using a
# heatmap. Clean the given dataset.
# a. iris.csv
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('iris.csv')

# Display basic info and first few rows to inspect
print("Initial Dataset Info:")
print(df.info())
print("\nFirst 5 rows:")
print(df.head())

# Cleaning the dataset: Select only numeric columns
df_cleaned = df.select_dtypes(include=['float64', 'int64'])

# Optional: Drop rows with missing or invalid data (if any)
df_cleaned = df_cleaned.dropna()

# Calculate the correlation matrix
correlation_matrix = df_cleaned.corr()

# Visualize the correlation matrix using a heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Heatmap')
plt.show()
