# 9
# Use the dataset ________________________, Use Python to identify outliers
# using the Z-score method and remove the outliers and display the cleaned DataFrame.

import pandas as pd
# Example data
data = pd.DataFrame({
    'col1': [1, 2, 3, 4, 5, 100],  # Notice 100 is an outlier
    'col2': [2, 3, 4, 200, 6, 5]   # Notice 200 is an outlier
})
# 1. Calculate the Z-scores for each column
z_scores = np.abs((data - data.mean()) / data.std())
print(z_scores)
# 2. Set the threshold for outliers
threshold = 2
# 3. Filter rows where all Z-scores are below the threshold
outliers_removed = (z_scores < threshold).all(axis=1)
# 4. Apply the filter to the original data
cleaned_data = data[outliers_removed]
# Print results
print("Original Data:\n", data)
print("\nOutliers Removed Data:\n", cleaned_data)
data1 =  pd.DataFrame(['col1'])
