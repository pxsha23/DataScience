# 4
# Create a line plot and bar chart to visualize categorical data using
# Matplotlib. Use all the possible operations on graphs.

import matplotlib.pyplot as plt

# Sample data
categories = ['A', 'B', 'C', 'D']
values = [10, 20, 15, 25]

# Line Plot
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.plot(categories, values, marker='o', color='blue', label='Line')
plt.title("Line Plot")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.legend()

# Bar Chart
plt.subplot(1, 2, 2)
plt.bar(categories, values, color='orange', label='Bar')
plt.title("Bar Chart")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.legend()

plt.tight_layout()
plt.show()
