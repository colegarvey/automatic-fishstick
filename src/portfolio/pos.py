# import numpy as np
import pandas as pd
from datetime import datetime #, timedelta
from trade.data import getOneStockData, getManyStockData

class Position:
    def __init__(self, data: dict):
        self.symbol = data['symbol']
        self.latest_price = float(data['price'])
        self.qty = float(data['qty'])
        self.total_value = self.latest_price * self.qty
        self.history = pd.DataFrame([])


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


    def populateHistory(self, start=datetime(25,1,1)):
        '''
        Take in bar data and populate the position history
        '''
        data = getOneStockData(self.symbol, start)

        for item in data:
            self.history = pd.concat([self.history, pd.DataFrame([dict(item)])], ignore_index=True)
        
        self.history.drop(columns=['symbol','trade_count','vwap'], axis=1, inplace=True)
        self.history['timestamp'] = self.history['timestamp'].dt.date