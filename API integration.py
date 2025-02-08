# 7
# Identify a public API (e.g., OpenWeatherMap, CoinGecko). Use Python to fetch 
# data from the API, store it in a data frame and perform any 5 operations
# on the data frame.

import requests
import pandas as pd

# API setup
url = "http://api.openweathermap.org/data/2.5/weather"
api_key = 'bd5e378503939ddaee76f12ad7a97608'
city = "New York"
params = {'q': city, 'appid': api_key, 'units': 'metric'}

# Fetch data
response = requests.get(url, params=params)
data = response.json()

# Create DataFrame
weather_data = {
    "City": [data["name"]],
    "Weather": [data["weather"][0]["description"]],
    "Temperature (C)": [data["main"]["temp"]],
    "Humidity (%)": [data["main"]["humidity"]],
    "Wind Speed (m/s)": [data["wind"]["speed"]]
}
df = pd.DataFrame(weather_data)

# Perform 5 operations
print("\n1. Display Columns:")
print(df.columns)

print("\n2. Filter Temperature > 0°C:")
print(df[df["Temperature (C)"] > 0])

df['Feels Like (C)'] = data["main"]["feels_like"] 
# 3. Add new column
print("\n3. Add 'Feels Like' column:")
print(df[['City', 'Feels Like (C)']])

print("\n4. Sort by Wind Speed:")
print(df.sort_values(by="Wind Speed (m/s)", ascending=False))

print("\n5. Select Weather and Temperature columns:")
print(df[['Weather', 'Temperature (C)']])
