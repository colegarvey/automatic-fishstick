from config import API_KEY, SECRET_KEY

# from alpaca.data.historical.option import OptionHistoricalDataClient, OptionLatestQuoteRequest
from alpaca.data import StockHistoricalDataClient
from alpaca.data.requests import StockLatestQuoteRequest, StockBarsRequest, StockLatestBarRequest
from alpaca.data.timeframe import TimeFrame
from datetime import datetime, timedelta




def getOneStockData(symbol: str, start=datetime(2025,1,1)):
    '''
    return bar request data for a single symbol
    (Args)
        symbol: stock ticker symbol
        start: date to specify beginning of data retrieval
    '''
    try:
        stock_data_client = StockHistoricalDataClient(api_key=API_KEY, secret_key=SECRET_KEY)
    except Exception as e:
        print(f"Error initializing DataClient: {e}")
        return None
    else:

        request = StockBarsRequest(symbol_or_symbols=symbol, start=start, timeframe=TimeFrame.Day)
        responce = stock_data_client.get_stock_bars(request)

    return responce


def getManyStockData(symbols: list, start=datetime(2025,1,1)):
    '''
    return bar request data for many symbols
    (Args)
        symbol: stock ticker symbol
        start: date to specify beginning of data retrieval
    '''
    try:
        stock_data_client = StockHistoricalDataClient(api_key=API_KEY, secret_key=SECRET_KEY)
    except Exception as e:
        print(f"Error initializing DataClient: {e}")
        return None
    else:

        request = StockBarsRequest(symbol_or_symbols=symbols, start=start, timeframe=TimeFrame.Day)
        responce = stock_data_client.get_stock_bars(request)

    return responce