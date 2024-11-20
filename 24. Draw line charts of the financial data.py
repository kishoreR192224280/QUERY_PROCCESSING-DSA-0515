import pandas as pd
import matplotlib.pyplot as plt

# Read the financial data
data = pd.read_csv('fdata.csv')

# Convert 'Date' column to datetime
data['Date'] = pd.to_datetime(data['Date'], format='%m-%d-%y')

# Plotting the line chart
plt.plot(data['Date'], data['Open'], label='Open')
plt.plot(data['Date'], data['Close'], label='Close')

# Adding title and labels
plt.title('Financial Data of Alphabet Inc. (Oct 3, 2016 - Oct 7, 2016)')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()

# Display the plot
plt.show()
