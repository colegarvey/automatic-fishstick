from config import API_KEY, SECRET_KEY
from alpaca.data.live import StockDataStream
from time import sleep


def getLiveQuotes(dct: dict):
    '''
    Output live quote data to the terminal
    (Args)
        dct: dictionary of account positions, symbol : obj
    '''
    try:
        live_quote_client = StockDataStream(api_key=API_KEY, secret_key=SECRET_KEY)
    except Exception as e:
        print(f"Error initializing LiveDataClient: {e}")
        live_quote_client = None
        # return


    async def quote_data_handler(data):
        print(data) # run to see output

        sleep(180) # move to main on getLiveQuotes() 
        # store data then sleep for 3 minutes

    # Move into main.py
    live_quote_client.subscribe_quotes(quote_data_handler, 'AAPL') # symbols
    live_quote_client.run()


    # 