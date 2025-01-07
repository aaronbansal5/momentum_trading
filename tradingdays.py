import pandas_market_calendars as mcal
from datetime import datetime

def getDateMarketDaysAgo(days,sched_start = '2020-01-01'):
    # Get the NYSE trading calendar
    nyse = mcal.get_calendar('NYSE')

    # Get all trading days up to today
    end_date = datetime.today()
    schedule = nyse.schedule(start_date=sched_start, end_date=end_date)

    # Convert to a list of trading dates
    trading_days = schedule.index

    # Get the date 20 trading days ago
    last_trading_day = trading_days[-days].strftime('%Y-%m-%d')
    return last_trading_day
