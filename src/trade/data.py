from src.config import API_KEY, SECRET_KEY
import alpaca
# from alpaca.data.historical.option import OptionHistoricalDataClient, OptionLatestQuoteRequest
from alpaca.data.historical.stock import StockHistoricalDataClient
from alpaca.data.requests import StocklatestQuoteRequest


try:
    stock_data_client = StockHistoricalDataClient(api_key=API_KEY, secret_key=SECRET_KEY)
except Exception as e:
    print(f"Error initializing DataClient: {e}")
    stock_data_client = None


def getHistoricalStockData(lst: list or str):

