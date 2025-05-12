import numpy as np
# import pandas as pd

class Position:
    def __init__(self, data: dict):
        self.price = None
        self.quantity = None
        self.history = []


    def update(self, new_data: dict):
        self.__init__(new_data)