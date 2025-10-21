# Weather Data Analysis using Pandas and NumPy
# Made by Lakshit Pandey

import pandas as pd
import numpy as np

# Load the Dataset
# if no datasheet available right now , we will take it as sample.
data = {
    'Date': pd.date_range(start='2024-01-01', periods=10, freq='D'),
    'Temperature_C': [22, 25, 20, 19, 24, 27, 26, 23, 21, 22],
    'Humidity_%': [60, 55, 65, 70, 58, 52, 50, 63, 66, 61],
    'WindSpeed_kmph': [10, 12, 8, 6, 11, 14, 13, 9, 7, 10],
    'Weather': ['Sunny', 'Sunny', 'Rainy', 'Rainy', 'Cloudy', 'Sunny', 'Sunny', 'Cloudy', 'Rainy', 'Cloudy']
}

df = pd.DataFrame(data)

print("===== WEATHER DATA =====")
print(df.head())

# Basic Information
print("\n===== BASIC INFO =====")
print(df.info())
print("\nSummary Statistics:")
print(df.describe())

# Data Cleaning
# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Example of filling missing data (if any)
df['Temperature_C'].fillna(df['Temperature_C'].mean(), inplace=True)

#Data Analysis
print("\n===== DATA ANALYSIS =====")

# Average Temperature, Humidity, and Wind Speed
print("\nAverage Temperature:", round(df['Temperature_C'].mean(), 2))
print("Average Humidity:", round(df['Humidity_%'].mean(), 2))
print("Average Wind Speed:", round(df['WindSpeed_kmph'].mean(), 2))

# Maximum and Minimum Temperature
print("\nHighest Temperature:", df['Temperature_C'].max())
print("Lowest Temperature:", df['Temperature_C'].min())

# Count of each weather type
print("\nWeather Condition Counts:")
print(df['Weather'].value_counts())

# Days with temperature above 25°C
hot_days = df[df['Temperature_C'] > 25]
print("\nDays with temperature > 25°C:")
print(hot_days[['Date', 'Temperature_C', 'Weather']])

# Correlation Analysis
print("\n===== CORRELATION ANALYSIS =====")
corr_matrix = df[['Temperature_C', 'Humidity_%', 'WindSpeed_kmph']].corr()
print(corr_matrix)

# NumPy Insights
temps = np.array(df['Temperature_C'])
print("\n===== NUMPY OPERATIONS =====")
print("Temperature Standard Deviation:", round(np.std(temps), 2))
print("Temperature Variance:", round(np.var(temps), 2))

# Optional: Save Cleaned Data
df.to_csv("cleaned_weather_data.csv", index=False)
print("\n✅ Cleaned data saved as 'cleaned_weather_data.csv'")
