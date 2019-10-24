# https://www.codecademy.com/courses/analyze-financial-data-with-python-beta/lessons/why-python-finance/exercises/python-candlestick-chart?action=resume_content_item

import datetime
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from mpl_finance import candlestick_ohlc

df = pd.read_csv('AAPL_data.csv')
print(df.head())

df['Date'] = pd.to_datetime(df['Date'])
df["Date"] = df["Date"].apply(mdates.date2num)
candle_data = df[['Date', 'Open', 'High', 'Low', 'Close']]
print(candle_data.head())

f1, ax = plt.subplots(figsize = (10,5))
candlestick_ohlc(ax,candle_data.values, colorup='green',colordown='red')
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
plt.title('Candlestick Chart for AAPL')
plt.xlabel('Date')
plt.ylabel('Value($)')
plt.show()
