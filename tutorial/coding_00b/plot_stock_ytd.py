# filename: plot_stock_ytd.py
import yfinance as yf
import matplotlib.pyplot as plt
import datetime
import os

def main():
    # Define the stock symbols and today's date
    stocks = ['NVDA', 'TSLA']
    today = datetime.date.today()
    year_start = datetime.date(today.year, 1, 1)

    # Dictionary to store stock data
    stock_data = {}

    # Fetch the stock data YTD
    for stock in stocks:
        print(f"Downloading data for {stock}...")
        data = yf.download(stock, start=year_start, end=today)
        if data.empty:
            print(f"No data found for {stock}.")
        else:
            stock_data[stock] = data

    if not stock_data:
        print("No stock data available, exiting script.")
        return

    # Plotting the stock price changes
    plt.figure(figsize=(10, 6))
    for stock, data in stock_data.items():
        plt.plot(data.index, data['Close'], label=stock)

    plt.title('Stock Price Change YTD (NVDA & TSLA)')
    plt.xlabel('Date')
    plt.ylabel('Stock Price (USD)')
    plt.legend()
    plt.grid(True)

    # Save the plot to plot.png in the current working directory
    plot_file_path = os.path.join(os.getcwd(), 'plot.png')
    plt.savefig(plot_file_path)
    plt.close()  # Close the plot after saving
    print(f"Plot saved successfully to {plot_file_path}")

if __name__ == "__main__":
    main()