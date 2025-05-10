from config import API_KEY, SECRET_KEY
from alpaca.trading.stream import TradingStream

trade_stream_client = TradingStream(api_key=API_KEY, secret_key=SECRET_KEY, paper=True)

async def trade_updates_handler(data):
    print(data)

# Output trades to the terminal window
trade_stream_client.subscribe_trade_updates(trade_updates_handler)
trade_stream_client.run()