# filename: plot_stocks.py
import matplotlib.pyplot as plt
import yfinance as yf
from datetime import date

# Define the instruments to download. We would like to see NVDA and TESLA.
companies_dict = {
 'NVDA': 'NVIDIA',
 'TSLA': 'TESLA',
}

companies = sorted(companies_dict.items(), key=lambda x: x[1])

# We would like to see the closing values YTD.
start_date = f'{date.today().year}-01-01'
end_date = date.today()

# Using yfinance to load the desired data.
data = yf.download(list(companies_dict.keys()), start=start_date, end=end_date)

# Getting just the adjusted closing prices. This will return a Pandas DataFrame
closing_data = data['Adj Close']

# Plot everything by leveraging the very powerful matplotlib package.
for company in companies:
    plt.plot(closing_data.index, closing_data[company[0]], label=company[1])

plt.legend(loc='best')
plt.title('Stock price comparison YTD')
plt.xlabel('Date')
plt.ylabel('Closing Price')
plt.grid()

plt.savefig('plot.png')