# filename: adjust_plot_v6.py
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.dates as mdates

# Example data: 20 periods
dates = pd.date_range(start='2023-01-01', periods=20, freq='D')

# Sample values for two datasets, ensuring initial values are non-zero
values1 = [10, 12, 15, 9, 8, 14, 18, 20, 22, 25, 30, 29, 35, 31, 34, 36, 38, 45, 50, 55]
values2 = [8, 10, 13, 11, 10, 15, 17, 19, 18, 21, 24, 27, 29, 32, 30, 33, 37, 40, 42, 48]

# Convert values to percentage change from the first value of each dataset
values_percentage1 = [(value / values1[0] - 1) * 100 for value in values1]
values_percentage2 = [(value / values2[0] - 1) * 100 for value in values2]

plt.figure(figsize=(14, 7))
plt.plot(dates, values_percentage1, label='Dataset 1', color='blue')
plt.plot(dates, values_percentage2, label='Dataset 2', color='green')

# Set major locator with a larger interval to reduce label frequency
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=2))

# Set the formatter to use shorter date format
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))

# Rotate x-axis date labels
plt.gcf().autofmt_xdate(rotation=45)

plt.xlabel('Date')
plt.ylabel('Percentage Change (%)')
plt.title('Sample Plot with Two Percentage Change Lines')
plt.legend()  # Add a legend to distinguish between datasets
plt.tight_layout()  # Adjust layout

plt.savefig('plot.png')

print("A plot with two percentage change lines has been generated and saved as 'plot.png'.")