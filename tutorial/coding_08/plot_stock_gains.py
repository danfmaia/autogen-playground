# filename: plot_stock_gains.py

import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

def fetch_data(ticker, start_date, end_date):
    try:
        data = yf.download(ticker, start=start_date, end=end_date, progress=False)
        return data['Adj Close']
    except Exception as e:
        print(f"Error fetching data for {ticker}: {e}")
        return None

# Define stocks and time period
stocks = ['TSLA', 'META']
start_date = '2024-01-01'
end_date = '2024-10-31'

# Fetch data for each stock
data = {stock: fetch_data(stock, start_date, end_date) for stock in stocks}

# Filter out any None values
data = {stock: stock_data for stock, stock_data in data.items() if stock_data is not None}

# Calculate the percentage change from the start of the year for available data
ytd_gains = {stock: (stock_data.iloc[-1] - stock_data.iloc[0]) / stock_data.iloc[0] * 100
             for stock, stock_data in data.items()}

# Plot the YTD stock price gains
plt.figure(figsize=(10, 6))
for stock, stock_data in data.items():
    plt.plot((stock_data - stock_data.iloc[0]) / stock_data.iloc[0] * 100, label=f'{stock} YTD Gain')

plt.title('YTD Stock Price Gains for TSLA and META (2024)')
plt.xlabel('Date')
plt.ylabel('Gain (%)')
plt.legend()
plt.grid(True)

# Save the plot to a file
plt.savefig('stock_gains.png')

print("Plot saved as 'stock_gains.png'.")