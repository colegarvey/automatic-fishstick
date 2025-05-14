
from portfolio.pos import Position

class TradingAcct:
    def __init__(self, data: dict):
        '''
        Mock portfolio 
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

        self.positions = {} # symbol : obj
        self.history = {} # date : value


    def update(self, new_data):
        self.__init__(new_data)

    
    def allocatePositions(self, asset_data: list):
        # current price or market_value, qty or qty_available
        for item in asset_data:
            symbol = item.symbol
            price = item.current_price
            qty = item.qty

            data = {'symbol': symbol, 'price': price, 'qty': qty}
            self.positions[symbol] = Position(data)

    