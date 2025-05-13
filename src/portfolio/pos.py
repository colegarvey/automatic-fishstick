# import numpy as np
# import pandas as pd

class Position:
    def __init__(self, data: dict):
        self.symbol = data.symbol
        self.qty = data.qty
        self.history = []


    def update(self, new_data: dict):
        self.__init__(new_data)

    
    # make moving average method to analyze a position