from config import API_KEY, SECRET_KEY
from alpaca.trading.stream import TradingStream, StockDataStream

try:
    live_quote_client = StockDataStream(api_key=API_KEY, secret_key=SECRET_KEY)
except Exception as e:
    print(f"Error initializing LiveDataClient: {e}")
    live_quote_client = None


async def quote_data_handler(data):
    print(data)

# Output trades to the terminal window
live_quote_client.subscribe_quotes(quote_data_handler, '...') # symbol
live_quote_client.run()