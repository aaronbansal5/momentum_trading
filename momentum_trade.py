import alpaca_trade_api as tradeapi 
import pandas as pd
from datetime import datetime, timedelta
import tradingdays
import secret


API_KEY = secret.API_KEY
API_SECRET = secret.API_SECRET
APCA_API_BASE_URL = 'https://paper-api.alpaca.markets' 
api = tradeapi.REST(API_KEY, API_SECRET, APCA_API_BASE_URL, api_version='v2')


def calculate_momentum(stock,momentum_period): 
    last_trading_day = tradingdays.getDateMarketDaysAgo(momentum_period)
    df = api.get_bars(stock, '1Day',start=last_trading_day, limit=momentum_period).df
    momentum = df['close'][-1] / df['close'][0] 
    return momentum

stock_tickers = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'NVDA', 'TSLA', 'META', 'AVGO']

stockInfo = []
for ticker in stock_tickers:
    stocky = []
    stocky.append(ticker)
    stocky.append(calculate_momentum(ticker,20))
    stocky.append(calculate_momentum(ticker,50))
    stocky.append(calculate_momentum(ticker,200))
    stockInfo.append(stocky)

print(stockInfo)