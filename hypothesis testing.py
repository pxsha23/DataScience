# 13.
# Perform a hypothesis test to determine if the mean of a sample differs 
# significantly from a known population mean.
# hypothesis testing
import numpy as np

from scipy.stats import ttest_1samp

import matplotlib.pyplot as plt

import seaborn as sns


# Sample data (e.g., heights of a sample of people in cm)

sample_data = [170, 168, 174, 171, 169, 167, 172, 176, 173, 175]


# Known population mean (e.g., average height of people in the population)

population_mean = 170


# Step 1: Perform t-test

t_stat, p_value = ttest_1samp(sample_data, population_mean)


# Step 2: Print results

print(f"T-Statistic: {t_stat:.2f}")

print(f"P-Value: {p_value:.4f}")


# Step 3: Conclusion based on p-value

alpha = 0.05  # Significance level

if p_value < alpha:

    print("Reject the null hypothesis (H₀): There is a significant difference between the sample mean and the population mean.")

else:

    print("Fail to reject the null hypothesis (H₀): There is no significant difference between the sample mean and the population mean.")


# Step 4: Visualize the sample data distribution

sns.histplot(sample_data, kde=True, color='skyblue', bins=5)

plt.title("Sample Data Distribution")

plt.xlabel("Value")

plt.ylabel("Frequency")

plt.show()

