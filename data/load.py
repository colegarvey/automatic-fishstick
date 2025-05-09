import pandas as pd
from alpaca_trade_api import REST, TimeFrame

from config import BASE_URL, API_KEY, SECRET_KEY

# Initialize the Alpaca API client
alpaca = REST(
    base_url=BASE_URL,
    key_id=API_KEY,
    secret_key=SECRET_KEY,
    api_version="v2",
)

def get_data(symbols, start_date, end_date, timeframe="1D"):
    """
    Load historical data for the given symbols from Alpaca API.

    Args:
        symbols (list): List of stock symbols to load data for.
        start_date (str): Start date in 'YYYY-MM-DD' format.
        end_date (str): End date in 'YYYY-MM-DD' format.
        timeframe (str): Timeframe for the data. Default is '1D'.

    Returns:
        dict: A dictionary with symbols as keys and DataFrames as values.
    """
    data = {}
    for symbol in symbols:
        try:
            print(f"Loading data for {symbol}...")

            bars = alpaca.get_bars(
                symbol,
                TimeFrame.Day,
                start=start_date,
                end=end_date,
            ).df
            bars['symbol'] = symbol
            data[symbol] = bars[['symbol', 'open', 'high', 'low', 'close', 'volume']]

            
        except Exception as e:
            print(f"Error loading data for {symbol}: {e}")
            continue
        
    combined_data = pd.concat(data.values(), axis=0)
    combined_data.set_index(['symbol', combined_data.index], inplace=True)

    return combined_data.sort_index()
