# import numpy as np
import pandas as pd
from datetime import datetime #, timedelta
from trade.data import getStockData

class Position:
    def __init__(self, data: dict):
        self.symbol = data['symbol']
        self.latest_price = float(data['price'])
        self.qty = float(data['qty'])
        self.total_value = self.latest_price * self.qty
        self.history = None


    def update(self, new_data: dict):
        self.__init__(new_data)

    
    def EMA(self, days, value):
        '''
        Calculate the exponential moving average of a position over a time period
        (Args)
            days: length of the desired time period
        '''
        smoothing_factor = 2 / (days + 1)
        # ema = value * 


    def populateHistory(self, start=datetime(2020,1,1)):
        '''
        Take in bar data and populate the position history
        '''
        data = getStockData(self.symbol, start)
        if data is None:
            print(f"No data returned for symbol {self.symbol}")
            return

        try:
            rows = [item.__dict__ for item in data]
        except Exception as e:
            print(f"Error converting bar data to dict for {self.symbol}: {e}")
            return
        
        self.history = pd.DataFrame(rows)       

        # Format date into multiple numeric columns
        self.history['timestamp'] = pd.to_datetime(self.history['timestamp'])
        self.history['year'] = self.history['timestamp'].dt.year
        self.history['month'] = self.history['timestamp'].dt.month
        self.history['day'] = self.history['timestamp'].dt.day

        # Drop unnecessary columns
        self.history.drop(columns=['symbol','trade_count','vwap','timestamp'], axis=1, inplace=True, errors='ignore')
