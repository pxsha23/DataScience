# 8
# For the dataset ________________________, Use Python to handle missing values by
# dropping rows, filling with a specific value, and filling with the mean of the column.
# Display the data frame after each operation.
# a. Heart.csv
import pandas as pd

# Load the dataset
df = pd.read_csv('ratings.csv')

# Display the original data
print("Original DataFrame:")
print(df.head())

# 1. Drop rows with missing values
df_drop = df.dropna()
print("\nDataFrame after dropping rows with missing values:")
print(df_drop.head())

# 2. Fill missing values with a specific value (e.g., 0)
df_fill_value = df.fillna(0)
print("\nDataFrame after filling missing values with 0:")
print(df_fill_value.head())

# 3. Fill missing values with the mean of each column
# df_fill_mean = df.fillna(df.mean())
# print("\nDataFrame after filling missing values with the mean of each column:")
# print(df_fill_mean.head())
