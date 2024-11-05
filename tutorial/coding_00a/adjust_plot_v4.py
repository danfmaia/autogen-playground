# filename: adjust_plot_v4.py
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.dates as mdates

# Example data
dates = pd.date_range(start='2023-01-01', periods=20, freq='D')
values = range(20)  # Example data set; adjust according to your data

# Handle division by zero
if values[0] == 0:
    print("Cannot calculate percentage change with an initial value of zero.")
    values_percentage = [0] * len(values)  # or handle it differently based on your needs
else:
    # Convert values to percentage change from the first value
    values_percentage = [(value / values[0] - 1) * 100 for value in values]

plt.figure(figsize=(14, 7))  # Increased figure size for better label spacing
plt.plot(dates, values_percentage)

# Set major locator with a larger interval to reduce label frequency
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=2))  # Adjust interval as needed

# Set the formatter to use shorter date format
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))

# Rotate x-axis date labels
plt.gcf().autofmt_xdate(rotation=45)  # Rotate by 45 degrees for better readability

plt.xlabel('Date')
plt.ylabel('Percentage Change (%)')  # Updated y-axis label to reflect percentage change
plt.title('Sample Plot with Percentage Change')
plt.tight_layout()  # Adjust layout to prevent clipping of tick-labels

plt.savefig('plot.png')  # Save the updated plot

print("The plot now shows percentage changes instead of price. The updated plot has been saved as 'plot.png'.")