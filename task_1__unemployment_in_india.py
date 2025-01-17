# -*- coding: utf-8 -*-
"""TASK 1 _UNEMPLOYMENT IN INDIA.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1WIp0FR2M56eYnMIusMqj58BJgIloEhYR
"""

pip install pandas numpy matplotlib seaborn

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set the style of the visualization
sns.set_style('whitegrid')

# Load the dataset
data = pd.read_csv('Unemployement.csv')

# Display the first few rows of the dataset
print(data.head())

# Display the column names
print(data.columns)

# Strip any leading or trailing whitespace characters from the column names
data.columns = data.columns.str.strip()

# Display the cleaned column names
print(data.columns)

# Check for missing values
print(data.isnull().sum())

# Fill or drop missing values if necessary
data['Estimated Unemployment Rate (%)'].fillna(data['Estimated Unemployment Rate (%)'].mean(), inplace=True)
data['Estimated Employed'].fillna(data['Estimated Employed'].mean(), inplace=True)
data['Estimated Labour Participation Rate (%)'].fillna(data['Estimated Labour Participation Rate (%)'].mean(), inplace=True)

# Basic statistics
print(data.describe())

# Check data types
print(data.dtypes)

# Convert date column to datetime if necessary
data['Date'] = pd.to_datetime(data['Date'])

# Plotting unemployment rate over time
plt.figure(figsize=(12, 6))
sns.lineplot(x='Date', y='Estimated Unemployment Rate (%)', data=data)
plt.title('Unemployment Rate in India Over Time')
plt.xlabel('Date')
plt.ylabel('Estimated Unemployment Rate (%)')
plt.show()

# Calculate rolling mean (moving average)
data['RollingMean'] = data['Estimated Unemployment Rate (%)'].rolling(window=3).mean()

# Plot rolling mean
plt.figure(figsize=(12, 6))
sns.lineplot(x='Date', y='Estimated Unemployment Rate (%)', data=data, label='Unemployment Rate')
sns.lineplot(x='Date', y='RollingMean', data=data, label='Rolling Mean (3 months)')
plt.title('Unemployment Rate and Rolling Mean in India')
plt.xlabel('Date')
plt.ylabel('Estimated Unemployment Rate (%)')
plt.legend()
plt.show()

# Plotting unemployment rate by region
plt.figure(figsize=(12, 6))
sns.lineplot(x='Date', y='Estimated Unemployment Rate (%)', hue='Region', data=data)
plt.title('Unemployment Rate in India by Region Over Time')
plt.xlabel('Date')
plt.ylabel('Estimated Unemployment Rate (%)')
plt.legend(title='Region', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()

# Scatter plot between Unemployment Rate and Estimated Employed
plt.figure(figsize=(12, 6))
sns.scatterplot(x='Estimated Employed', y='Estimated Unemployment Rate (%)', data=data, hue='Region')
plt.title('Relationship between Estimated Employed and Unemployment Rate')
plt.xlabel('Estimated Employed')
plt.ylabel('Estimated Unemployment Rate (%)')
plt.legend(title='Region', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()

# Scatter plot between Unemployment Rate and Labour Participation Rate
plt.figure(figsize=(12, 6))
sns.scatterplot(x='Estimated Labour Participation Rate (%)', y='Estimated Unemployment Rate (%)', data=data, hue='Region')
plt.title('Relationship between Labour Participation Rate and Unemployment Rate')
plt.xlabel('Estimated Labour Participation Rate (%)')
plt.ylabel('Estimated Unemployment Rate (%)')
plt.legend(title='Region', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()

# Compute the correlation matrix
correlation_matrix = data[['Estimated Unemployment Rate (%)', 'Estimated Employed', 'Estimated Labour Participation Rate (%)']].corr()

# Plot the heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Correlation Matrix')
plt.show()

