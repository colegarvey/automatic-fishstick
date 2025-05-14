
from clients.client import *
from portfolio.acct import TradingAcct
from portfolio.pos import Position

def main():
    # create interpreter structure using match
    
    client = getTradingClient()
    account_data = client.get_account()
    account_assets = client.get_all_positions()

    Acct = TradingAcct(account_data)

    Acct.allocatePositions(account_assets)
    print(Acct.positions['AAPL'].current_price)

    return
        


if __name__ == "__main__":
    main()