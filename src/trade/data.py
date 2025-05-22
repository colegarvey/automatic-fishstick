from config import API_KEY, SECRET_KEY

# from alpaca.data.historical.option import OptionHistoricalDataClient, OptionLatestQuoteRequest
from alpaca.data import StockHistoricalDataClient
from alpaca.data.requests import StockLatestQuoteRequest, StockBarsRequest, StockLatestBarRequest
from alpaca.data.timeframe import TimeFrame
from datetime import datetime, timedelta


def getStockData(symbol, start=datetime(2020,1,1)):
    '''
    return bar request data for a single symbol
    (Args)
        symbol: stock ticker symbol or list of symbols
        start: date to specify beginning of data retrieval period
    '''
    try:
        stock_data_client = StockHistoricalDataClient(api_key=API_KEY, secret_key=SECRET_KEY)
    except Exception as e:
        print(f"Error initializing DataClient: {e}")
        return None
    else:

        request = StockBarsRequest(symbol_or_symbols=symbol, start=start, timeframe=TimeFrame.Day)
        response = stock_data_client.get_stock_bars(request)

    return response[symbol]
