# filename: adjust_plot_v5.py
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.dates as mdates

# Example data: with initial value set to a non-zero number
dates = pd.date_range(start='2023-01-01', periods=20, freq='D')
# Sample values: ensuring the first value is non-zero
values = [10, 12, 15, 9, 8, 14, 18, 20, 22, 25, 30, 29, 35, 31, 34, 36, 38, 45, 50, 55]

# Convert values to percentage change from the first value
values_percentage = [(value / values[0] - 1) * 100 for value in values]

plt.figure(figsize=(14, 7))
plt.plot(dates, values_percentage)

# Set major locator with a larger interval to reduce label frequency
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=2))  

# Set the formatter to use shorter date format
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))

# Rotate x-axis date labels
plt.gcf().autofmt_xdate(rotation=45)

plt.xlabel('Date')
plt.ylabel('Percentage Change (%)')
plt.title('Sample Plot with Percentage Change')
plt.tight_layout()  # Adjust layout

plt.savefig('plot.png')

print("A meaningful plot with percentage changes has been generated and saved as 'plot.png'.")