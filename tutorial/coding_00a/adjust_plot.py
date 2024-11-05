# filename: adjust_plot.py
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.dates as mdates

# Example data
dates = pd.date_range(start='2023-01-01', periods=10, freq='D')
values = range(10)

plt.figure(figsize=(10, 5))
plt.plot(dates, values)

# Setting a major locator for the x-axis to space out labels
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=1))

# Setting a formatter for the x-axis dates
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))

# Rotating x-axis date labels to prevent overlap
plt.gcf().autofmt_xdate(rotation=60)  # Rotate the date labels by 60 degrees

plt.xlabel('Date')
plt.ylabel('Values')
plt.title('Sample Plot with Spaced Date Labels')
plt.tight_layout()  # Adjust layout to prevent clipping of tick-labels

plt.savefig('plot.png')  # Save the adjusted plot

print("The x-axis labels were adjusted to prevent overlap, and the updated plot has been saved as 'plot.png'.")