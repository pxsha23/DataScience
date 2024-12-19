# 6
# Identify a website with tabular data (e.g., a Wikipedia table). 
# Use BeautifulSoup to scrape the data, store it in a Data Frame and perform any
# 5 operations on the data frame.

from bs4 import BeautifulSoup
import pandas as pd
import requests

# Step 1: Scrape the table
url = "https://en.wikipedia.org/wiki/List_of_highest-grossing_Indian_films"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
table = soup.find('table', {'class': 'wikitable'})

# Step 2: Extract headers and rows
headers = [header.text.strip() for header in table.find_all('th')]
rows = [[cell.text.strip() for cell in row.find_all(['td', 'th'])] for row in table.find_all('tr')[1:]]

# Step 3: Create DataFrame and handle mismatched columns
df = pd.DataFrame(rows, columns=headers[:len(rows[0])])  # Ensure columns match rows

# Display DataFrame
print("DataFrame Head:\n", df.head())

# Step 4: Perform operations
print("\nSelect specific columns:\n", df.iloc[:, :2])  # Select the first two columns
print("\nFilter rows (first 3 rows):\n", df.head(3))  # Filter first 3 rows
