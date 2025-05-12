import numpy as np
import pandas as pd
from pos import Position

class TradingAcct:
    def __init__(self, data: dict, positions: list):
        '''
        (Args) 
            data: dict containing account data from the trading client 
        '''
        self._data = data
        self.buying_power = data.buying_power
        self.daytrade_count = data.daytrade_count
        self.equity = data.equity
        self.options_approved_level = data.options_approved_level
        self.options_buying_power = data.options_buying_power
        self.options_trading_level = data.options_trading_level
        self.portfolio_value = data.portfolio_value
        self.status = data.status

        self.positions = []


    def update(self, new_data):
        self.__init__(new_data)

    
    def allocatePositions(self):

    # make moving average method to analyze a position