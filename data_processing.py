# 3
# Create a data frame from a dictionary of lists. Perform basic operations like selecting
# rows/columns, filtering, and sorting.

import pandas as pd

# Create a DataFrame from a dictionary of lists
data = {
    'Name': ['JAKE', 'AMY', 'CAPTAIN', 'BOYLE', 'ROSA'],
    'Age': [25, 30, 35, 40, 28],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'],
    'Score': [85, 90, 95, 80, 88]
}
df = pd.DataFrame(data)
# Display the DataFrame
print("Original DataFrame:")
print(df)
# Select columns
print("\nSelecting 'Name' and 'Score' columns:")
print(df[['Name', 'Score']])
# Select rows using loc (label-based) and iloc (integer-location-based)
print("\nSelect rows using loc (row 2):")
print(df.loc[2])  # Charlie's details
print("\nSelect rows using iloc (row 0 to 2):")
print(df.iloc[0:3])  # First three rows
# Filtering rows based on conditions
print("\nFiltering rows where Age > 30:")
filtered_df = df[df['Age'] > 30]
print(filtered_df)
# Sorting
print("\nSorting by 'Score' in descending order:")
sorted_df = df.sort_values(by='Score', ascending=False)
print(sorted_df)
