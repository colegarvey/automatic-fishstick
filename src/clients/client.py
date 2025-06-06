from config import API_KEY, SECRET_KEY
from alpaca.trading.client import TradingClient #, GetAssetsRequest
from alpaca.data import StockHistoricalDataClient

def getTradingClient():
        
    try:
        trading_client = TradingClient(api_key=API_KEY, secret_key=SECRET_KEY)
    except Exception as e:
        print(f"Error initializing the TradingClient: {e}")
        return None

    return trading_client 
    

def getDataClient():
        
    try:
        stock_data_client = StockHistoricalDataClient(api_key=API_KEY, secret_key=SECRET_KEY)
    except Exception as e:
        print(f"Error initializing the StockHistoricalDataClient: {e}")
        return None

    return stock_data_client 