# import numpy as np
# import pandas as pd
from datetime import datetime, timedelta

class Position:
    def __init__(self, data: dict):
        self.symbol = data['symbol']
        self.current_price = float(data['price'])
        self.qty = float(data['qty'])
        self.total_value = self.current_price * self.qty
        self.history = []


    def update(self, new_data: dict):
        self.__init__(new_data)

    
    # make moving average method to analyze a position
    def EMA(self, days, value):
        '''
        Calculate the exponential moving average of a position over a time period
        (Args)
            days: length of the desired time period
        '''
        smoothing_factor = 2 / (days + 1)
        ema = value * 


    def populateHistory(self, data):
        '''
        Take in close price data and populate the position history
        '''
        pass