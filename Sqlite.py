# 5
# Set up a local SQLite database and create a table with some sample data.
# Use Python to import data from the SQL table into a data frame and perform any
# 5 operations on the data frame.

import sqlite3
import pandas as pd

# Connect to SQLite and create table
conn = sqlite3.connect('sample.db')
cur = conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, name TEXT, age INTEGER, grade TEXT)''')
# Insert sample data
cur.executemany("INSERT INTO students (name, age, grade) VALUES (?, ?, ?)", 
                [('ABC', 22, 'A'), ('PQR', 25, 'B'), ('XYZ', 20, 'A')])
conn.commit()
# Load data into DataFrame
df = pd.read_sql_query("SELECT * FROM students", conn)
# Perform operations
print("\nOriginal DataFrame:\n", df)
print("\nSelect columns:\n", df[['name', 'grade']])
print("\nFilter rows:\n", df[df['age'] > 21])
df['status'] = df['grade'].apply(lambda g: 'Pass' if g == 'A' else 'Fail')
print("\nNew column added:\n", df)
print("\nSorted by age:\n", df.sort_values(by='age'))
# Close connection
conn.close()
