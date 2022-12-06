import os
import json
import requests
def stock_data(ticker, tweet_times):
    # url for api request. 
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=SPY&interval=5min&outputsize=full&apikey=XK9UE7MB6UJJ1XUL'
    r = requests.get(url)
    data = r.json()
    # using the api data, create a list of times when data was reported
    stock_times = list(data['Time Series (5min)'].keys())
    # using python set functions, create a list of times where the input user tweeted, and there was stock data
    valid_times = list(set(stock_times) & set(tweet_times))
    # format for open price is data['Time Series (1min)'][time]['1. open']
    table_of_stuff = [];
    for time in valid_times:
       table_of_stuff.append([float(data['Time Series (5min)'][time]['1. open']), float(data['Time Series (5min)'][time]['4. close']), float(data['Time Series (5min)'][time]['5. volume'])])
    # format for close price is data['Time Series (1min)'][time]['4. close']
    return table_of_stuff
    #print(float(data['Time Series (1min)'][time]['1. open']))
def recent_price():
   url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=SPY&interval=5min&outputsize=full&apikey=XK9UE7MB6UJJ1XUL'
   r = requests.get(url)
   data = r.json()
   most_recent = data['Meta Data']['3. Last Refreshed']

   return [float(data['Time Series (5min)'][most_recent]['1. open']), float(data['Time Series (5min)'][most_recent]['5. volume'])]
